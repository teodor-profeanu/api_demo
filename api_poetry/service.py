import re
import string
from collections import Counter


def remove_punctuation(text):
    translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
    return text.translate(translator)


def words(text):
    return remove_punctuation(text).split()


def sentences(text):
    return [x.strip() for x in re.split(r'[.!?]', text) if len(x.strip()) > 0]


def paragraphs(text):
    return [x for x in text.split('\n') if len(x.strip()) > 0]


def bigrams(text):
    words = remove_punctuation(text).lower().split()
    pairs = [' '.join([words[i], words[i + 1]]) for i in range(0, len(words) - 1)]
    counter = Counter(pairs).most_common()
    max_size = 5 if len(counter) > 5 else len(counter)
    return {counter[i][0]: counter[i][1] for i in range(0, max_size)}
