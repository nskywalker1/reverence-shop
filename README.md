# REVERENCE SHOP
## Online clothing shop created in django using postgresql database. I created it to practice my knowledge in django and use new approaches to develop online stores. I learned how to use the Stripe payment system 
### Technologies Used
1. Python
2. Django
3. Bootstrap
4. JavaScript
5. PostgreSQL
6. Stripe
### Installation
1. Clone or download the project to your local machine.
2. Change directory to the "reverence" folder.
3. Ensure that you have Python 3, pip, and virtualenv installed on your machine.
4. Create a virtual environment using the following command:
#### For Linux/macOS:
```bash
python3 -m venv myenv
```
#### For Windows
```bash
python -m venv venv
```
5. Activate the virtual environment:
   For Linux/macOS: `source venv/bin/activate`
   For Windows: `venv\scripts\Activate`
6. Install the application requirements by running: `pip install -r requirements.txt`
7. Create env file in project directory and fill fields POSTGRES_DB, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER, PASSWORD
8. Migrate the database by executing: `python manage.py migrate`
9. Create account in Stripe site and file fields STRIPE_TEST_PUBLIC_KEY, STRIPE_TEST_SECRET_KEY
10. Start server: `python manage.py runserver`
#### Create superuser
You need to create superuser if you want to add clothing, categories, size etc.:
`python manage.py createsuperuser`
