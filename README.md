# Lexus-Feedback-System
A Flask-based web application for collecting and managing customer feedback for Lexus dealerships. The system allows customers to submit feedback about their dealer experience and stores the data in a MySQL database.
Features

Customer feedback form with rating system
Real-time feedback display
MySQL database integration
Email notifications for new feedback (optional)
Responsive web interface

Requirements

Python 3.7+
XAMPP (for MySQL database)
Flask
PyMySQL

Installation
1. Clone or Download the Project
bashgit clone <repository-url>
cd lexus-feedback-system
2. Install Python Dependencies
bashpip install flask pymysql
3. Set Up XAMPP and MySQL Database

Install XAMPP from https://www.apachefriends.org/
Start XAMPP Control Panel and start both Apache and MySQL services
Create Database:

Open phpMyAdmin (http://localhost/phpmyadmin)
Create a new database named akash
Create the feedback table:



sqlCREATE TABLE lexis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer VARCHAR(255) NOT NULL,
    dealer VARCHAR(255) NOT NULL,
    rating INT NOT NULL,
    comments TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
4. Configure Email (Optional)
If you want to enable email notifications:

Sign up for a Mailtrap account at https://mailtrap.io/
Update the send_mail.py file with your Mailtrap credentials:

python   login = 'your-mailtrap-username'
   password = 'your-mailtrap-password'
Project Structure
lexus-feedback-system/
│
├── app.py              # Main Flask application
├── send_mail.py        # Email notification functionality
├── templates/
│   └── index.html      # HTML template (you need to create this)
├── static/             # CSS, JS, images (optional)
└── README.md          # This file
Usage
Running the Application

Start XAMPP services (Apache and MySQL)
Run the Flask application:

bash   python app.py

Open your browser and navigate to: http://127.0.0.1:5000

Using the Feedback Form

Fill in the required fields:

Customer Name: Name of the customer
Dealer: Name of the dealership
Rating: Numerical rating (1-5 or 1-10)
Comments: Detailed feedback


Submit the form to save feedback to the database
View all submitted feedback on the same page

Database Schema
lexis Table
ColumnTypeDescriptionidINTAuto-incrementing primary keycustomerVARCHAR(255)Customer namedealerVARCHAR(255)Dealer nameratingINTCustomer ratingcommentsTEXTCustomer feedback commentscreated_atTIMESTAMPRecord creation timestamp
Configuration
Database Configuration
The application uses the following default MySQL configuration for XAMPP:

Host: localhost
Port: 3306
Username: root
Password: (empty)
Database: akash

To modify these settings, edit the get_db_connection() function in app.py.
Security Configuration

Change the secret key in app.py:

python  app.secret_key = 'your-secure-secret-key-here'
API Endpoints
MethodEndpointDescriptionGET/Display feedback form and all recordsPOST/Submit new feedback
Error Handling
The application includes error handling for:

Database connection issues
Invalid form submissions
MySQL execution errors
Missing required fields

Development
Adding Email Notifications
To integrate email notifications with the feedback submission:

Import the send_mail function in app.py:

python   from send_mail import send_mail

Call the function after successful data insertion:

python   send_mail(customer, dealer, rating, comments)
Customizing the Interface

Modify templates/index.html to customize the web interface
Add CSS files in the static/css/ directory
Add JavaScript files in the static/js/ directory

Troubleshooting
Common Issues

Database Connection Error

Ensure XAMPP MySQL service is running
Verify database name and credentials
Check if the akash database exists


Template Not Found Error

Create the templates/ directory
Ensure index.html exists in the templates folder


Import Error for pymysql

Install pymysql: pip install pymysql


Port Already in Use

Change the port in app.run() to a different number
Or stop other applications using port 5000



Contributing

Fork the repository
Create a feature branch
Make your changes
Test thoroughly
Submit a pull request

License
This project is open source and available under the MIT License.
Support
For support or questions, please create an issue in the repository or contact the development team.
