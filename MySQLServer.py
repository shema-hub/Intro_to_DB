import pymysql

def create_database():
    try:
        # Connect to MySQL server
        connection = pymysql.connect(
            host='localhost',  # Change if your MySQL server is hosted elsewhere
            user='root',  # Replace with your MySQL username
            password='Kamiz@500'  # Replace with your MySQL password
        )
        
        cursor = connection.cursor()
        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    
    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
