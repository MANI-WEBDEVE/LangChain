from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser, JsonOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

class FeedBack(BaseModel):

    sentiment: Literal["Positive", "Negative"]=Field(description="Give the sentiment about the feedback")


parser=StrOutputParser()

parser1=PydanticOutputParser(pydantic_object=FeedBack)

parser2=JsonOutputParser()

prompt1=PromptTemplate(
    template="given the feedback and analysis the feeback its Positive to return the text Positive \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser1.get_format_instructions()}
)

prompt2=PromptTemplate(
    template="if feedback sentiment its positive to appriciate the user and recommand the related product"
)
prompt3=PromptTemplate(
    template="if feedback sentiment its negative to sorry the user and recommand to contact customer support team"
)

answere_feedback=RunnableBranch(
    (lambda x:x['sentiment'] == "Positive", prompt2 | model | parser),
    (lambda x:x['sentiment'] == "Negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Not detail found please contact customer support")
)


feedback_classifier=prompt1 | model | parser2 


chain = feedback_classifier | answere_feedback


print(chain.invoke({"feedback":"this phone is very terriable i wish not purchase this phone"}))






