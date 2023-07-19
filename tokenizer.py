import tiktoken


class Tokenizer:
    def __init__(self):
        self.enc = tiktoken.encoding_for_model("gpt-4")

    def split_into_chunks(self, text, chunk_size):
        tokens = self.enc.encode(text)
        return [tokens[i:i+chunk_size] for i in range(0, len(tokens), chunk_size)]

    def chunks_to_text(self, chunks):
        return [self.enc.decode(chunk) for chunk in chunks]
