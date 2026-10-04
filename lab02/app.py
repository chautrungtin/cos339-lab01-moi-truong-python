"""2.5.6: Giao diện Flask cho Caesar và Playfair."""
from flask import Flask, render_template, request
from lab02 import caesar, playfair

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024


@app.route('/', methods=['GET', 'POST'])
def index():
    values = {'algorithm': 'caesar', 'operation': 'encrypt',
              'text': 'HUTECH - Chau Trung Tin 2410060248', 'key': '3'}
    result, error, square, prepared = None, None, None, None
    if request.method == 'POST':
        values = {key: request.form.get(key, '') for key in values}
        try:
            if not values['text'].strip():
                raise ValueError('Vui lòng nhập nội dung')
            if values['operation'] not in ('encrypt', 'decrypt'):
                raise ValueError('Thao tác không hợp lệ')
            if values['algorithm'] == 'caesar':
                try:
                    key = int(values['key'])
                except ValueError:
                    raise ValueError('Khóa Caesar phải là số nguyên') from None
                fn = caesar.encrypt if values['operation'] == 'encrypt' else caesar.decrypt
                result = fn(values['text'], key)
            elif values['algorithm'] == 'playfair':
                square = playfair.make_square(values['key'])
                fn = playfair.encrypt if values['operation'] == 'encrypt' else playfair.decrypt
                result = fn(values['text'], values['key'])
                if values['operation'] == 'encrypt':
                    prepared = playfair.prepare(values['text'])
            else:
                raise ValueError('Thuật toán không hợp lệ')
        except ValueError as exc:
            error = str(exc)
    return render_template('index.html', values=values, result=result,
                           error=error, square=square, prepared=prepared), 400 if error else 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=False)
