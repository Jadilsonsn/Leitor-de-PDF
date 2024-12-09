from PyPDF2 import PdfReader # Extrai informações de pdfs 
from langchain.text_splitter import CharacterTextSplitter # divide o pdf em parte menores 
 
def procesar_aqr(arquivos):
      text = ""
      for arquivo in arquivos:
       pdf = PdfReader(arquivo)
       for page in pdf.pages:
         text += page.extract_text()
       return text 


def criar_chunks(text):  # Função para qubrar textos  
   text_splitter = CharacterTextSplitter(
      separator="/n",
      chunk_size = 300,
      chunk_overlap = 100, 
      length_function = len
   ) 
   chunk = text_splitter.split_text(text) 
   return chunk 
   
