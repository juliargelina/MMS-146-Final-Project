#copied encryption class from the reference

import os
import string
import random


class Encryption:
    def __init__(self, key: str):
        self.key = key
        self.alphabet = string.ascii_letters + string.digits + string.punctuation + " "
        self.cipher = self._make_cipher(key)
        self.reverse_cipher = {v: k for k, v in self.cipher.items()}

    def _make_cipher(self, password: str):
        chars = list(self.alphabet)
        random.seed(password)  # makes cipher unique per password
        shuffled = chars.copy()
        random.shuffle(shuffled)
        return dict(zip(chars, shuffled))

    def encrypt(self, text: str) -> str:
        return "".join(self.cipher.get(c, c) for c in text)

    def decrypt(self, text: str) -> str:
        return "".join(self.reverse_cipher.get(c, c) for c in text)
