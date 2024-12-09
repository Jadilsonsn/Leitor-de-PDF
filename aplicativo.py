import streamlit as st 
from streamlit_chat import message
from chat_pnl import files
from chat_pnl import embedd


def main(): 



    st.title(" Chat CCEE")
    st.subheader(":blue[Seu assistente] virtual")

    user_question = st.text_input("Experimente fazer uma pergunta!",placeholder='Digite uma pergunta ou comando')
    if('conversation' not in st.session_state):
        st.session_state.conversation = None
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    if (user_question):      

        response = st.session_state.conversation({
    'question': user_question,
    'chat_history': st.session_state.chat_history
})['chat_history'][-1]
        
        message(user_question,is_user=True)
        message(response.content, is_user=False) 

    with st.sidebar: 
     st.subheader(" Seus arquivos ") 
     pdf = st.file_uploader(" carregue seu arquivo ",accept_multiple_files=True)     
     if st.button("carregar"):
       all_files_text = files.procesar_aqr(pdf) 
       chunk = files.criar_chunks(all_files_text)        
       vectorstore = embedd.criar_vectorstore(chunk)   
       st.session_state.conversation = embedd.creat_con_chains(vectorstore) 

if __name__== "__main__":
    main()



