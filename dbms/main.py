from mysql.connector import Error, cursor, connect
#import my created module
from module import insertdb as insert, updatedb as update, displaydb as display, deletedb as delete
import cowsay

def create_db(username, password):
    '''Function to Create a new Database'''
    try:
      with connect(host=gblhost,user=username,password=password) as connection:
         dbname = input("What database Would you like to create?:  ")
         create_db_query =  "CREATE DATABASE "+ dbname
         with connection.cursor() as cursor:
            cursor.execute(create_db_query)
         print(f"[+] Database {dbname} has been created.")

    except Error as e:
      print('[-] Opps Something wrong happened ', e)

    except NameError:
       print("[+] NameError is raised when the identifier being accessed is not defined in the local or global scope.")



def drop_db(username, password):
   '''Function to Drop the Created Database'''
   try:
     with connect(host=gblhost, user=username, password=password) as connection:
        dbname = input("What Database would you like to drop: ")
        drop_db_query = "DROP DATABASE "+ dbname
        with connection.cursor() as cursor:
           cursor.execute(drop_db_query)

        print(f"[+] Database {dbname} has been dropped")

   except Error as e:
     print(f"[-] Opps An Error Occured {format(e)}")


def create_table(username, password):
   '''Function to Create a Table in the specified database'''
   dbname = input("Enter a Database Name first: ")
   try:
     with connect(host=gblhost, user=username, password=password, database=dbname) as connection:
        table_name = input("Enter Table name you want to create: ")
        create_table_query = "CREATE TABLE "+ table_name+ " (coders_id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(50), lname VARCHAR(50), gender VARCHAR(20), phone_number VARCHAR(12), location VARCHAR(30))"
        print(create_table_query)
        with connection.cursor() as cursor:
           cursor.execute(create_table_query)
           for x in cursor:
              print(x)
   except Error as e:
     print(f"[-] Opps An Error Occured {format(e)}")


def drop_table(username, password):
   dbname = input("From which database would you like to delete a table?: ")
   try:
     with connect(host=gblhost, user=username, password=password, database=dbname) as connection:
        dbtable=input("What table would you like to drop?: ")
        drop_table_query = "DROP TABLE "+ dbtable
        print(drop_table_query)
        with connection.cursor() as cursor:
           cursor.execute(drop_table_query)
           print(f"Table, {dbtable} has been dropped.")
   except Error as e:
     print(f"[-] ERROR! {format(e)}")


def show_databases(username, password):
   '''Function to show the available databases on the server'''
   try:
     with connect(host=gblhost, user=username, password=password) as connection:
        cursor = connection.cursor()
        databases = "SHOW DATABASES"
        cursor.execute(databases)
        i = 0
        for databases in cursor:
           i = i + 1
           print(f"Database {i} is: {databases[0]}")

   except Error as e:
     print(f"[-] ERROR! {format(e)}")
   except NameError:
      print("NameError is raised when the identifier being accessed is not defined in the local or global scope.")



#MAIN PROGRAM DISPLAYS
cowsay.ghostbusters("WELCOME TO CODEZILLA DATABASE MANAGEMENT SYSTEM")
print("Developed by vernonthedev")
print("1. CREATE DATABASE \n2. DROP DATABASE \n3. CREATE TABLE \n4. DROP TABLE \n5. INSERT \n6. UPDATE \n7. DELETE \n8. DISPLAY \n9. SHOW DATABASE \n10. EXIT\n")


while True:
   choice = input("Please Enter A Choice: ")
   if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
      #exit if someone types in 10 straight away
      if choice == '10':
         exit()

      #gblhost is global local host variable
      gblhost = 'localhost'
      u = input("Enter MySQL Username: ")
      p = input("Enter MySQL Password: ")
      i = 0

      #like a switch statement
      if choice == '1':
         #create the db
         create_db(u,p)
      elif choice == '2':
         #drop the database
         drop_db(u,p)
      elif choice == '3':
         #create a table
         create_table(u,p)
      elif choice == '4':
         #drop table
         drop_table(u,p)
      elif choice == '5':
         #insert into table
         dbname = input("Enter Database Name: ")
         table_name = input("Enter Table Name: ")
         insert.insert(gblhost, u,p,dbname,table_name)
      elif choice == '6':
         #update table
         dbname = input("Enter Database Name: ")
         table_name = input("Enter Table Name: ")
         update.update(gblhost, u, p, dbname, table_name)
      elif choice == '7':
         #delete table
         dbname = input("Enter Database Name: ")
         table_name = input("Enter Table Name: ")
         delete.delete(gblhost, u, p, dbname, table_name)
      elif choice == '8':
         #display tables
         dbname = input("Enter Database Name: ")
         table_name = input("Enter Table Name: ")
         display.displayTableInformation(gblhost, u, p, dbname, table_name)
      elif choice == '9':
         #display the databases
         show_databases(u,p)

   else:
         print("[-] Invalid Input!")






