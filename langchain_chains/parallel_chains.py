from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
# Removed unused import of StrOutputParser

load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")
model2 = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt1 = PromptTemplate(
    template="generate a in detail easy notes in Minglish language for the following topic: {notes}",
    input_variables=["notes"]
)

prompt2 = PromptTemplate(
    template="generate a quizes in Minglish language for the following topic: {notes}",
    input_variables=["notes"]
)

prompt3 = PromptTemplate( 
    template="merge the following notes and quizes into a single document: {notes} and {quizes}",
    input_variables=["notes", "quizes"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "notes": prompt1 | model1 | parser,
        "quizes": prompt2 | model2 | parser,
    }
) 

merged_chain = prompt3 | model2 | parser

chain = parallel_chain | merged_chain

result=chain.invoke({"notes": "linear Regression"})

print(result)

chain.get_graph().print_ascii()