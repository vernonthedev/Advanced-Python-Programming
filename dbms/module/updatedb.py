import mysql.connector as msconn

def update(host, username, password, database, table_name):
    try:
      db = msconn.connect(
         host=host,
         user=username,
         password=password,
         database=database
      )

      coders_id = input("Enter coders id: ")
      fname = input("Enter coders Firstname: ")
      lname = input("Enter coders LastName: ")
      gender = input("Enter coders Gender: ")
      phone_number = input("Enter coders Phone Number: ")
      location = input("Enter coders Location: ")

      cursor = db.cursor()

      try:
        #update the first name
        sqlFormula = "UPDATE "+ table_name+ "SET fname = %s WHERE id = %s"
        cursor.execute(sqlFormula,(fname, coders_id))

        #update the second name
        sqlFormula = "UPDATE "+ table_name+ "SET lname = %s WHERE id = %s"
        cursor.execute(sqlFormula,(lname, coders_id))

        #update the gender
        sqlFormula = "UPDATE "+ table_name+ "SET gender = %s WHERE id = %s"
        cursor.execute(sqlFormula,(gender, coders_id))

        #update phone number
        sqlFormula = "UPDATE "+ table_name+ "SET phone_number = %s WHERE id = %s"
        cursor.execute(sqlFormula,(phone_number, coders_id))

        #update the location
        sqlFormula = "UPDATE "+ table_name+ "SET location = %s WHERE id = %s"
        cursor.execute(sqlFormula,(location, coders_id))


        db.commit()
        print("[+] Entries updated in "+ table_name)
      except:
        db.rollback()
        print("[-] ERROR Executing SQL Statements")

    except:
      print('[-] ERROR! Database Not connected')
