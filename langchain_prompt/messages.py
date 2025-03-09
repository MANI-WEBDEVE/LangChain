from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")

messages=[
    SystemMessage(content="Your are a very help full knowledge friend and only conversation in Minglish language"),
    HumanMessage(content="Tell me about the langChain framewrok?")
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)