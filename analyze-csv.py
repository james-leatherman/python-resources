import pandas as pd
import sqlite3
import dis
# import psycopg2

def create_csv(file_path):
# create a dictionary
    data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

# create a dataframe from the dictionary
    df = pd.DataFrame(data)

# write dataframe to csv file
    try:
        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"An error occurred writing file: {e}")
        return

def analyze_csv(file_path):
    # Load the CSV file
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except Exception as e:
        print(f"An error occurred while reading the CSV: {e}")
        return

    # Display first few rows
    print("First 5 rows:")
    print(df.head())

    # Basic info
    print("\nDataFrame Info:")
    print(df.info())

    # Summary statistics
    print("\nSummary Statistics:")
    print(df.describe(include='all'))

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Optional: Group by a column and show mean (uncomment to use)
    # if 'your_column_name' in df.columns:
    #     print("\nGrouped Data (mean by 'your_column_name'):")
    #     print(df.groupby('your_column_name').mean())

def write_csv_to_sqlite(file_path):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Create a table (if it doesn't already exist)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS people (
            Name TEXT,
            Age INTEGER,
            City TEXT
        )
    ''')

    # Load the CSV file into a DataFrame
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError as e:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the CSV: {e}")
        conn.close()
        return

    # Write the DataFrame to the database
    try:
        df.to_sql('people', conn, if_exists='append', index=False)
        print("Data successfully written to the database.")
    except Exception as e:
        print(f"An error occurred while writing to the database: {e}")
    finally:
        conn.close()

def read_from_sqlite(file_path):
    # Connect to SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Query the database
    try:
        cursor.execute('SELECT * FROM people')
        rows = cursor.fetchall()
        print("Data from the database:")
        for row in rows:
            print(row)
    except Exception as e:
        print(f"An error occurred while reading from the database: {e}")
    finally:
        conn.close()
            
# def write_to_postgres(file_path):

#         CREATE TABLE IF NOT EXISTS people (
#             Name TEXT,
#             Age INTEGER,
#             City TEXT
#         )
    
    
# Example usage
if __name__ == "__main__":
    file_path = input("Please enter the path to the CSV file: ")
    create_csv(file_path)
    analyze_csv(file_path)
    # write_csv_to_sqlite(file_path)
    # read_from_sqlite(file_path)
    # write_to_postgres(file_path)
    
    dis.dis(create_csv)
