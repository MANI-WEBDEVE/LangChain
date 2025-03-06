from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.8)


st.set_page_config(
    page_icon="🔬",
    page_title="Research Paper"
)
st.header("Research Paper Summarizer 🔬")
st.write("Summarize the research paper so easy way")

paper_title = st.selectbox(
    "Select the research paper title",
   [
    "Attention Is All You Need", 
    "BERT: Pre-training of Deep Bidirectional Transformers", 
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis",
    "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
    ]
)

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# load the prompt template
template=load_prompt("prompt_template.json")




if st.button("Summarize"):
    # create a chain 
    chain = template | model
    # invoke the prompt template
    result=chain.invoke(
        {
            "paper_title": paper_title,
            "style_input": style_input,
            "length_input": length_input
        }
    )
    st.write(result.content)