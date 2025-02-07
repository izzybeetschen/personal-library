# import mysql.connector

# # Connect to the MySQL database
# conn = mysql.connector.connect(
#     host="localhost",       # Database host
#     user="izzy",            # Your MySQL username
#     password="",  # Your MySQL password
#     database="book_collection_db"  # The database you're using
# )

# cursor = conn.cursor()

# cursor.execute("SELECT * FROM books")
# books = cursor.fetchall()

# for book in books:
#     print(book)

# cursor.close()
# conn.close()
