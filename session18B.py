import datetime

class HealthLogger:

    def __init__(self, phone=None, weight=None, bp_high=None, bp_low=None, sugar=None):
        self.phone = phone
        self.weight = weight
        self.bp_high = bp_high
        self.bp_low = bp_low
        self.sugar =sugar
        dt = str(datetime.datetime.today())
        idx = dt.rindex(".")
        self.log_time_stamp = dt[0: idx]


    def insert_sql_command(self):
        sql = "insert into HealthLogger values(null, '{phone}', " \
              "{weight}, {bp_high}, {bp_low}, {sugar}, " \
              "'{log_time_stamp}')".format_map(vars(self))
        return sql

    def fetch_sql_command(self):
        return "select * from HealthLogger"

"""
    def update_log(self):
        self.id = int(input("Enter Log Id:"))
        self.phone = input("Enter Phone:")
        self.weight = int(input("Enter weight:"))
        self.bp_high = int(input("Enter Bp High:"))
        self.bp_low =int( input("Enter bp low:"))
        self.sugar = int(input("Enter sugar:"))
        dt = str(datetime.datetime.today())
        idx = dt.rindex(".")
        self.log_time_stamp = dt[0: idx]

        sql = "update into HealthLogger set phone='{phone}',weight={weight}, bp_high={bp_high}, bp_low={bp_low},sugar= {sugar}, log_time_stamp= '{log_time_stamp}'where id={id}".format_map(vars(self))
        return sql


    def delete_log(self):
        self.id=int(input("Enter Log Id:"))

        sql="delete from HealthLogger where id = {id}".format_map(vars(self))

"""