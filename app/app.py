from flask import Flask, render_template, request
from urllib.request import urlopen
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Top Page', message='ISBNコードを入力してください')


@app.route('/', methods=['POST'])
def post():
    isbn_code = request.form.get('isbn')

    query = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(isbn_code)

    try:
        response = urlopen(query).read()
        res_dict = json.loads(response)['items'][0]['volumeInfo']
    except Exception:
        return render_template('index.html', title='Top Page', message='本が見つかりませんでした\n再度ISBNコードを入力してください')

    data = {
        'title': res_dict['title'],
        'authors': ', '.join(res_dict['authors']),
        'published_date': res_dict['publishedDate'],
        'description': res_dict['description'],
        'isbn_code': isbn_code,
        'thumbnail': res_dict['imageLinks']['thumbnail'],
    }

    return render_template('confirm.html', title='Book Information', book_data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
