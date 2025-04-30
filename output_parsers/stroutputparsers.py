from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("HUGGINGFACEHUB_API_KEY")

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Configuration for HuggingFaceEndpoint:
# - repo_id: Specifies the model repository on HuggingFace Hub
# - task: Set to text-generation for chat/completion tasks
# - model: Should match the model name from repo_id

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     huggingfacehub_api_token=api_key,
#      model=""
# ) 

# model=ChatHuggingFace(llm=llm)

template1= PromptTemplate(
    template="generate a in detail report in Minglish language for the following input: {input}",
    input_variables=["input"]
)

template2= PromptTemplate(
    template="simplify the following report text in Minglish language: {text}",
    input_variables=["text"]
)

prompt1=template1.invoke({"input":"time machine"})

result=model.invoke(prompt1)

prompt2=template2.invoke({"text":result.content})

result1=model.invoke(prompt2)

print(result1.content)
