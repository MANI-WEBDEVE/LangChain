# its is Base LLM model usage it not recommanded 

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


llm=GoogleGenerativeAI(model="gemini-2.0-flash")
result=llm.invoke("What is the capital of Pakistan")
print(result)
