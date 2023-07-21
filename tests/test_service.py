from api_poetry.service import sentences, bigrams, paragraphs, words

import unittest


class TestTextApi(unittest.TestCase):
    def test_sentences(self):
        self.assertEqual(sentences("aaa. bbb"), ["aaa", "bbb"])
        self.assertEqual(sentences("Asta functioneaza?... sper..."), ["Asta functioneaza", "sper"])
        self.assertEqual(sentences(".bro.bbb     .stas"), "bro", ["bbb", "stas"])
        self.assertEqual(sentences(".bro...bbb     ?stas"), ["bro", "bbb", "stas"])

    def test_bigrams(self):
        self.assertEqual(bigrams("json is what    json is not"), {"json is": 2, "is what": 1, "what json": 1, "is not": 1})
        self.assertEqual(bigrams("Dormeau adanc sicriele de plumb, \nSi flori de plumb si funerar vestmint -- \nStam singur în cavou... si era vint... \nSi scirtiiau coroanele de plumb. \nDormea intors amorul meu de plumb \nPe flori de plumb, si-am inceput sa-l strig -- \nStam singur langa mort... si era frig... \nSi-i atirnau aripile de plumb."), {"de plumb": 6, "plumb si": 3, "flori de": 2, "stam singur": 2, "si era": 2})

    def test_paragraphs(self):
        self.assertEqual(paragraphs("umm\n   \nnu cred"), ["umm", "nu cred"])
        self.assertEqual(paragraphs("\n\n\nHow about     \n    \n   This one"), ["How about", "This one"])

    def test_words(self):
        self.assertEqual(words("umm\n   \nnu. cred"), ["umm", "nu", "cred"])
        self.assertEqual(words("\n\n\nHow about     \n    \n   This one"), ["How", "about", "This", "one"])


if __name__ == '__main__':
    unittest.main()
