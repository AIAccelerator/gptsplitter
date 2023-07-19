import mimetypes
import streamlit as st
from tokenizer import Tokenizer

def main():
    tokenizer = Tokenizer()

    def split_text(text, chunk_size, prompt):
        return tokenizer.split_into_chunks(text, chunk_size, prompt)

    st.title('ChatGPT Splitter')

    uploaded_file = st.file_uploader("Upload file", type=['txt', 'pdf', 'docx', 'doc'])
    chunk_size = st.number_input('Enter chunk size', min_value=1, value=4000, step=1000)
    prompt = st.text_area('Enter prompt', 'Act as a document/text loader until you load and remember the content of the next text/s or document/s. There might be multiple files, each file is marked by name in the format ### DOCUMENT NAME. I will send them to you in chunks. Each chunk start will be noted as [START CHUNK x/TOTAL], and the end of this chunk will be noted as [END CHUNK x/TOTAL], where x is the number of the current chunk and TOTAL is the number of all chunks I will send you. I will send you multiple messages with chunks, for each message just reply OK: [CHUNK x/TOTAL], don\'t reply anything else, don\'t explain the text! Let\'s begin:')

    file_content = None
    if uploaded_file is not None:
        from file_handler import PDFHandler, DocHandler, TextFileHandler

    if uploaded_file is not None:
        mimetype = mimetypes.guess_type(uploaded_file.name)[0]
        if mimetype == 'application/pdf':
            handler = PDFHandler()
        elif mimetype == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            handler = DocHandler()
        elif mimetype == 'text/plain':
            handler = TextFileHandler()
        else:
        pass
    else:
        pass
        st.write(f"Unsupported file type: {mimetype}")
        handler = None
    elif uploaded_file is None:
        handler = None

    if handler is not None:
        file_content = handler.read(uploaded_file)
        file_content = file_content.decode('utf-8') if isinstance(file_content, bytes) else file_content
    elif st.button('Or paste your text', key='unique_key_2'):
        file_content = st.text_area('Paste your text here')

    if file_content is not None:
        chunks = split_text(file_content, chunk_size, prompt)
        for i, chunk in enumerate(chunks):
            if i == 0:
                st.text_area(f'Chunk {i+1}', prompt + chunk, key=f'chunk_{i}')
            else:
        pass
                st.text_area(f'Chunk {i+1}', chunk, key=f'chunk_{i}')
        
