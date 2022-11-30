from db.run_sql import run_sql
from models.author import Author



def create(author):
    sql = "INSERT INTO authors (author_name) VALUES (%s) RETURNING *"
    values = [author.author_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def select(id):
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    return results[0]

def select_all():
    sql = "SELECT * FROM authors"
    results = run_sql(sql)
    return results

def update(author):
    sql = "UPDATE authors SET author_name = %s WHERE id = %s RETURNING *"
    values = [author.author_name]
    results = run_sql(sql, values)
    return results