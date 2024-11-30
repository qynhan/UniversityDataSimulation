import csv
import random
from faker import Faker
from datetime import timedelta

fake = Faker()

# File paths for all tables
output_files = {
    "STUDENT": "students.csv",
    "CLUB": "clubs.csv",
    "EVENT": "events.csv",
    "EXPENSE": "expenses.csv",
    "EVENT_RESOURCES": "event_resources.csv",
    "MEMBERSHIP": "memberships.csv",
    "DEPARTMENT": "departments.csv",
    "VENUE": "venues.csv",
    "STAFF": "staff.csv",
    "TASK": "tasks.csv",
    "RESOURCES": "resources.csv",
    "REGISTRATION": "registrations.csv",
    "VOLUNTEER": "volunteers.csv",
    "FEEDBACK": "feedback.csv",
    "APPLICATION": "applications.csv",
    "SPONSOR": "sponsors.csv"
}

# Generate EVENT_RESOURCES data linking events to resources with quantity
def generate_event_resources(num_records=2000):
    with open(output_files["EVENT_RESOURCES"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "EventID", "ResourceID", "Quantity"])
        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                random.randint(1, 1000),  # Event ID (1000 events)
                random.randint(1, 100),   # Resource ID (100 resources)
                random.randint(1, 10)     # Random quantity (1-10)
            ])


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

# Previous methods (students, clubs, events, expenses, memberships) remain the same

def generate_departments(num_records=5):
    department_names = ["Engineering", "Arts", "Sciences", "Business", "Medicine"]
    with open(output_files["DEPARTMENT"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name"])
        for i in range(1, num_records + 1):
            writer.writerow([i, department_names[i-1]])

def generate_venues(num_records=30):
    with open(output_files["VENUE"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Location", "Capacity", "Availability"])
        for i in range(1, num_records + 1):
            building_name = f"{fake.company()} {fake.building_number()} {fake.street_name()}"
            writer.writerow([
                i,
                building_name,
                fake.address(),
                random.randint(50, 500),
                random.choice([True, False])
            ])

def generate_staff(num_records=50):
    roles = ["Advisor", "Coordinator", "Manager", "Director", "Assistant"]
    with open(output_files["STAFF"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "FirstName", "Role"])
        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                fake.first_name(),
                random.choice(roles)
            ])

def generate_tasks(num_records=200):
    statuses = ["Pending", "In Progress", "Completed", "On Hold"]
    with open(output_files["TASK"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Description", "Deadline", "Status"])
        for i in range(1, num_records + 1):
            deadline = fake.date_between(start_date='now', end_date='+1y')
            writer.writerow([
                i,
                fake.sentence(nb_words=6),
                deadline,
                random.choice(statuses)
            ])

def generate_resources(num_records=100):
    resource_types = ["Equipment", "Technology", "Consumables", "Space", "Funding"]
    with open(output_files["RESOURCES"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Type", "Quantity"])
        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                fake.word().capitalize() + " " + fake.word().capitalize(),
                random.choice(resource_types),
                random.randint(1, 100)
            ])

def generate_registrations(num_records=5000):
    with open(output_files["REGISTRATION"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Timestamp", "Attendance", "EventID", "StudentID"])
        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                fake.date_time_this_year(),
                random.choice([True, False]),
                random.randint(1, 1000),  # Assuming 1000 events
                random.randint(1, 1000)   # Assuming 1000 students
            ])

def generate_volunteers(num_records=1000):
    volunteer_roles = ["Event Staff", "Setup", "Cleanup", "Technical Support", "Registration"]
    with open(output_files["VOLUNTEER"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Role", "Hours", "EventID", "StudentID"])
        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                random.choice(volunteer_roles),
                random.randint(1, 10),
                random.randint(1, 1000),  # Assuming 1000 events
                random.randint(1, 1000)   # Assuming 1000 students
            ])

def generate_feedback(num_records=2000):
    with open(output_files["FEEDBACK"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Rating", "Comments", "DateSubmitted", "EventID", "StudentID"])
        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                random.randint(1, 5),
                fake.paragraph(nb_sentences=2),
                fake.date_between(start_date='-1y', end_date='today'),
                random.randint(1, 1000),  # Assuming 1000 events
                random.randint(1, 1000)   # Assuming 1000 students
            ])

def generate_applications(num_records=500):
    positions = ["President", "Vice President", "Treasurer", "Secretary", "Event Coordinator"]
    statuses = ["Pending", "Approved", "Rejected"]
    with open(output_files["APPLICATION"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Position", "Date", "Status", "ClubID", "StudentID"])
        for i in range(1, num_records + 1):
            writer.writerow([
                i,
                random.choice(positions),
                fake.date_between(start_date='-1y', end_date='today'),
                random.choice(statuses),
                random.randint(1, 20),  # Assuming 20 clubs
                random.randint(1, 1000)  # Assuming 1000 students
            ])

def generate_sponsors(num_records=50):
    contribution_types = ["Monetary", "Equipment", "Venue", "Catering", "Scholarship"]
    with open(output_files["SPONSOR"], mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "PhoneNum", "ContributionType", "Amount"])
        for i in range(1, num_records + 1):
            contribution_type = random.choice(contribution_types)
            writer.writerow([
                i,
                fake.company(),
                fake.phone_number(),
                contribution_type,
                round(random.uniform(100, 50000), 2) if contribution_type == "Monetary" else 0
            ])

# Generate Data for All Tables
def generate_all_data():
    print("Generating all data...")
    
    # Existing methods
    generate_students(1000)
    generate_clubs(20)
    generate_events(1000)
    generate_expenses(2000)
    generate_memberships(3000)
    
    # New methods for additional tables
    generate_departments()
    generate_venues()
    generate_staff()
    generate_tasks()
    generate_resources()
    generate_registrations()
    generate_volunteers()
    generate_feedback()
    generate_applications()
    generate_sponsors()
    generate_event_resources()
    
    print("Data generation completed! Check the CSV files.")

# Run the data generation
if __name__ == "__main__":
    generate_all_data()