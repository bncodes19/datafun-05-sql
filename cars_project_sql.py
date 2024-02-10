"""
Python, SQL, and CSVs: this module establishes a SQLite database, creats a connection, creates two tables named car_brands and car_models.
Data is then inserted into these tables from CSV files.
Insert, Delete, and Update statements are then ran from SQL files on the created tables.
Analysis queries are created to view the data.
Results are stored in 'query_results_pretty.txt'
"""

# Import dependencies
import logging
import sqlite3
import pandas as pd
import pathlib

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Define the database file in the current root project directory
db_file = pathlib.Path("project.db")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        car_brands_data_path = pathlib.Path("data", "car_brands.csv")
        car_models_data_path = pathlib.Path("data", "car_models.csv")
        car_brands_df = pd.read_csv(car_brands_data_path)
        car_models_df = pd.read_csv(car_models_data_path)
        with sqlite3.connect(db_file) as conn:
            car_brands_df.to_sql("car_brands", conn, if_exists="replace", index=False)
            car_models_df.to_sql("car_models", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def execute_sql(db_file, sql_file):
        with sqlite3.connect(db_file) as conn:
            with open(sql_file, 'r') as file:
                sql_stmt = file.read()
                conn.executescript(sql_stmt)
                print (f"SQL file executed: {sql_file}")

def main():
    """ 
    Main program execution to create the database, tables, insert data, and analysis queries. 
    Logging is built in to track the progress of the program (logs are stored in log.txt)
    """
    logging.info("Program started")
    create_database()
    logging.info("Database has been created successfully")
    
    create_tables()
    logging.info("Tables have been created successfully")

    insert_data_from_csv()
    logging.info("Data has been successfully from CSVs")

    execute_sql(db_file, 'sql/insert_records.sql')
    logging.info("Additional records have been inserted")

    execute_sql(db_file, 'sql/delete_records.sql')
    logging.info("Records have been deleted")

    execute_sql(db_file, 'sql/update_records.sql')
    logging.info("Records have been updated")

    execute_sql(db_file, 'sql/query_aggregation.sql')
    execute_sql(db_file, 'sql/query_filter.sql')
    execute_sql(db_file, 'sql/query_join.sql')
    execute_sql(db_file, 'sql/query_sorting.sql')
    execute_sql(db_file, 'sql/query_group_by.sql')

    logging.info("Program ended")

if __name__ == "__main__":
    main()