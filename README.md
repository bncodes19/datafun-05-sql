# Python, SQL, and CSVs: 
These are the steps and overview of what this project accomplishes:
- creates a SQLite database
- establishes a connection
- creates two tables named car_brands and car_models (sql/create_tables.sql)
- Inserts data into these two tables from CSV files (data/car_brands.csv and data/car_models.csv)
- Insert, delete, and update statements are then ran from SQL files on the created tables (sql/insert_records.sql, sql/delete_records.sql, sql/update_records.sql)
- Analysis queries are created to view the data
- Results are stored in 'query_results_pretty.txt'

This project utilizes several Python packages. The list of required Python projects can be found in requirements.txt.

To fetch and install these required packages in the project in a virtual environment, run the following commands in the project directory on a terminal:

Create virtual environment
``` shell
python3 -m venv .venv
```

Activate virtual environment
``` shell
source .venv/bin/activate
```

Install required packages
``` shell
python3 -m pip install -r requirements.txt
```

Freeze dependencies
``` shell
python3 -m pip freeze > requirements.txt
```
