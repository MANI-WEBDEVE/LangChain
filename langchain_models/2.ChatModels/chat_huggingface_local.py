# Old Code
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import os
load_dotenv()

os.environ['HF_HOME']="C:/huggingface_chache/hub/models--TinyLlama--TinyLlama-1.1B-Chat-v1.0"

llm=HuggingFacePipeline.from_model_id(
        model_id="Qwen/Qwen2.5-0.5B", #TinyLlama/TinyLlama-1.1B-Chat-v1.0
        task="text-generation",
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("hi")
print(result.content)


# import torch

# device = None

# cuda_device_count = torch.cuda.device_count()
# print(f"CUDA Device Count: {cuda_device_count}")

# print(torch.cuda.is_available())
# print(torch.cuda.current_device())
# print(torch.cuda.device_count())
# print(torch.cuda.get_device_name(0))
# print(torch.cuda.is_initialized())
# # print(torch.cuda.is_built())
# print(torch.cuda.list_gpu_processes())