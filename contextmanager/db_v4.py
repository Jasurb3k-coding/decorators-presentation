from sqlite3 import connect


def temptable(cur):
    cur.execute('create table points(x int, y int)')
    yield
    cur.execute('drop table points')


class contextmanager:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        self.gen = temptable(self.cur)
        next(self.gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        next(self.gen, None)


with connect('test.db') as conn:
    cur = conn.cursor()
    with contextmanager(cur):
        cur.execute('insert into points(x,y) values(1,1)')
        cur.execute('insert into points(x,y) values(1,2)')
        cur.execute('insert into points(x,y) values(2,1)')
        cur.execute('insert into points(x,y) values(2,2)')
        for row in cur.execute('select * from points'):
            print(row)

# Can the __exit__ be called before __enter__
