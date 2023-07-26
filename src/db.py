import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect(':memory:')
        print(f'Successfully Connected with SQLite Version {sqlite3.version}')
        return conn
    except sqlite3.Error as e:
        print(f'Error occurred: {e}')
        return None

def select_all_tasks(conn):
    if conn is None:
        print('No connection to the database.')
        return

    try:
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM tasks")
            rows = cur.fetchall()
    except sqlite3.Error as e:
        print(f'Error occurred: {e}')
        return

    for row in rows:
        print(row)

if __name__ == '__main__':
    conn = create_connection()
    select_all_tasks(conn)
    if conn is not None:
        conn.close()
