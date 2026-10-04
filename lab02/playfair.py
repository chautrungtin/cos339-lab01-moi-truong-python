"""2.5.4: Playfair 5x5, gộp J vào I, giữ ký tự đệm khi giải mã."""
from string import ascii_uppercase


def normalize(text):
    return ''.join(c for c in text.upper() if c in ascii_uppercase).replace('J', 'I')


def make_square(key):
    key = normalize(key)
    if not key:
        raise ValueError('Khóa phải chứa ít nhất một chữ cái A-Z')
    letters = ''.join(dict.fromkeys(key + ascii_uppercase.replace('J', '')))
    return [letters[i:i + 5] for i in range(0, 25, 5)]


def prepare(text):
    text = normalize(text)
    if not text:
        raise ValueError('Nội dung phải chứa ít nhất một chữ cái A-Z')
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        filler = 'Q' if a == 'X' else 'X'
        if i + 1 == len(text) or a == text[i + 1]:
            pairs.append(a + filler)
            i += 1
        else:
            pairs.append(text[i:i + 2])
            i += 2
    return ''.join(pairs)


def transform(text, key, step):
    square = make_square(key)
    positions = {c: (r, col) for r, row in enumerate(square)
                 for col, c in enumerate(row)}
    result = []
    for i in range(0, len(text), 2):
        r1, c1 = positions[text[i]]
        r2, c2 = positions[text[i + 1]]
        if r1 == r2:
            result.extend((square[r1][(c1 + step) % 5], square[r2][(c2 + step) % 5]))
        elif c1 == c2:
            result.extend((square[(r1 + step) % 5][c1], square[(r2 + step) % 5][c2]))
        else:
            result.extend((square[r1][c2], square[r2][c1]))
    return ''.join(result)


def encrypt(text, key):
    return transform(prepare(text), key, 1)


def decrypt(text, key):
    text = ''.join(text.split()).upper()
    if not text or len(text) % 2 or any(c not in ascii_uppercase.replace('J', '') for c in text):
        raise ValueError('Bản mã phải có số chữ cái chẵn, chỉ A-Z và không chứa J')
    return transform(text, key, -1)


if __name__ == '__main__':
    key, text = 'PLAYFAIR EXAMPLE', 'HIDE THE GOLD IN THE TREE STUMP'
    print('2.5.4 - PLAYFAIR')
    print('Khóa:', key)
    for row in make_square(key):
        print(' '.join(row))
    cipher = encrypt(text, key)
    print('Bản rõ:', text)
    print('Chuẩn hóa và thêm đệm:', prepare(text))
    print('Mã hóa:', cipher)
    print('Giải mã (giữ đệm):', decrypt(cipher, key))
