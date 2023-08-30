# django Inventory Project

Inventory management system using Django.

python -m venv env
source env/bin/activate (mac)
source env\Scripts\activate (windows)

pip install -r requirements.txt

cd inventory

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
