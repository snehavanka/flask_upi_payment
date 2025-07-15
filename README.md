# flask_upi_payment
A Flask app that captures payer details and generates UPI payment links for instant mobile payments.
 NAME : V . SNEHA 
 DOMAIN : WEB DEVELOPMENT
 DURATION : JUNE 2025 TO JULY 2025
 MENTOR : DR . G. RAMAKRISHNA (IIT Tirupati)
1. Objective
##  Objective
To create a basic payment system that:
- Collects user information securely
- Validates Gmail address format
- Stores data in MySQL
- Generates a UPI deep link for instant payments
2. Features
## Features
- Flask web server
- Regex Gmail verification
- UPI payment link generation
- MySQL integration
- Basic HTML front-end
3. Tech Stack
##  Tech Stack
- Python 3.11+
- Flask
- MySQL
- mysql-connector-python
- HTML, Jinja2 Templates
4. Project Structure
##  Project Structure
project-folder/
├── app.py
├── schema.sql
├── requirements.txt
├── templates/
│   ├── index.html
│   └── payment_success.html
└── README.md
5. How to Run
## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
   cd REPO_NAME
Create a virtual environment:
python -m venv venv
source venv/bin/activate   # or venv\\Scripts\\activate on Windows
Install dependencies:

pip install -r requirements.txt
Set up the database:
Open MySQL and run the schema.sql file:

CREATE DATABASE IF NOT EXISTS payment_db;
USE payment_db;
CREATE TABLE IF NOT EXISTS payments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  upi_id VARCHAR(120),
  receiver_upi_id VARCHAR(120),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Run the Flask app:

python app.py
Open in browser:

Visit http://localhost:5000/

### 6. **How It Works**

- User fills name, Gmail, and UPI ID in `index.html`
- Server verifies Gmail format using regex
- Stores details in MySQL
- Generates and shows a `upi://pay?...` link to open UPI apps
7. Security Notes

##  Security Notes
- Uses parameterized queries to prevent SQL injection
- Gmail format checked with regex
- In production, use `.env` to secure database credentials
- Serve with HTTPS for secure UPI link redirection


