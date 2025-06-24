from flask import Flask, render_template, request
import mysql.connector as sql_connect 

app = Flask(__name__, template_folder="template")

def create_table():
    # Connect to the MySQL database
    try:
        mydb = sql_connect.connect(user='root', password='Root@12345678', host='127.0.0.1', database='student')
        print("✅ Connected!")
        cursor = mydb.cursor()

        # SQL query to create table
        cursor.execute("CREATE DATABASE IF NOT EXISTS student")
        cursor.execute("USE student")
        cursor.execute("""CREATE TABLE IF NOT EXISTS Stud (First_Name VARCHAR(20), Last_Name VARCHAR(20), Student_No INT)""")

        mydb.commit()
        cursor.close()
        mydb.close()
    except sql_connect.Error as err:
        print("MySQL Error:", err)


@app.route("/")
def home():
    #create_table()  # Ensures the table is created before rendering the page
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)