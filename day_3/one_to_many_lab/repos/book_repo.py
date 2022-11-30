from db.run_sql import run_sql
from repos import author_repo
from models.book import Book

def create(book):
    sql = "INSERT INTO books (title, author_id, price) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.price]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def select(id):
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    return results[0]

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repo.select(row['id'])
        book = Book(row['title'], author, row['price'], row['id'] )
        books.append(book)
    return books 


def update(book):
    sql = "UPDATE books SET (title, author, price, id) = (%s, %s, %s, %s) WHERE id = %s RETURNING *"
    values = [book.title, book.author.id, book.price, book.id]
    results = run_sql(sql, values)
    return results

def get_book_by_author(author_id):
    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [author_id]
    results = run_sql(sql, values)
    return results