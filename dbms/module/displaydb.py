import mysql.connector as msconn

def displayTableInformation(host, username, password, database, table_name):
    #connect to the database
    db = msconn.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )

    cursor = db.cursor()

    #check whether the connection was successful
    if db.is_connected():
        allcolumns = "SELECT * FROM "+ table_name+ ";"
        cursor.execute(allcolumns)
        #row will print each column for each row of data
        print("[++++++++++++++++ TABLE CONTENTS ++++++++++++++++]")
        for row in cursor:
            print("\nCoders ID: ", row[0])
            print("Coders First Name: ", row[1])
            print("Coders Last name: ", row[2])
            print("Coders Gender: ", row[3])
            print("Coders Phone Number: ", row[4])
            print("Coders Location: ", row[5])

