import csv
import random
from faker import Faker

fake = Faker()

# File paths
output_files = {
    "STUDENT": "students.csv",
    "CLUB": "clubs.csv",
    "EVENT": "events.csv",
    "EXPENSE": "expenses.csv",
    "MEMBERSHIP": "memberships.csv",
}

# Generate STUDENT data with realistic variability
def generate_students(num_records=1000):
    with open(output_files["STUDENT"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "FirstName", "LastName", "Email", "PhoneNum"])
        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                fake.first_name(),
                fake.last_name(),
                fake.email(domain="example.edu"),  # Use an academic-style domain
                fake.phone_number()
            ])

# Generate CLUB data with realistic variability
def generate_clubs(num_records=20):
    departments = ["Engineering", "Arts", "Sciences", "Business", "Medicine"]
    with open(output_files["CLUB"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "DepartmentID", "President", "FoundingDate"])
        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                fake.bs().capitalize() + " Club",  # Use business-style names for clubs
                random.randint(1, len(departments)),  # Department ID
                random.randint(1, 1000),  # President is a student ID
                fake.date_this_century(before_today=True, after_today=False)
            ])

# Generate EVENT data with more varied fields
def generate_events(num_records=1000):
    event_types = ["Workshop", "Seminar", "Sports", "Cultural", "Networking"]
    venues = list(range(1, 30))  # Assume 30 venues are available
    with open(output_files["EVENT"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "EventType", "Date", "Description", "ClubID", "VenueID"])
        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                fake.catch_phrase(),
                random.choice(event_types),
                fake.date_between(start_date="-1y", end_date="today"),
                fake.paragraph(nb_sentences=2),
                random.randint(1, 20),  # Club ID (20 clubs)
                random.choice(venues)  # Random venue ID
            ])

# Generate EXPENSE data with variability
def generate_expenses(num_records=2000):
    with open(output_files["EXPENSE"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "SpentAmount", "Description", "EventID"])
        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                round(random.uniform(100, 5000), 2),  # Expense ranges from $100 to $5000
                fake.sentence(nb_words=6),
                random.randint(1, 1000)  # Event ID
            ])

# Generate MEMBERSHIP data, linking students to clubs with realistic membership spread
def generate_memberships(num_records=3000):
    with open(output_files["MEMBERSHIP"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "JoinDate", "ClubID", "StudentID"])
        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                fake.date_between(start_date="-5y", end_date="today"),
                random.randint(1, 20),  # Club ID (20 clubs)
                random.randint(1, 1000)  # Student ID (1000 students)
            ])

# Generate Data for All Tables with More Realism
def generate_all_data():
    print("Generating STUDENT data...")
    generate_students(1000)  # 1000 students
    
    print("Generating CLUB data...")
    generate_clubs(20)  # 20 clubs
    
    print("Generating EVENT data...")
    generate_events(1000)  # 1000 events
    
    print("Generating EXPENSE data...")
    generate_expenses(2000)  # 2000 expenses
    
    print("Generating MEMBERSHIP data...")
    generate_memberships(3000)  # 3000 memberships
    
    print("Data generation completed! Check the CSV files.")

# Run the data generation
if __name__ == "__main__":
    generate_all_data()