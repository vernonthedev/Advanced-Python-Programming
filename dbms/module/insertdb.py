import mysql.connector as msconn


#insert the data into table
def insert(host,  username, password, database, table_name):
    try:

      db = msconn.connect(
         host=host,
         user=username,
         password=password,
         database=database
      )
      print("[+] Database Connection Established Successfully.")
      # display to insert data
      coders_id = input("Enter coders id: ")
      fname = input("Enter coders Firstname: ")
      lname = input("Enter coders LastName: ")
      gender = input("Enter coders Gender: ")
      phone_number = input("Enter coders Phone Number: ")
      location = input("Enter coders Location: ")

      #create a cursor
      cursor = db.cursor()
      sql = "INSERT INTO "+ table_name + "(coders_id, fname, lname, gender, phone_number, location) VALUES(%s, %s, %s, %s, %s, %s);"
      print(sql)

      val = (coders_id, fname, lname, gender, phone_number, location)
      cursor.execute(sql, val)
      db.commit()

      #to close the connection obtained from the connection pool
      #close() doesn't actually close the connection bt returns a pool
      #and makes it available for other connections
      db.close()
      print("[+] One record inserted into "+ table_name)

    except:
      #undo all the changes of the current transaction
      db.rollback()
      print('[-] An exception occurred')
