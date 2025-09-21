import psycopg2
def table():
    connect = psycopg2.connect(dbname="postgres", user="postgres",password="x",host="localhost",port="5432")
    cursor=connect.cursor()
    cursor.execute("""CREATE TABLE employees(Name text, ID int, Age int);""")
    print("Table created successfully")
    connect.commit()
    connect.close()

def data():
    connect = psycopg2.connect(dbname="postgres", user="postgres",password="x,host="localhost",port="5432")
    cursor=connect.cursor()
    name=input("Enter name: ")
    ID=int(input("Enter ID: "))
    age=int(input("Enter Age: "))
    query="""INSERT INTO employees (Name, ID, Age) VALUES (%s, %s, %s);"""
    cursor.execute(query, (name, ID, age))
    print("Data inserted successfully")
    connect.commit()
    connect.close()
def extract():
    connect = psycopg2.connect(dbname="postgres", user="postgres",password="x",host="localhost",port="5432")
    cursor=connect.cursor()
    cursor.execute("""Select * from employees;""")
    print(cursor.fetchall())
    print("Data extracted successfully")
    connect.commit()
    connect.close()
extract()