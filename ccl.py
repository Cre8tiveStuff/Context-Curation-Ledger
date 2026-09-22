import tiktoken

_encoder = tiktoken.get_encoding("cl100k_base")


def count_tokens(text):
    return len(_encoder.encode(text))

def     fit_to_budget(chunks, max_tokens=2000):
        selected = []
        used = 0

        for chunk in chunks:
            cost = count_tokens(chunk)
            if used + cost > max_tokens:
               break
            selected.append(chunk)
            used += cost

        return selected
