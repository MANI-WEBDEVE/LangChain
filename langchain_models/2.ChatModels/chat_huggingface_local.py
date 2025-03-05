from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import os
load_dotenv()

os.environ['HF_HOME']="E:/huggingface_chache"

llm=HuggingFacePipeline.from_model_id(
        model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("What is the capital of Pakistan?")
print(result.content)