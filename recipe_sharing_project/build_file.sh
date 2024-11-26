# python3.9 -m install -r requirements.txt
# python3.9 manage.py collectstatic --noinput --clear


pip install -r requirements.txt
python3 manage.py collectstatic --noinput
python3 manage.py migrate