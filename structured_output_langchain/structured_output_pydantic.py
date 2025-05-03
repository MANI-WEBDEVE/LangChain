from pydantic import BaseModel, Field, field_validator
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

"""
BaseModel: Pydantic ka core class, jisse data schema define karte hain.

Field: Fields ke descriptions aur constraints add karne ke liye (e.g., description="...").

field_validator: Custom validation rules banane ke liye 18.

"""

class Joke(BaseModel):
    """Joke to tell user."""
    
    setup: str = Field(description="Joke ka setup, question form mein")
    punchline: str = Field(description="Joke ka punchline, answer form mein")
    rating: int = Field(ge=1, le=10, description="Joke ka rating 1-10 ke beech")

    @field_validator('setup')
    def validate_setup(cls, v):
        if v[-1] != '?':
            raise ValueError("Setup must end with '?'")
        return v
    
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

structured_output = model.with_structured_output(Joke)

try:
    joke = structured_output.invoke("Tell me a joke about WOMEN in Hindi and every time new joke generate")
    print(joke)
except Exception as e:
    print(f"Error: {e}")