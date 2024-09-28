import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("student.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create the table
table_info = """
Create table STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25)
);
"""
cursor.execute(table_info)

# Insert records
cursor.execute("Insert Into STUDENT Values('ABHI', 'Data Science', 'A')")
cursor.execute("Insert Into STUDENT Values('ABHISHEK', 'ML', 'B')")
cursor.execute("Insert Into STUDENT Values('JOY', 'DevOps', 'C')")
cursor.execute("Insert Into STUDENT Values('YASH', 'Php', 'D')")
cursor.execute("Insert Into STUDENT Values('ARYA', 'DS', 'E')")  # Fixed the syntax error

# Commit the changes
connection.commit()

# Display all the records
print("The inserted records are:")
data = cursor.execute("Select * from STUDENT")
for row in data:
    print(row)

# Close the connection
connection.close()
