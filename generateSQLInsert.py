import random
from faker import Faker

fake = Faker()

# Output file for all tables
output_file = "all_data.sql"

# Helper function to generate SQL insert statements and append them to a single file
def write_to_sql(file_path, table_name, data):
    with open(file_path, mode='a') as file:  # Open in append mode
        for row in data:
            sql = f"INSERT INTO {table_name} ({', '.join(row.keys())}) VALUES ({', '.join(map(str, row.values()))});\n"
            file.write(sql)

# Generate EVENT_RESOURCES data linking events to resources with quantity
def generate_event_resources(num_records=200):
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "EventID": random.randint(1, 1000),
            "ResourceID": random.randint(1, 100),
            "Quantity": random.randint(1, 10)
        })
    write_to_sql(output_file, "EVENT_RESOURCES", data)

# Generate STUDENT data with realistic variability
def generate_students(num_records=1000):
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "FirstName": fake.first_name(),
            "LastName": fake.last_name(),
            "Email": fake.email(domain="example.edu"),
            "PhoneNum": fake.phone_number()
        })
    write_to_sql(output_file, "STUDENT", data)

# Generate CLUB data with realistic variability
def generate_clubs(num_records=20):
    departments = ["Engineering", "Arts", "Sciences", "Business", "Medicine"]
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "Name": fake.bs().capitalize() + " Club",
            "DepartmentID": random.randint(1, len(departments)),
            "President": random.randint(1, 1000),
            "FoundingDate": fake.date_this_century(before_today=True, after_today=False)
        })
    write_to_sql(output_file, "CLUB", data)

# Generate EVENT data with more varied fields
def generate_events(num_records=200):
    event_types = ["Workshop", "Seminar", "Sports", "Cultural", "Networking"]
    venues = list(range(1, 30))  # Assume 30 venues are available
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "Name": fake.catch_phrase(),
            "EventType": random.choice(event_types),
            "Date": fake.date_between(start_date="-1y", end_date="today"),
            "Description": fake.paragraph(nb_sentences=2),
            "ClubID": random.randint(1, 20),
            "VenueID": random.choice(venues)
        })
    write_to_sql(output_file, "EVENT", data)

# Generate EXPENSE data with variability
def generate_expenses(num_records=1000):
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "SpentAmount": round(random.uniform(100, 5000), 2),
            "Description": fake.sentence(nb_words=6),
            "EventID": random.randint(1, 1000)
        })
    write_to_sql(output_file, "EXPENSE", data)

# Generate MEMBERSHIP data, linking students to clubs with realistic membership spread
def generate_memberships(num_records=1000):
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "JoinDate": fake.date_between(start_date="-5y", end_date="today"),
            "ClubID": random.randint(1, 20),
            "StudentID": random.randint(1, 1000)
        })
    write_to_sql(output_file, "MEMBERSHIP", data)

# Generate DEPARTMENT data
def generate_departments(num_records=5):
    department_names = ["Engineering", "Arts", "Sciences", "Business", "Medicine"]
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "Name": department_names[i-1]
        })
    write_to_sql(output_file, "DEPARTMENT", data)

# Generate VENUE data
def generate_venues(num_records=30):
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "Name": f"{fake.company()} {fake.building_number()} {fake.street_name()}",
            "Location": fake.address(),
            "Capacity": random.randint(50, 500),
            "Availability": random.choice([True, False])
        })
    write_to_sql(output_file, "VENUE", data)

# Generate STAFF data
def generate_staff(num_records=50):
    roles = ["Advisor", "Coordinator", "Manager", "Director", "Assistant"]
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "FirstName": fake.first_name(),
            "Role": random.choice(roles)
        })
    write_to_sql(output_file, "STAFF", data)

# Generate TASK data
def generate_tasks(num_records=200):
    statuses = ["Pending", "In Progress", "Completed", "On Hold"]
    data = []
    for i in range(1, num_records + 1):
        deadline = fake.date_between(start_date='now', end_date='+1y')
        data.append({
            "ID": i,
            "Description": fake.sentence(nb_words=6),
            "Deadline": deadline,
            "Status": random.choice(statuses)
        })
    write_to_sql(output_file, "TASK", data)

# Generate RESOURCES data
def generate_resources(num_records=100):
    resource_types = ["Equipment", "Technology", "Consumables", "Space", "Funding"]
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "Name": fake.word().capitalize() + " " + fake.word().capitalize(),
            "Type": random.choice(resource_types),
            "Quantity": random.randint(1, 100)
        })
    write_to_sql(output_file, "RESOURCES", data)

# Generate REGISTRATION data
def generate_registrations(num_records=3000):
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "Timestamp": fake.date_time_this_year(),
            "Attendance": random.choice([True, False]),
            "EventID": random.randint(1, 1000),
            "StudentID": random.randint(1, 1000)
        })
    write_to_sql(output_file, "REGISTRATION", data)

# Generate VOLUNTEER data
def generate_volunteers(num_records=100):
    volunteer_roles = ["Event Staff", "Setup", "Cleanup", "Technical Support", "Registration"]
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "Role": random.choice(volunteer_roles),
            "Hours": random.randint(1, 10),
            "EventID": random.randint(1, 1000),
            "StudentID": random.randint(1, 1000)
        })
    write_to_sql(output_file, "VOLUNTEER", data)

# Generate FEEDBACK data
def generate_feedback(num_records=1000):
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "Rating": random.randint(1, 5),
            "Comments": fake.paragraph(nb_sentences=2),
            "DateSubmitted": fake.date_between(start_date='-1y', end_date='today'),
            "EventID": random.randint(1, 1000),
            "StudentID": random.randint(1, 1000)
        })
    write_to_sql(output_file, "FEEDBACK", data)

# Generate APPLICATION data
def generate_applications(num_records=500):
    positions = ["President", "Vice President", "Treasurer", "Secretary", "Event Coordinator"]
    statuses = ["Pending", "Approved", "Rejected"]
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "Position": random.choice(positions),
            "Status": random.choice(statuses),
            "StudentID": random.randint(1, 1000),
            "ClubID": random.randint(1, 20)
        })
    write_to_sql(output_file, "APPLICATION", data)

# Generate SPONSOR data
def generate_sponsors(num_records=50):
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "ID": i,
            "Name": fake.company(),
            "Amount": round(random.uniform(500, 10000), 2),
            "EventID": random.randint(1, 1000)
        })
    write_to_sql(output_file, "SPONSOR", data)

# Generate all data
def generate_all_data():
    # Open the output file once to initialize
    with open(output_file, mode='w') as file:
        file.write("")

    # Generate all the tables
    generate_students()
    generate_clubs()
    generate_events()
    generate_expenses()
    generate_memberships()
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

# Call the function to generate all data
generate_all_data()

print("SQL data generation completed.")
