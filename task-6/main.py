# %pip install langchain
# %pip install OpenAI
# %pip install PyPDF2
# %pip install python-dotenv
# %pip install streamlit
# %pip install faiss-cpu
# %pip install streamlit-extras
# %pip install PyMuPDF
# %pip install -U langchain-community
# %pip install tiktoken


from dotenv import load_dotenv # type: ignore
import streamlit as st # type: ignore
import fitz # type: ignore # install using: pip install PyMuPDF

from PyPDF2 import PdfReader # type: ignore
from streamlit_extras.add_vertical_space import add_vertical_space # type: ignore
from langchain.text_splitter import CharacterTextSplitter # type: ignore
from langchain.embeddings.openai import OpenAIEmbeddings # type: ignore
from langchain.vectorstores import FAISS # type: ignore
from langchain.chains.question_answering import load_qa_chain # type: ignore
from langchain.llms import OpenAI # type: ignore
from langchain.callbacks import get_openai_callback # type: ignore

load_dotenv()

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf[page_num]
            text += page.get_text()
    return text

# pdf_path = "../data/task-5/Operations Management.pdf"
pdf = st.file_uploader("Upload your PDF File and Ask Questions", type="pdf")
text= extract_text_from_pdf(pdf)

# split into chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
    )
chunks = text_splitter.split_text(text)

#create embeddings
embeddings = OpenAIEmbeddings()
knowledge_base = FAISS.from_texts(chunks, embeddings)

llm = OpenAI()
chain = load_qa_chain(llm, chain_type="stuff")
with get_openai_callback() as cb:
    response = chain.run(input_documents=docs, question=user_question)
    print(cb)
           
st.write(response)


# Sidebar contents
with st.sidebar:
    st.title('💬PDF Summarizer and Q/A App')

    add_vertical_space(2)
    st.write('Made for Resolute-Ai intern assignment Task-6 of pdf q/a')
    add_vertical_space(2)    
    st.write('Made by Aryan Sharma')

def main():
    load_dotenv()

    #Main Content
    st.header("Ask About Your PDF 🤷‍♀️💬")


# show user input
with st.chat_message("user"):
    st.write("Hello World👋")
    user_question = st.text_input("Please ask a question about your PDF here:")
    if user_question:
        docs = knowledge_base.similarity_search(user_question)