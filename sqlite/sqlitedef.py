import sqlite3

class BookDB():
    def __init__(self):
        pass

    def __del__(self):
        pass

    def create_connection(self):
        conn = sqlite3.connect('sqlite/my_books.db')
        return conn

    # crreate table 
    def create_table(self):
        conn = self.create_connection()
        c = conn.cursor()
        sql = """ 
            create table if not exists books(
                title text,
                published_date text,
                publisher text,
                pages integer,
                recommend integer
            )"""
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()

    def insert_book(self, item):
        conn = self.create_connection()
        c = conn.cursor()
        sql = "INSERT INTO books VALUES(?,?,?,?,?)"
        c.execute(sql, item)
        conn.commit()
        c.close()
        conn.close()

    def insert_books(self, items):
        conn = self.create_connection()
        c = conn.cursor()
        sql = "INSERT INTO books VALUES(?,?,?,?,?)"
        c.executemany(sql, items)
        conn.commit()
        c.close()
        conn.close()

    def all_books(self):
        conn = self.create_connection()
        c = conn.cursor()
        sql = "SELECT * FROM books"
        c.execute(sql)
        books = c.fetchall()
        conn.commit()
        c.close()
        conn.close()
        return books

    def one_book(self, title):
        conn = self.create_connection()
        c = conn.cursor()
        sql = "SELECT * FROM books WHERE title = ?"
        c.execute(sql, (title,))
        book = c.fetchone()
        conn.commit()
        c.close()
        conn.close()
        return book

    def one_book_like(self, title):
        conn = self.create_connection()
        c = conn.cursor()
        sql = "SELECT * FROM books WHERE title LIKE ?"
        title = "%" + title + "%"
        c.execute(sql, (title,))
        book = c.fetchone()
        conn.commit()
        c.close()
        conn.close()
        return book
        
    def delete_books(self):
        conn = self.create_connection()
        c = conn.cursor()
        sql = "DELETE FROM books"
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()


if __name__ == '__main__':
    book = BookDB()
    book.create_table()
    book.delete_books()
    item = ('데이터분석실무', '2020-07-13', '위키북스', 300, 10)
    book.insert_book(item)
    items = [
        ('빅데이터', '2020-07-13', 'IT월드', 200, 5),
        ('데이터분석', '2020-07-15', '이지스퍼블리싱', 350, 12),
        ('머신러닝', '2020-07-01', '한빛미디어', 400, 20),
    ]
    book.insert_books(items)
    for row in book.all_books():
        print(row)
    print()
    print(book.one_book('빅데이터'))
    print()
    print(book.one_book_like('데이터'))