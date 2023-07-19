import openai

class Tokenizer:
    def __init__(self):
        self.api = openai.Api()

    def split_into_chunks(self, text, chunk_size):
        tokens = self.api.tokenize(text)
        return [tokens[i:i+chunk_size] for i in range(0, len(tokens), chunk_size)]
