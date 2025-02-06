import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",       # Database host
    user="izzy",            # Your MySQL username
    password="",  # Your MySQL password
    database="book_collection_db"  # The database you're using
)

cursor = conn.cursor()

# Example: Fetch all books from the books table
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

# Print out the results (books)
for book in books:
    print(book)

# Close the connection
cursor.close()
conn.close()
