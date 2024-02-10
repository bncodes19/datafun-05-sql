## datafun-05-sql

Python, SQL, and CSVs: 
This project establishes a SQLite database, creats a connection, creates two tables named car_brands and car_models.
Data is then inserted into these tables from CSV files.
Insert, Delete, and Update statements are then ran from SQL files on the created tables.
Analysis queries are created to view the data.
Results are stored in 'query_results_pretty.txt'

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