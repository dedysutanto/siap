# Installation

- Install Python Environment
- pip install -r requirements.txt
- pythoy manage.py makemigrations/migrate
- python manage.py shell (Optional: Init first company)

        from company.models import Company
        company = Company()
        company.code = 'SIS001'
        company.code = 'Salt Integra Solusi'
        company.save()
        exit()

- python manage.py createsuperuser
- Go to admin URL and add record


# To Reset Database

- Delete all files in migrations folders except __init__.py
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser