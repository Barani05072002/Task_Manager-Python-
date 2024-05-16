from mysql.connector import connect

def connect_database():
    try:
        mydb = connect(
            host = "localhost",
            user = "root",
            password = "root123",
            database = "pyTask"
        )
        print('Connected to the Server...')
        return mydb
    except:
        print('Connection Error :( ...')
        return None

def create_table(mydb):
    try:
        querry = "CREATE TABLE task(id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(25) NOT NULL,\
        description VARCHAR(100),priority ENUM('high','normal','low'),\
        status ENUM('completed','in-process','pending'))"
        mydb.cursor().execute(querry)
        print('Table task created successfully...')
        return True
    
    except:
        print('Table is already existed...')
        return False
    
