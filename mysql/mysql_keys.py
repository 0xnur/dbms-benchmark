import mysql.connector as mysql
'''
get mysql keys from db for select and update insert_test
'''
def mysqlKeys():
    db = mysql.connect(
        host = "localhost",
        user = "test",
        passwd = "test",
        database = "hacettepe"
    )
    cursor = db.cursor()
    query = "select id from test"
    cursor.execute(query)
    return [item[0] for item in cursor.fetchall()]
