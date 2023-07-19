import streamlit as st
from tokenizer import Tokenizer

tokenizer = Tokenizer()

def split_text(text, chunk_size):
    return tokenizer.split_into_chunks(text, chunk_size)

st.title('ChatGPT Splitter')

uploaded_file = st.file_uploader("Upload file", type=['txt', 'pdf', 'docx', 'doc', 'xml'])
chunk_size = st.number_input('Enter chunk size', min_value=1, value=4000, step=1000)
prompt = st.text_input('Enter prompt', 'Act as a document/text loader until you load and remember the content of the next text/s or document/s. There might be multiple files, each file is marked by name in the format ### DOCUMENT NAME. I will send them to you in chunks. Each chunk start will be noted as [START CHUNK x/TOTAL], and the end of this chunk will be noted as [END CHUNK x/TOTAL], where x is the number of the current chunk and TOTAL is the number of all chunks I will send you. I will send you multiple messages with chunks, for each message just reply OK: [CHUNK x/TOTAL], don\'t reply anything else, don\'t explain the text! Let\'s begin:')

file_content = None
if uploaded_file is not None:
    file_content = uploaded_file.read().decode()
elif st.button('Or paste your text'):
    file_content = st.text_area('Paste your text here')

if file_content is not None:
    chunks = split_text(file_content, chunk_size)
    for i, chunk in enumerate(chunks):
        st.write(f'Chunk {i+1}:')
        st.write(chunk)
        st.button('Copy text')
