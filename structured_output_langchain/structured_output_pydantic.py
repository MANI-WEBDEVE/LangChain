from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI

# Step 1: Define structured output with Pydantic
class PersonInfo(BaseModel):
    name: str
    age: int
    profession: str

# Step 2: Initialize your model (replace with OpenAI if needed)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

# Step 3: Use with_structured_output
structured_output = model.with_structured_output(PersonInfo)

# Step 4: Prompt
response = structured_output.invoke("Aik software engineer ka naam, age aur profession btao amaerica site.")

print(response)
