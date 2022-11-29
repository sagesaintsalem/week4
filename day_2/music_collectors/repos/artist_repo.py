from db.run_sql import run_sql


def create(artist):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    return results[0]

def select_all():
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    return results

def update(artist):
    sql = "UPDATE artists SET artist_name = %s WHERE id = %s RETURNING *"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    return results