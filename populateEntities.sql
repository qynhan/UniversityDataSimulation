-- Drop tables if they exist
SET foreign_key_checks = 0;
DROP TABLE IF EXISTS EVENT_RESOURCES;
DROP TABLE IF EXISTS EVENT;
DROP TABLE IF EXISTS EXPENSE;
DROP TABLE IF EXISTS VOLUNTEER;
DROP TABLE IF EXISTS FEEDBACK;
DROP TABLE IF EXISTS REGISTRATION;
DROP TABLE IF EXISTS MEMBERSHIP;
DROP TABLE IF EXISTS APPLICATION;
DROP TABLE IF EXISTS RESOURCES;
DROP TABLE IF EXISTS SPONSOR;
DROP TABLE IF EXISTS STAFF;
DROP TABLE IF EXISTS VENUE;
DROP TABLE IF EXISTS TASK;
DROP TABLE IF EXISTS CLUB;
DROP TABLE IF EXISTS DEPARTMENT;
DROP TABLE IF EXISTS STUDENT;
SET foreign_key_checks = 1;


-- Create the DEPARTMENT table
CREATE TABLE DEPARTMENT (
    ID INT PRIMARY KEY,
    Name VARCHAR(100)
);

CREATE TABLE Test (
    ID INT PRIMARY KEY,
    Name VARCHAR(50)
);

-- Create the STUDENT table
CREATE TABLE STUDENT (
    ID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNum VARCHAR(25)
);

-- Create the VENUE table
CREATE TABLE VENUE (
    ID INT PRIMARY KEY,
    Name VARCHAR (100) ,
    Location VARCHAR(100),
    Capacity INT,
    Availability BOOLEAN
);

-- Create the CLUB table (This should be before EVENT)
CREATE TABLE CLUB (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    DepartmentID INT,
    President INT,
    FoundingDate DATE,
    FOREIGN KEY (DepartmentID) REFERENCES DEPARTMENT(ID),
    FOREIGN KEY (President) REFERENCES STUDENT(ID)
);

-- Create the EVENT table (Now CLUB exists)
CREATE TABLE EVENT (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    EventType VARCHAR(50),
    Date DATE,
    Description TEXT,
    ClubID INT,
    VenueID INT,
    FOREIGN KEY (ClubID) REFERENCES CLUB(ID),
    FOREIGN KEY (VenueID) REFERENCES VENUE(ID)
);

-- Create the STAFF table
CREATE TABLE STAFF (
    ID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    Role VARCHAR(50)
);

-- Create the EXPENSE table
CREATE TABLE EXPENSE (
    ID INT PRIMARY KEY,
    SpentAmount DECIMAL(10, 2),
    Description TEXT,
    EventID INT,
    FOREIGN KEY (EventID) REFERENCES EVENT(ID)
);

-- Create the SPONSOR table
CREATE TABLE SPONSOR (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    PhoneNum VARCHAR(25),
    ContributionType VARCHAR(50),
    Amount DECIMAL(10, 2)
);

-- Create the RESOURCES table
CREATE TABLE RESOURCES (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Type VARCHAR(50),
    Quantity INT
);

-- Create the EVENT_RESOURCES table
CREATE TABLE EVENT_RESOURCES (
    EventID INT,
    ResourceID INT,
    UsedAmount INT,
    PRIMARY KEY (EventID, ResourceID),
    FOREIGN KEY (EventID) REFERENCES EVENT(ID),
    FOREIGN KEY (ResourceID) REFERENCES RESOURCES(ID)
);

-- Create the TASK table
CREATE TABLE TASK (
    ID INT PRIMARY KEY,
    Description TEXT,
    Deadline DATE,
    Status VARCHAR(50)
);

-- Create the REGISTRATION table
CREATE TABLE REGISTRATION (
    ID INT PRIMARY KEY,
    Timestamp DATETIME,
    Attendance BOOLEAN,
    EventID INT,
    StudentID INT,
    FOREIGN KEY (EventID) REFERENCES EVENT(ID),
    FOREIGN KEY (StudentID) REFERENCES STUDENT(ID)
);

-- Create the MEMBERSHIP table
CREATE TABLE MEMBERSHIP (
    ID INT PRIMARY KEY,
    JoinDate DATE,
    ClubID INT,
    StudentID INT,
    FOREIGN KEY (ClubID) REFERENCES CLUB(ID),
    FOREIGN KEY (StudentID) REFERENCES STUDENT(ID)
);

-- Create the VOLUNTEER table
CREATE TABLE VOLUNTEER (
    ID INT PRIMARY KEY,
    Role VARCHAR(50),
    Hours INT,
    EventID INT,
    StudentID INT,
    FOREIGN KEY (EventID) REFERENCES EVENT(ID),
    FOREIGN KEY (StudentID) REFERENCES STUDENT(ID)
);

-- Create the FEEDBACK table
CREATE TABLE FEEDBACK (
    ID INT PRIMARY KEY,
    Rating INT,
    Comments TEXT,
    DateSubmitted DATE,
    EventID INT,
    StudentID INT,
    FOREIGN KEY (EventID) REFERENCES EVENT(ID),
    FOREIGN KEY (StudentID) REFERENCES STUDENT(ID)
);

-- Create the APPLICATION table
CREATE TABLE APPLICATION (
    ID INT PRIMARY KEY,
    Position VARCHAR(50),
    Date DATE,
    Status VARCHAR(50),
    ClubID INT,
    StudentID INT,
    FOREIGN KEY (ClubID) REFERENCES CLUB(ID),
    FOREIGN KEY (StudentID) REFERENCES STUDENT(ID)
);





















-- Sample Inserts for DEPARTMENT
INSERT INTO DEPARTMENT (ID, Name) VALUES 
(1, 'Computer Science'),
(2, 'Electrical Engineering'),
(3, 'Mechanical Engineering'),
(4, 'Business Administration'),
(5, 'Psychology'),
(6, 'Biology'),
(7, 'Chemistry'),
(8, 'Physics'),
(9, 'Mathematics'),
(10, 'Communications');

-- Sample Inserts for STUDENT
INSERT INTO STUDENT (ID, FirstName, LastName, Email, PhoneNum) VALUES 
(1, 'John', 'Doe', 'john.doe@example.com', '555-1234'),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '555-5678'),
(3, 'Mike', 'Johnson', 'mike.johnson@example.com', '555-9012'),
(4, 'Emily', 'Brown', 'emily.brown@example.com', '555-3456'),
(5, 'David', 'Wilson', 'david.wilson@example.com', '555-7890'),
(6, 'Sarah', 'Taylor', 'sarah.taylor@example.com', '555-2345'),
(7, 'Alex', 'Martinez', 'alex.martinez@example.com', '555-6789'),
(8, 'Emma', 'Anderson', 'emma.anderson@example.com', '555-0123'),
(9, 'Ryan', 'Thomas', 'ryan.thomas@example.com', '555-4567'),
(10, 'Olivia', 'Garcia', 'olivia.garcia@example.com', '555-8901');

-- Sample Inserts for VENUE
INSERT INTO VENUE (ID, Name, Location, Capacity, Availability) VALUES 
(1, 'Main Auditorium', 'Central Campus', 500, TRUE),
(2, 'Science Building Lecture Hall', 'Science Complex', 200, TRUE),
(3, 'Student Union Conference Room', 'Student Center', 100, TRUE),
(4, 'Engineering Workshop', 'Engineering Building', 50, TRUE),
(5, 'Library Multipurpose Room', 'Main Library', 75, TRUE),
(6, 'Sports Complex Arena', 'Athletics Center', 1000, TRUE),
(7, 'Business School Seminar Room', 'Business Building', 80, TRUE),
(8, 'Art Gallery', 'Creative Arts Center', 120, TRUE),
(9, 'Chemistry Lab', 'Science Complex', 30, TRUE),
(10, 'Outdoor Amphitheater', 'Campus Green', 250, TRUE);

-- Sample Inserts for CLUB with Department and President References
INSERT INTO CLUB (ID, Name, DepartmentID, President, FoundingDate) VALUES 
(1, 'Robotics Club', 1, 1, '2020-09-01'),
(2, 'Debate Society', 10, 2, '2019-02-15'),
(3, 'Computer Programming Society', 1, 3, '2018-11-10'),
(4, 'Environmental Action Group', 6, 4, '2021-03-20'),
(5, 'Business Innovation Network', 4, 5, '2017-08-05'),
(6, 'Chess Club', 9, 6, '2019-10-12'),
(7, 'Drama Society', 10, 7, '2020-01-25'),
(8, 'Physics Exploration Group', 8, 8, '2018-06-30'),
(9, 'Machine Learning Club', 1, 9, '2021-09-15'),
(10, 'Psychology Research Club', 5, 10, '2019-04-22');

-- Sample Inserts for EVENT
INSERT INTO EVENT (ID, Name, EventType, Date, Description, ClubID, VenueID) VALUES 
(1, 'Annual Robotics Showcase', 'Technical', '2024-03-15', 'Robotics projects exhibition', 1, 1),
(2, 'Intercollegiate Debate Tournament', 'Academic', '2024-04-20', 'Regional debate competition', 2, 2),
(3, 'Hackathon 2024', 'Technical', '2024-05-10', 'Programming marathon', 3, 4),
(4, 'Sustainability Fair', 'Community', '2024-02-25', 'Environmental awareness event', 4, 10),
(5, 'Startup Pitch Competition', 'Professional', '2024-06-05', 'Student business ideas showcase', 5, 7),
(6, 'Chess Championship', 'Academic', '2024-01-30', 'Annual university chess tournament', 6, 3),
(7, 'Theater Production', 'Cultural', '2024-04-15', 'Annual drama club performance', 7, 8),
(8, 'Physics Symposium', 'Academic', '2024-03-05', 'Research presentations', 8, 2),
(9, 'AI and Machine Learning Workshop', 'Technical', '2024-02-10', 'Latest trends in AI', 9, 5),
(10, 'Psychology Research Symposium', 'Academic', '2024-05-22', 'Student research presentations', 10, 9);

-- Sample Inserts for STAFF
INSERT INTO STAFF (ID, FirstName, Role) VALUES 
(1, 'Michael', 'Event Coordinator'),
(2, 'Lisa', 'Club Advisor'),
(3, 'Robert', 'Administrative Director'),
(4, 'Karen', 'Student Activities Manager'),
(5, 'David', 'Technical Support'),
(6, 'Emily', 'Campus Events Planner'),
(7, 'Steven', 'Facilities Manager'),
(8, 'Jennifer', 'Student Services Director'),
(9, 'Mark', 'Operations Coordinator'),
(10, 'Amanda', 'Campus Engagement Officer');

-- Sample Inserts for EXPENSE
INSERT INTO EXPENSE (ID, SpentAmount, Description, EventID) VALUES 
(1, 1500.00, 'Robotics Equipment', 1),
(2, 750.50, 'Tournament Prizes', 2),
(3, 2000.00, 'Hackathon Supplies', 3),
(4, 500.25, 'Sustainability Materials', 4),
(5, 1200.75, 'Competition Logistics', 5),
(6, 350.00, 'Chess Tournament Setup', 6),
(7, 1800.50, 'Theater Production Costs', 7),
(8, 650.25, 'Symposium Catering', 8),
(9, 900.00, 'Workshop Technology', 9),
(10, 475.50, 'Research Presentation Expenses', 10);

-- Sample Inserts for SPONSOR
INSERT INTO SPONSOR (ID, Name, PhoneNum, ContributionType, Amount) VALUES 
(1, 'Tech Innovations Inc.', '888-123-4567', 'Financial', 5000.00),
(2, 'Global Solutions Corp', '888-987-6543', 'Equipment', 3500.00),
(3, 'Startup Accelerator Network', '888-456-7890', 'Mentorship', 2000.00),
(4, 'Local Business Alliance', '888-234-5678', 'Financial', 4500.00),
(5, 'Community Tech Fund', '888-345-6789', 'Grants', 6000.00),
(6, 'Regional Development Bank', '888-567-8901', 'Financial', 3000.00),
(7, 'Innovation Research Grant', '888-678-9012', 'Research Support', 4000.00),
(8, 'Student Success Foundation', '888-789-0123', 'Scholarship', 2500.00),
(9, 'Technology Education Trust', '888-890-1234', 'Financial', 5500.00),
(10, 'Corporate Social Responsibility Fund', '888-901-2345', 'Equipment', 3750.00);

-- Sample Inserts for RESOURCES
INSERT INTO RESOURCES (ID, Name, Type, Quantity) VALUES 
(1, 'Projector', 'AV Equipment', 10),
(2, 'Laptop', 'Computing', 25),
(3, 'Microphone', 'Audio Equipment', 15),
(4, 'Speaker', 'Audio Equipment', 12),
(5, 'Chairs', 'Furniture', 200),
(6, 'Tables', 'Furniture', 50),
(7, 'White Board', 'Presentation', 8),
(8, 'Extension Cords', 'Electrical', 30),
(9, 'Power Strips', 'Electrical', 20),
(10, 'Screen', 'Projection', 5);

-- Sample Inserts for EVENT_RESOURCES
INSERT INTO EVENT_RESOURCES (EventID, ResourceID, UsedAmount) VALUES 
(1, 1, 3),
(1, 2, 5),
(2, 3, 2),
(2, 4, 4),
(3, 5, 50),
(3, 6, 10),
(4, 7, 2),
(4, 8, 5),
(5, 9, 4),
(5, 10, 1);

-- Sample Inserts for TASK
INSERT INTO TASK (ID, Description, Deadline, Status) VALUES 
(1, 'Prepare Robotics Showcase Presentation', '2024-03-10', 'In Progress'),
(2, 'Organize Debate Tournament Logistics', '2024-04-15', 'Not Started'),
(3, 'Set Up Hackathon Registration', '2024-05-01', 'Completed'),
(4, 'Develop Sustainability Fair Marketing Plan', '2024-02-20', 'In Progress'),
(5, 'Coordinate Startup Pitch Competition Judges', '2024-05-25', 'Not Started'),
(6, 'Arrange Chess Championship Venue', '2024-01-25', 'Completed'),
(7, 'Finalize Theater Production Script', '2024-04-01', 'In Progress'),
(8, 'Prepare Physics Symposium Presentations', '2024-02-28', 'Not Started'),
(9, 'Develop AI Workshop Curriculum', '2024-01-30', 'Completed'),
(10, 'Organize Psychology Research Presentation Schedule', '2024-05-15', 'In Progress');

-- Sample Inserts for REGISTRATION
INSERT INTO REGISTRATION (ID, Timestamp, Attendance, EventID, StudentID) VALUES 
(1, '2024-03-10 09:15:00', TRUE, 1, 1),
(2, '2024-03-11 10:30:00', FALSE, 1, 2),
(3, '2024-04-15 11:45:00', TRUE, 2, 3),
(4, '2024-04-16 12:00:00', TRUE, 2, 4),
(5, '2024-05-05 14:20:00', TRUE, 3, 5),
(6, '2024-05-06 15:30:00', FALSE, 3, 6),
(7, '2024-02-20 16:45:00', TRUE, 4, 7),
(8, '2024-02-21 17:00:00', TRUE, 4, 8),
(9, '2024-06-01 18:15:00', TRUE, 5, 9),
(10, '2024-06-02 19:30:00', FALSE, 5, 10);

-- Sample Inserts for MEMBERSHIP
INSERT INTO MEMBERSHIP (ID, JoinDate, ClubID, StudentID) VALUES 
(1, '2023-09-15', 1, 1),
(2, '2023-10-01', 2, 2),
(3, '2023-11-10', 3, 3),
(4, '2023-12-05', 4, 4),
(5, '2024-01-20', 5, 5),
(6, '2024-02-15', 6, 6),
(7, '2024-03-01', 7, 7),
(8, '2024-04-10', 8, 8),
(9, '2024-05-05', 9, 9),
(10, '2024-06-20', 10, 10);

-- Sample Inserts for VOLUNTEER
INSERT INTO VOLUNTEER (ID, Role, Hours, EventID, StudentID) VALUES 
(1, 'Setup Crew', 4, 1, 1),
(2, 'Registration', 3, 2, 2),
(3, 'Technical Support', 5, 3, 3),
(4, 'Marketing', 2, 4, 4),
(5, 'Stage Management', 3, 5, 5),
(6, 'Event Coordination', 4, 6, 6),
(7, 'Sound and Lighting', 3, 7, 7),
(8, 'Speaker Assistance', 2, 8, 8),
(9, 'Workshop Assistant', 3, 9, 9),
(10, 'Presentation Support', 2, 10, 10);

-- Sample Inserts for FEEDBACK
INSERT INTO FEEDBACK (ID, Rating, Comments, DateSubmitted, EventID, StudentID) VALUES 
(1, 5, 'Amazing robotics showcase!', '2024-03-16', 1, 1),
(2, 4, 'Interesting debate topics', '2024-04-21', 2, 2),
(3, 5, 'Great hackathon experience', '2024-05-11', 3, 3),
(4, 3, 'Could improve sustainability fair organization', '2024-02-26', 4, 4),
(5, 4, 'Inspiring startup pitches', '2024-06-06', 5, 5),
(6, 5, 'Well-organized chess tournament', '2024-01-31', 6, 6),
(7, 4, 'Enjoyable theater production', '2024-04-16', 7, 7),
(8, 3, 'Complex physics research', '2024-03-06', 8, 8),
(9, 5, 'Informative AI workshop', '2024-02-11', 9, 9),
(10, 4, 'Interesting psychology research', '2024-05-23', 10, 10);

-- Sample Inserts for APPLICATION
INSERT INTO APPLICATION (ID, Position, Date, Status, ClubID, StudentID) VALUES 
(1, 'Vice President', '2024-01-15', 'Approved', 1, 2),
(2, 'Event Coordinator', '2024-02-01', 'Pending', 2, 3),
(3, 'Technical Lead', '2024-03-10', 'Rejected', 3, 4),
(4, 'Sustainability Officer', '2024-04-05', 'Approved', 4, 5),
(5, 'Marketing Director', '2024-05-20', 'Pending', 5, 6),
(6, 'Tournament Organizer', '2024-06-15', 'Approved', 6, 7),
(7, 'Stage Manager', '2024-07-01', 'Pending', 7, 8),
(8, 'Research Coordinator', '2024-08-10', 'Rejected', 8, 9);



-- SELECT E.Name AS EventName, 
--        COUNT(R.StudentID) AS StudentAttendance
-- FROM EVENT E
-- LEFT JOIN REGISTRATION R ON E.ID = R.EventID
-- GROUP BY E.Name
-- ORDER BY StudentAttendance DESC;


-- SELECT 
--     d.Name AS DepartmentName, 
--     COUNT(DISTINCT r.StudentID) AS TotalStudentsAttended
-- FROM 
--     DEPARTMENT d
-- JOIN 
--     CLUB c ON d.ID = c.DepartmentID
-- JOIN 
--     EVENT e ON c.ID = e.ClubID
-- JOIN 
--     REGISTRATION r ON e.ID = r.EventID
-- WHERE 
--     r.Attendance = TRUE
-- GROUP BY 
--     d.Name
-- ORDER BY 
--     TotalStudentsAttended DESC;


SELECT 
    d.Name AS DepartmentName,
    ROUND(AVG(r.TotalStudentsAttended), 2) AS AvgStudentsAttended,
    ROUND(AVG(e2.TotalSpending), 2) AS AvgSpending
FROM 
    DEPARTMENT d
JOIN 
    CLUB c ON d.ID = c.DepartmentID
JOIN 
    EVENT e ON c.ID = e.ClubID
LEFT JOIN 
    (SELECT 
        EventID, 
        COUNT(DISTINCT StudentID) AS TotalStudentsAttended
    FROM 
        REGISTRATION
    WHERE 
        Attendance = TRUE
    GROUP BY 
        EventID) r ON e.ID = r.EventID
LEFT JOIN 
    (SELECT 
        EventID, 
        SUM(SpentAmount) AS TotalSpending
    FROM 
        EXPENSE
    GROUP BY 
        EventID) e2 ON e.ID = e2.EventID
GROUP BY 
    d.Name
ORDER BY 
    AvgStudentsAttended DESC;


+-------------------------+---------------------+-------------+
| DepartmentName          | AvgStudentsAttended | AvgSpending |
+-------------------------+---------------------+-------------+
| Biology                 |               64.33 |      500.25 |
| Communications          |               53.42 |     1275.50 |
| Computer Science        |               50.87 |     1466.67 |
| Business Administration |               34.36 |     1200.75 |
| Psychology              |               19.34 |      475.50 |
| Physics                 |               14.49 |      650.25 |
| Mathematics             |               12.42 |      350.00 |
+-------------------------+---------------------+-------------+