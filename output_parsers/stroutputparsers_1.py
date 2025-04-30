
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()


model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")


template1= PromptTemplate(
    template="ey bhai, ek dum detail mein report banao Minglish mein, jo bhi input diya hai uske baare mein. Samjha kya? {input}",
    input_variables=["input"]
)

template2= PromptTemplate(
    template="Chal, yeh report ka text ko 5 line mein simplify karo aur Minglish mein batao: {text}",
    input_variables=["text"]
)
parsers=StrOutputParser()

chain = template1 | model | parsers | template2 | model | parsers

result=chain.invoke({"input":"time machine"})

print(result)