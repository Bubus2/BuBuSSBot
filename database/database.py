from sqlite3 import connect
from os.path import isfile

DB_PATH = "./database/database.sqlite3"
BUILD_PATH = "./database/build.sql"

# we don't use connection pool
connection = connect(DB_PATH, check_same_thread=False)
current = connection.cursor()

def with_commit(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        commit()
    return inner

@with_commit
def build():
    if isfile(BUILD_PATH):
        scriptexec(BUILD_PATH)

def commit():
    connection.commit()

def close():
    connection.close()

def field(command, *values):
    cursor.execute(command, tuple(values))
    if (fetch := cursor.fetch_one()) is not None:
        return fetch[0]

def record(command, *values):
    cursor.execute(command, tuple(values))
    return cur.fetch_one()

def records(command, *values):
    cursor.execute(command, tuple(values))
    return cur.fetch_all()

def column(command, *values):
    cursor.execute(command, tuple(values))
    return [item[0] for item in cur.fetch_all()]

def execute(command, *values):
    cursor.execute(command, tuple(values))

def multi_execute(command, *values):
    cursor.execute_many(command, valueset)

def script_execute(path):
    with open(path, "r", encoding="utf-8") as script:
        cursor.execute_script(script.read())