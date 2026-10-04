"""2.5.1: Caesar trên bảng chữ cái Latin A-Z, a-z."""


def caesar(text, shift):
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            base = ord('A')
        elif 'a' <= char <= 'z':
            base = ord('a')
        else:
            result.append(char)
            continue
        result.append(chr((ord(char) - base + shift) % 26 + base))
    return ''.join(result)


def encrypt(text, key):
    return caesar(text, key)


def decrypt(text, key):
    return caesar(text, -key)


if __name__ == '__main__':
    text, key = 'HUTECH - Chau Trung Tin 2410060248', 3
    cipher = encrypt(text, key)
    print('2.5.1 - CAESAR')
    print('Bản rõ:', text)
    print('Khóa:', key)
    print('Mã hóa:', cipher)
    print('Giải mã:', decrypt(cipher, key))
