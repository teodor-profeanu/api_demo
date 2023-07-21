from api_poetry.main import sentences, bigrams, TextItem, paragraphs

import unittest


class TestTextApi(unittest.TestCase):
    def test_sentences(self):
        self.assertEqual(sentences(TextItem(**{"text": "aaa. bbb"})), {"sentences": ["aaa", "bbb"]})
        self.assertEqual(sentences(TextItem(**{"text": "Asta functioneaza?... sper..."})), {"sentences": ["Asta functioneaza", "sper"]})
        self.assertEqual(sentences(TextItem(**{"text": ".bro.bbb     .stas"})), {"sentences": ["bro", "bbb", "stas"]})
        self.assertEqual(sentences(TextItem(**{"text": ".bro...bbb     ?stas"})), {"sentences": ["bro", "bbb", "stas"]})

    def test_bigrams(self):
        self.assertEqual(bigrams(TextItem(**{"text": "json is what    json is not"})), {"bigrams": {"json is": 2, "is what": 1, "what json": 1, "is not": 1}})
        self.assertEqual(bigrams(TextItem(**{"text": "Dormeau adanc sicriele de plumb, \nSi flori de plumb si funerar vestmint -- \nStam singur în cavou... si era vint... \nSi scirtiiau coroanele de plumb. \nDormea intors amorul meu de plumb \nPe flori de plumb, si-am inceput sa-l strig -- \nStam singur langa mort... si era frig... \nSi-i atirnau aripile de plumb."})), {"bigrams": {"de plumb": 6, "plumb si": 3, "flori de": 2, "stam singur": 2, "si era": 2}})

    def test_paragraphs(self):
        self.assertEqual(paragraphs(TextItem(**{"text": "umm\n   \nnu cred"})), {"paragraphs": ["umm", "nu cred"]})


if __name__ == '__main__':
    unittest.main()
