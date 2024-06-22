# EcoChic Website

EcoChic is a fashion brand dedicated to sustainability and style. Our website showcases our commitment to eco-friendly practices and offers a range of ethically sourced and fashionable clothing for the modern consumer.

## Project Structure

The project is structured as follows:

Ecochic_website/
├── ecochic/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ ├── asgi.py
│ ├── static/
│ │ ├── css/
│ │ │ └── style.css
│ │ └── media/
│ │ ├── C.E.O.jpg
│ │ ├── Jphoto.jpg
│ │ └── AD.jpg
│ └── templates/
│ └── trends/
│ ├── home.html
│ ├── team.html
│ └── milestones.html
| __ registration
|        login.html
├── trends/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
└── manage.py


## Features

- **Home Page:** Introduction to EcoChic and our mission.
- **Team Page:** Meet the team behind EcoChic with their bios and images.
- **Milestones Page:** Key milestones and achievements of EcoChic.
- **Trends Page:** Stay updated with the latest trends in sustainable fashion.
- **Login Page:** 

## Setup and Installation

1. **Clone the Repository:**
   ```sh
   git clone <repository_url>
Navigate to the Project Directory:

sh
Copy code
cd Ecochic_website
Create a Virtual Environment:

sh
Copy code
python -m venv myenv
Activate the Virtual Environment:

On Windows:
sh
Copy code
myenv\Scripts\activate
On macOS/Linux:
sh
Copy code
source myenv/bin/activate
Install Dependencies:

sh
Copy code
pip install -r requirements.txt
Apply Migrations:

sh
Copy code
python manage.py migrate
Run the Development Server:

sh
Copy code
python manage.py runserver
Open the Website:
Open your web browser and go to http://127.0.0.1:8000 to see the website.

Contributing
We welcome contributions to improve the EcoChic website. If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bugfix.
Commit your changes and push the branch to your forked repository.
Open a pull request and describe your changes.
License
This project is licensed under the MIT License.

Contact
For any inquiries or support, please contact us at lorineabdul@gmil.com

Thank you for visiting EcoChic! Join us in making fashion more sustainable and stylish.
