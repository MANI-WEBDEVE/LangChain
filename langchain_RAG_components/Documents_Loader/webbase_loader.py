from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

url="http://m-inam.vercel.app/projects"

loader=WebBaseLoader(url)

docs=loader.load()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser=StrOutputParser()

prompt=PromptTemplate(
    template="read the Given text and analyze and explain \n {text}",
    input_variables=['text']
)


chain=prompt | model | parser

print(chain.invoke({"text": docs}))