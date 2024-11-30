import pandas as pd
from sqlalchemy import create_engine

# Database connection configuration
DB_USER = 'root'          # Replace with your MySQL username
DB_PASSWORD = 'password'  # Replace with your MySQL password
DB_HOST = 'localhost'          # Replace with your host (default: localhost)
DB_NAME = 'UniversityDatabase'      # Replace with your database name

# Establish database connection
engine = create_engine(f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

# List of tables and their corresponding CSV files
tables_and_files = {
    "DEPARTMENT": "departments.csv",
    "STUDENT": "students.csv",
    "VENUE": "venues.csv",
    "CLUB": "clubs.csv",
    "EVENT": "events.csv",
    "STAFF": "staff.csv",
    "EXPENSE": "expenses.csv",
    "SPONSOR": "sponsors.csv",
    "RESOURCES": "resources.csv",
    "EVENT_RESOURCES": "event_resources.csv",
    "TASK": "tasks.csv",
    "REGISTRATION": "registrations.csv",
    "MEMBERSHIP": "memberships.csv",
    "VOLUNTEER": "volunteers.csv",
    "FEEDBACK": "feedbacks.csv",
    "APPLICATION": "applications.csv",
}

# Load each CSV file into its corresponding table
for table, file in tables_and_files.items():
    try:
        # Load CSV into DataFrame
        df = pd.read_csv(file)
        
        # Write to MySQL table
        df.to_sql(table, con=engine, if_exists='append', index=False)
        print(f"Successfully loaded data into {table} from {file}")
    except Exception as e:
        print(f"Error loading data into {table} from {file}: {e}")

print("Data loading complete.")
