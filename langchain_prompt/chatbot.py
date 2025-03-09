from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.8)

chat_histroy = [
    SystemMessage(content="tum mare ak perfect AI engineer ho jo mujha is field ko master karna ma maded kara ga")
]


while True:
    user_input=input("Enter your prompt: ")
    chat_histroy.append(HumanMessage(content=user_input))
    if user_input=="exit":
        print("Exiting")
        break
    result=model.invoke(chat_histroy)
    chat_histroy.append(AIMessage(content=result.content))

print(chat_histroy)