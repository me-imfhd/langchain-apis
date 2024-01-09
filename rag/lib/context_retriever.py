from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings

import bs4


loader = WebBaseLoader(
    web_paths=("https://www.notion.so/Week-6-1-React-Deeper-Dive-581a481892fe4d3a8e0cb5360ce8d73e",),
    bs_kwargs=dict(
        # this is helps to parse the html given by the url to text
        parse_only=bs4.SoupStrainer(
            # class_=("post-content", "post-title", "post-header")
        )
    )
)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)

def context_retriever(document):
    splits = text_splitter.split_documents(document)
    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    return retriever
