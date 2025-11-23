from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter

with open("knowledge_base/faq.txt") as f:
    data = f.read()

splitter = CharacterTextSplitter(chunk_size=200)
docs = splitter.split_text(data)

emb = OpenAIEmbeddings()
vectordb = FAISS.from_texts(docs, emb)
vectordb.save_local("embeddings")
