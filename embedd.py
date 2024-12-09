
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS # Bando de dados vetorial local
from langchain_community.chat_models import ChatOllama # Chat 
from langchain.memory import ConversationBufferMemory 
from langchain.chains import conversational_retrieval
from langchain.chains import ConversationalRetrievalChain

def criar_vectorstore(chunk):
    embeddings = OllamaEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunk, embedding=embeddings)
    return vectorstore 

def creat_con_chains(vectorstore):
    llm = ChatOllama()
    memory = ConversationBufferMemory(      
      return_messages=True,
      human_prefix =  "Human",
      ai_prefix = "AI",
      memory_key = "chat_history"
    )

    con_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever =vectorstore.as_retriever(),
        memory=memory

    ) 
    return con_chain 