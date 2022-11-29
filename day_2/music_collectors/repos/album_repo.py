from db.run_sql import run_sql


def create(album):
    sql = "INSERT INTO albums (title, release_year, genre, artist_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [album.title, album.release_year, album.genre, album.artist_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select(id):
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    return results[0]

def select_all():
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    return results

def update(album):
    sql = "UPDATE albums SET (title, release_year, genre, artist_id) = (%s, %s, %s, %s) WHERE id = %s RETURNING *"
    values = [album.title, album.release_year, album.genre, album.artist_id]
    results = run_sql(sql, values)
    return results

def get_album_by_artist(artist_id):
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist_id]
    results = run_sql(sql, values)
    return results