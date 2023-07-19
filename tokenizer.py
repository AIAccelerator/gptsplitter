import tiktoken


class Tokenizer:
    def __init__(self):
        self.enc = tiktoken.encoding_for_model("gpt-4")

    def split_into_chunks(self, text, chunk_size, prompt):
        tokens = self.enc.encode(text)
        chunks = [tokens[i:i+chunk_size] for i in range(0, len(tokens), chunk_size)]
        total = len(chunks)
        chunks[0] = prompt + str(chunks[0])
        return [f'[START CHUNK {i+1}/{total}]\n{" ".join(map(str, chunk))}\n[END CHUNK {i+1}/{total}]' for i, chunk in enumerate(chunks)]

    def chunks_to_text(self, chunks):
        return [self.enc.decode(chunk.split('\n')[1]) for chunk in chunks]
