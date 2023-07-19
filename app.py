import streamlit as st

def split_text(text, chunk_size):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

st.title('ChatGPT Splitter')

uploaded_file = st.file_uploader("Upload file", type=['txt', 'pdf', 'docx'])
chunk_size = st.number_input('Enter chunk size', min_value=1, value=1000)

if uploaded_file is not None:
    file_content = uploaded_file.read().decode()
elif st.button('Or paste your text'):
    file_content = st.text_area('Paste your text here')

if file_content:
    chunks = split_text(file_content, chunk_size)
    for i, chunk in enumerate(chunks):
        st.write(f'Chunk {i+1}:')
        st.write(chunk)
