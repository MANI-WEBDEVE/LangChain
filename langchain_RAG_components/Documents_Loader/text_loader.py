from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")


loader=TextLoader("./sample.txt")

docs=loader.load()

parser=StrOutputParser() 

prompt=PromptTemplate(
    template="please tell me what is text meaning \n {text}",
    input_variables=['text']
)

chain = prompt | model | parser

print(chain.invoke({'text':docs[0]}))

# print(docs)

# print(type(docs))

# print(len(docs))

# print(docs[0])

# print(type(docs[0]))

# print(docs[0].metadata)

# print(docs[0].page_content)