import tiktoken

_encoder = tiktoken.get_encoding("cl100k_base")


def count_tokens(text):
    return len(_encoder.encode(text))


def fit_to_budget(chunks, max_tokens=2000):
    selected = []
    used = 0

    for chunk in chunks:
        cost = count_tokens(chunk)
        if used + cost > max_tokens:
            break
        selected.append(chunk)
        used += cost

    return selected


def position_aware_order(ranked_chunks):
    if len(ranked_chunks) <= 2:
        return ranked_chunks

    result = [None] * len(ranked_chunks)
    front = 0
    back = len(ranked_chunks) - 1

    for i, chunk in enumerate(ranked_chunks):
        if i % 2 == 0:
            result[front] = chunk
            front += 1
        else:
            result[back] = chunk
            back -= 1

    return result