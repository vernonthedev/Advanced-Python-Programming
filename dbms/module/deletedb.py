import mysql.connector as msconn

#function to delete the data
def delete(host, username, password, database, table_name):
    print("\n")

    #make a database connection
    db = msconn.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )

    #return a cursor obj
    cursor = db.cursor()
    sql_delete_query = "DELETE FROM "+ table_name + " WHERE coders_id = %s;"
    print(sql_delete_query)
    Id = int(input("Enter coders id: "))
    #execute the database operation
    cursor.execute(sql_delete_query, (Id,))
    db.commit()
    print("[+] One row deleted from "+ table_name)


