from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")


prompt1= PromptTemplate(
    template="generate a in detail report in Minglish language for the following input: {topic}",
    input_variables=["topic"]
)

prompt2= PromptTemplate(
    template="Summarize the following detailed report into a concise 5-line summary: {text}",
    input_variables=["text"]
)


parsers=StrOutputParser()

chain1=prompt1 | model | parsers

result=chain1.invoke({"topic":"pakistan economy"})

chain2=prompt2 | model | parsers

result2=chain2.invoke({"text":result})

print(result2)




