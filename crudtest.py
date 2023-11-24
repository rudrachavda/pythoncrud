from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Book 1"},
    {"id": 2, "title": "Book 2"}
]

# CRUD operations
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        method = request.form.get('method')
        book_id = int(request.form.get('book_id'))
        title = request.form.get('title')

        if method == 'GET':
            return get_books()
        elif method == 'POST':
            return create_book(title)
        elif method == 'PUT':
            return update_book(book_id, title)
        elif method == 'DELETE':
            return delete_book(book_id)

    return render_template('index.html', books=books)

def get_books():
    return jsonify({"books": books})

def create_book(title):
    new_book = {"id": len(books) + 1, "title": title}
    books.append(new_book)
    return jsonify({"message": "Book created", "book": new_book}), 201

def update_book(book_id, title):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        book['title'] = title
        return jsonify({"message": "Book updated", "book": book})
    else:
        return jsonify({"message": "Book not found"}), 404

def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({"message": "Book deleted"})

if __name__ == '__main__':
    app.run(debug=True)
