import sqlite3

def Connect(db):
    try:
        conn = sqlite3.connect(db)
        conn.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, cpf TEXT, date TEXT,  city TEXT, cep TEXT, email TEXT, password TEXT)')
        
        return conn
    except Exception as err:
        print(err)
        exit(1)

def LoginCycle(cpf, email, password, cnn):
    cur = cnn.cursor()
    query = f"SELECT cpf, email, password FROM users WHERE cpf='{cpf}' AND email='{email}' AND password='{password}';"
    cur.execute(query)

    if not cur.fetchone():
        return False
    else:
        return True

def RegisterLogin(name, cpf, date, city, cep, email, password, cnn):
    if LoginCycle(cpf, email, password, cnn):
        return False
    
    cur = cnn.cursor()
    try:
        query = f"INSERT INTO users (name, cpf, date, city, cep, email, password) VALUES ('{name}', {cpf}, {date}, '{city}', {cep}, '{email}', '{password}');"
        cur.execute(query)
        cnn.commit()
        return True
    except Exception as err:
        print(err)
        return False
