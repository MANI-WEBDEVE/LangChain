from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Book(BaseModel):
    title: str = Field(description="Title of the book")
    author: str = Field(description="Author of the book")
    year: int = Field(description="Year of publication")
    genre: str = Field(description="Genre of the book")
    summary: str = Field(description="Summary of the book")


parser=PydanticOutputParser(pydantic_object=Book)

template=PromptTemplate(
    template="Give me a {topic} book recommendation in the following format: \n{format_instruction} ",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)



chain = template | model | parser

result = chain.invoke({"topic": "horror"})

print(dict(result))
