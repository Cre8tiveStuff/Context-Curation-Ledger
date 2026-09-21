import tiktoken

_encoder = tiktoken.get_encoding("cl100k_base")


def count_tokens(text):
    return len(_encoder.encode(text))