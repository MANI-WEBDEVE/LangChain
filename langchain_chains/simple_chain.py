from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")


prompt= PromptTemplate(
    template="generate a in detail report in Minglish language for the following input: {input}",
    input_variables=["input"]
)


parsers=StrOutputParser()


chain = prompt | model | parsers

result=chain.invoke({"input":"time machine"})

print(result)

