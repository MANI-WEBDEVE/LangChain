from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("HUGGINGFACEHUB_API_KEY")

# Configuration for HuggingFaceEndpoint:
# - repo_id: Specifies the model repository on HuggingFace Hub
# - task: Set to text-generation for chat/completion tasks
# - model: Should match the model name from repo_id

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=api_key,
     model=""
) 

model=ChatHuggingFace(llm=llm)

result=model.invoke("Acha Mujha ya batao Minglish language ma ka space time kiya hota hai")

print(result.content)