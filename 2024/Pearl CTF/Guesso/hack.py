from collections import defaultdict
from typing import Any, MutableMapping, MutableSet
from gensim.downloader import load
from gensim.matutils import unitvec
import numpy as np
from socket import AF_INET, socket
from ssl import SOCK_STREAM
from time import sleep

RECEIVE_SIZE = 1024


def load_model() -> MutableMapping[str, Any]:
    model = load(
        "word2vec-google-news-300"
    )  # gensim.models.KeyedVectors.load_word2vec_format("", binary=True)
    words = [w for w in model.index_to_key if w.lower() == w]
    vectors = np.array([unitvec(model[w]) for w in words])
    return {k: v for k, v in zip(words, vectors)}


def send_and_recv(socket: socket, text: str):
    print(text)
    socket.send(f"{text}\n".encode())
    ret = socket.recv(RECEIVE_SIZE).decode("utf-8")
    print(ret, end="")
    return ret


def main():
    model = load_model()
    words = ["google", "news", "capture", "flag", "the"]
    reverse_lookups = defaultdict[str, MutableMapping[float, MutableSet[str]]](
        lambda: defaultdict(set)
    )
    for word in words:
        my_vector = model[word]
        for other_word, other_vector in model.items():
            reverse_lookups[word][round(np.dot(my_vector, other_vector) * 100, 2)].add(
                other_word
            )
    while True:
        candidates = set[str]()
        s = socket(AF_INET, SOCK_STREAM)
        try:
            s.connect(("dyn.ctf.pearlctf.in", 30021))
            s.recv(RECEIVE_SIZE)
            for word in words:
                print(f"(number of candidates: {len(candidates)})")
                if len(candidates) == 1:
                    word = next(iter(candidates))
                ret = send_and_recv(s, word)
                if "Similarity to the target word: " in ret:
                    similarity = round(
                        float(
                            ret[
                                ret.find("Similarity to the target word: ")
                                + len("Similarity to the target word: ") :
                            ].splitlines()[0]
                        ),
                        2,
                    )
                    matching = reverse_lookups[word][similarity]
                    if candidates:
                        candidates &= matching
                    else:
                        candidates = matching
                elif "Congratulations" in ret:
                    return
        finally:
            s.close()


if __name__ == "__main__":
    main()
