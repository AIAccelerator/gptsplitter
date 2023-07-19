import tiktoken
class Tokenizer:
    def __init__(self):
        self.tokenizer = tiktoken.encoding_for_model("gpt-4")
    def split_into_chunks(self, text, chunk_size, prompt):
        tokens = list(self.tokenizer.encode(text))
        chunks = [tokens[i:i+chunk_size] for i in range(0, len(tokens), chunk_size)]
        total = len(chunks)
        
        return [f' {prompt} [START CHUNK {i+1}/{total}]\n' + ''.join([self.tokenizer.decode([token]) for token in chunk]) + '\n[END CHUNK {i+1}/{total}]' for i, chunk in enumerate(chunks)]
    def chunks_to_text(self, chunks):
        return [' '.join(chunk.split('\n')[1].split()) for chunk in chunks]