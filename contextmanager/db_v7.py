from sqlite3 import connect


class contextmanager:
    def __init__(self, gen):
        self.gen = gen

    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self

    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)

    def __exit__(self, exc_type, exc_val, exc_tb):
        next(self.gen_inst, None)


def temptable(cur):
    cur.execute('create table points(x int, y int)')
    try:
        yield
    finally:
        cur.execute('drop table points')


temptable = contextmanager(temptable)

with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points(x,y) values(1,1)')
        cur.execute('insert into points(x,y) values(1,2)')
        cur.execute('insert into points(x,y) values(2,1)')
        cur.execute('insert into points(x,y) values(2,2)')
        for row in cur.execute('select * from points'):
            print(row)

# Can the __exit__ be called before __enter__
