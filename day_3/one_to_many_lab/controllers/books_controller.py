from flask import Flask, render_template, Blueprint, request, redirect
from repos import book_repo, author_repo
from models.book import Book
from models.author import Author

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/')
def homepage():
    return render_template('/books/index.html')

@books_blueprint.route('/books')
def booklist():
    books = book_repo.select_all()
    return render_template('/books/booklist.html', books=books)

#CREATE NEW
# "/books/new"
@books_blueprint.route('/books/new')
def new_form():
    return render_template('books/new.html')

@books_blueprint.route('/books', methods=['POST'])
def submit_new():
    title = request.form['title']
    author = request.form['author']
    price = request.form['price']
    author = Author(author)
    author = author_repo.create(author)
    book = Book(title, author, price)
    book_repo.create(book)
    return redirect('/books')

@books_blueprint.route('/books/<book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book_repo.delete(book_id)
    return redirect('/books')

@books_blueprint.route('/books/<book_id>/edit')
def edit_book_form(book_id):
    book = book_repo.select(book_id)
    return render_template('/books/edit.html', book=book)

@books_blueprint.route('/books/<book_id>/update', methods=['POST'])
def edit_book(book_id, author_id):
    title = request.form['title']
    author = request.form['author']
    price = request.form['price']
    author = Author(author, author_id)
    author = author_repo.select(author_id)
    book = Book(title, author, price, book_id)
    book_repo.update(book)
    return redirect('/books')