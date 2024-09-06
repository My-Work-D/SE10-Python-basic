# #
# # import mysql.connecter
# # Taking user inputs for name, age, and weight
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# weight = float(input("Enter your weight: "))
#
# # Establishing the connection to MySQL
# db = mysql.connector.connect(
#     host="localhost",  # Replace with your database host
#     user="root",       # Replace with your MySQL username
#     password="ijse@2001",  # Replace with your MySQL password
#     database="user_data"       # The name of the database you've created
# )
#
# # Creating a cursor object to execute SQL queries
# cursor = db.cursor()
#
# # Defining the SQL query to insert data
# insert_query = "INSERT INTO users (name, age, weight) VALUES (%s, %s, %s)"
# data = (name, age, weight)
#
# # Executing the query and committing the transaction
# cursor.execute(insert_query, data)
# db.commit()
#
# # Closing the cursor and connection
# cursor.close()
# db.close()
#
# print("Data has been saved successfully!")

import mysql.connector

# Now you can use mysql.connector to connect to your MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ijse@2001",
    database="user_data"
)

# Do your database operations here

