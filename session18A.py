import mysql.connector as db


class DBHelper:

    def __init__(self):
        self.connection = db.connect(user='root', password='Binaypal@1510',
                                     host='127.0.0.1',
                                     database='gw2022pd1')
        print("DB CONNECTED :)")
        self.cursor = self.connection.cursor()
        print("CURSOR CREATED :)")

    def write(self, sql):
        self.cursor.execute(sql)        #1.create connection 2. create cursor   3. execute sql cmd
        self.connection.commit()
        print("SQL QUERY EXECUTED :)")

    def read(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def update_log(self,sql):
        self
