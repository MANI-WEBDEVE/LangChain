'''
LangChain ka with_structured_output() ab zyada Pydantic models ke sath compatible hai, especially jab aap Google Generative AI (gemini) ya similar LLMs use kar rahe ho. TypedDict mostly OpenAI Chat Models ke sath smooth chalta hai, lekin Google LLMs mein Pydantic preferred hai.
'''

from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# create a a data structure format 
class PersonInfo(TypedDict):

    name: str
    age: int
    profession: str

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")


# result = model.invoke("")
structured_output=model.with_structured_output(PersonInfo)

result = structured_output.invoke("mujha ak software engineer ka naam , age aur profession batao ")


print(result)

