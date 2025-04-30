from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser , ResponseSchema
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")


schema=[
    ResponseSchema(name="fact_1", description="Fact 1 about the Given topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the Given topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the Given topic"),
]

parser=StructuredOutputParser.from_response_schemas(schema)

prompt=PromptTemplate(
    template="Give me 5 facts about {topic} \n {output_parser}",
    input_variables=["topic"],
    partial_variables={"output_parser": parser.get_format_instructions()},
)

chain = prompt | model | parser

result = chain.invoke({"topic": "Python programming language"})

print(result["fact_1"])