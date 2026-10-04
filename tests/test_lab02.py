import unittest
from lab02 import caesar, playfair
from lab02.app import app


class CipherTests(unittest.TestCase):
    def test_caesar_vector(self):
        self.assertEqual(caesar.encrypt('Abc XYZ! 248', 3), 'Def ABC! 248')

    def test_caesar_roundtrip(self):
        for key in (-53, -1, 0, 3, 26, 100):
            text = 'HUTECH / Tín 248!'
            self.assertEqual(caesar.decrypt(caesar.encrypt(text, key), key), text)

    def test_playfair_vector(self):
        key = 'PLAYFAIR EXAMPLE'
        text = 'HIDE THE GOLD IN THE TREE STUMP'
        expected = 'BMODZBXDNABEKUDMUIXMMOUVIF'
        self.assertEqual(playfair.encrypt(text, key), expected)
        self.assertEqual(playfair.decrypt(expected, key), 'HIDETHEGOLDINTHETREXESTUMP')

    def test_playfair_repeated_and_padding(self):
        for text in ('BALLOON', 'XX', 'X', 'JIG', 'A', 'HELLO WORLD'):
            cipher = playfair.encrypt(text, 'HUTECH')
            self.assertEqual(playfair.decrypt(cipher, 'HUTECH'), playfair.prepare(text))
        self.assertEqual(playfair.prepare('XX'), 'XQXQ')

    def test_playfair_invalid(self):
        for text in ('ABC', 'AB1C', 'AJ', ''):
            with self.assertRaises(ValueError):
                playfair.decrypt(text, 'KEY')
        with self.assertRaises(ValueError):
            playfair.make_square('123')

    def test_flask_get_and_encrypt(self):
        client = app.test_client()
        self.assertEqual(client.get('/').status_code, 200)
        response = client.post('/', data={'algorithm': 'caesar', 'operation': 'encrypt', 'text': 'ABC', 'key': '3'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'DEF', response.data)

    def test_flask_playfair_and_error(self):
        client = app.test_client()
        response = client.post('/', data={'algorithm': 'playfair', 'operation': 'decrypt', 'text': 'BMODZBXDNABEKUDMUIXMMOUVIF', 'key': 'PLAYFAIR EXAMPLE'})
        self.assertIn(b'HIDETHEGOLDINTHETREXESTUMP', response.data)
        response = client.post('/', data={'algorithm': 'caesar', 'operation': 'encrypt', 'text': 'ABC', 'key': 'abc'})
        self.assertEqual(response.status_code, 400)

    def test_html_escaping(self):
        response = app.test_client().post('/', data={'algorithm': 'caesar', 'operation': 'encrypt', 'text': '<script>alert(1)</script>', 'key': '0'})
        self.assertNotIn(b'<script>', response.data)
        self.assertIn(b'&lt;script&gt;', response.data)


if __name__ == '__main__':
    unittest.main()
