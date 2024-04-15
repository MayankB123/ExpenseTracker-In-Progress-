from user import User
import sqlite3

con = sqlite3.connect("et_database.db")

cursor = con.cursor()

# for i in cursor.execute("SELECT * from income_table"):
#     print(i)

# cursor.execute("create table user_data (Email varchar(50), Password varchar(50), First_Name varchar(50), Last_Name varchar(50))")

# cursor.execute("DELETE FROM income_table WHERE iName = 'f'")
# con.commit()

# for i in cursor.execute("SELECT * from user_data"):
#     print(i)

# cursor.execute("""
# INSERT INTO user_data VALUES
#     ('john@gmail.com', '12345678', 'John', 'Smith')
# """)
# con.commit()

def add_income(user, name, date, category, amount):
    email = user.get_email()
    # print(email, name, date, category, amount)
    amount = float(amount)
    cursor.execute(f"insert into income_table values('{email}', '{name}', '{date}', '{category}', {amount})")

    con.commit()

def add_expense(user, name, date, category, amount):
    email = user.get_email()
    # print(email, name, date, category, amount)
    amount = float(amount)
    cursor.execute(f"insert into expense_table values('{email}', '{name}', '{date}', '{category}', {amount})")

    con.commit()

def get_income(user):
    email = user.get_email()
    return cursor.execute(f"select * from income_table where Email = '{email}'")



def login(email, password):
    result = cursor.execute("select * from user_data")
    for item in result:
        if email == item[0]:
            if password == item[1]:
                user = User(item)
                return user
            else:
                pass
        else:
            pass

    return False



def register(first_name, last_name, email, password):
    cursor.execute(f"""
    INSERT INTO user_data VALUES
        ('{email}', '{password}', '{first_name}', '{last_name}')
    """)

    con.commit()

    return True































# def login(email, password):
#     cursor.execute("select * from user_data")
#
#     for item in cursor:
#         if email == item[0]:
#             if password == item[1]:
#                 user = User(item)
#                 return user
#             else:
#                 pass
#         else:
#             pass
#
#     return False
#
# def register(first_name, last_name, email, password):
#     SQL = "insert into user_data value(%s, %s, %s, %s)"
#     values = (email, password, first_name, last_name)
#     cursor.execute(SQL, values)
#
#     my_db.commit()
#
#     return True
#
# def add_expense(user, name, date, category, amount):
#     cursor.execute("select * from income_table")
#     # email = user.get_email()
#     # print(email, name, date, category, amount)
#     # amount = int(amount)
#     # SQL = "insert into income_table value(%s, %s, %s, %s, %s)"
#     # values = (str(email), str(name), str(date), str(category), amount)
#     # cursor.execute(SQL, values)
#     #
#     # my_db.commit()
#
#     return True










# import mysql.connector
# from user import User
# from datetime import date
#
# my_db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="12345678",
#     database="database2"
# )
#
# cursor = my_db.cursor()
#
#
#
#