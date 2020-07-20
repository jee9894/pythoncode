import pymysql

class BookDB:
    def create_connection(self):
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='qwer1234',
                               db='test',
                               charset='utf8mb4',
                               #cursorclass = pymysql.cursors.DictCursor
                               )
        return conn
        
    def drop_table(self):
        conn = self.create_connection()
        c = conn.cursor()
        sql = '''DROP TABLE IF EXISTS books'''
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()

    def create_table(self):
        conn = self.create_connection()
        c = conn.cursor()
        sql = '''
            CREATE TABLE IF NOT EXISTS books (
                book_id integer NOT NULL AUTO_INCREMENT PRIMARY KEY,
                title text,
                published_date text,
                publisher text,
                pages integer,
                recommend integer
            )DEFAULT CHARSET=utf8mb4'''
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()

    def insert_book(self, item):
        conn = self.create_connection()
        c = conn.cursor()
        sql = """INSERT INTO books (title,published_date,publisher,pages,recommend)
                 VALUES(%s,%s,%s,%s,%s)"""
        c.execute(sql, item)
        conn.commit()
        c.close()
        conn.close()

    def insert_books(self, items):
        conn = self.create_connection()
        c = conn.cursor()
        sql = """INSERT INTO books (title,published_date,publisher,pages,recommend)
                 VALUES(%s,%s,%s,%s,%s)"""
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
        sql = "SELECT * FROM books WHERE title = %s"
        c.execute(sql, (title,))
        book = c.fetchone()
        conn.commit()
        c.close()
        conn.close()
        return book

    def one_book_id(self, book_id):
        conn = self.create_connection()
        c = conn.cursor()
        sql = "SELECT * FROM books WHERE title = %s"
        c.execute(sql, (book_id,))
        book = c.fetchone()
        conn.commit()
        c.close()
        conn.close()
        return book

    def books_like(self, title):
        conn = self.create_connection()
        c = conn.cursor()
        sql = "SELECT * FROM books WHERE title LIKE %s"
        title = "%" + title + "%"
        c.execute(sql, (title,))
        book = c.fetchall()
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

    def delete_book(self, book_id):
        conn = self.create_connection()
        c = conn.cursor()
        sql = "DELETE FROM books WHERE book_id = %s"
        c.execute(sql, book_id)
        conn.commit()
        c.close()
        conn.close()
    
    def update_titles(self, title, book_id):
        conn = self.create_connection()
        c = conn.cursor()
        sql = "UPDATE books SET title = %s WHERE book_id = %s"
        c.execute(sql, (title,book_id))
        conn.commit()
        c.close()
        conn.close()

if __name__ == '__main__':
    book = BookDB()
    book.drop_table()
    book.create_table()
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
    # print()
    # print(book.one_book('빅데이터'))
    # print()
    # print(book.books_like('빅'))
    book.update_titles('스몰데이터',2)
    for row in book.all_books():
        print(row)
