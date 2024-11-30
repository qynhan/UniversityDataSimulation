import pandas as pd
from sqlalchemy import create_engine

# Database connection configuration
DB_USER = 'root'          # MySQL username
DB_PASSWORD = 'password'  # MySQL password
DB_HOST = 'localhost'     # host (default: localhost)
DB_NAME = 'UniversityData'  # database name

# Establish database connection
engine = create_engine(f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

# List of tables and their corresponding CSV files (ordered for parent tables first)
tables_and_files = {
    "DEPARTMENT": "entitiesCsv/departments.csv",
    "STUDENT": "entitiesCsv/students.csv",
    "VENUE": "entitiesCsv/venues.csv",
    "CLUB": "entitiesCsv/clubs.csv",   # CLUB should come after DEPARTMENT and STUDENT
    "EVENT": "entitiesCsv/events.csv",  # EVENT should come after CLUB and VENUE
    "STAFF": "entitiesCsv/staff.csv",
    "EXPENSE": "entitiesCsv/expenses.csv",  # Ensure EVENT exists before EXPENSE
    "SPONSOR": "entitiesCsv/sponsors.csv",
    "RESOURCES": "entitiesCsv/resources.csv",
    "EVENT_RESOURCES": "entitiesCsv/event_resources.csv",  # Ensure EVENT and RESOURCES exist
    "TASK": "entitiesCsv/tasks.csv",
    "REGISTRATION": "entitiesCsv/registrations.csv",  # Ensure EVENT and STUDENT exist
    "MEMBERSHIP": "entitiesCsv/memberships.csv",  # Ensure CLUB and STUDENT exist
    "VOLUNTEER": "entitiesCsv/volunteers.csv",  # Ensure EVENT and STUDENT exist
    "FEEDBACK": "entitiesCsv/feedbacks.csv",  # Ensure EVENT and STUDENT exist
    "APPLICATION": "entitiesCsv/applications.csv",  # Ensure CLUB and STUDENT exist
}

# Insert data into tables
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
