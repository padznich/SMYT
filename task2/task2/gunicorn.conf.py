bind = '127.0.0.1:8000'
workers = 3
user = "padznich"

"""
# /etc/supervisor/conf.d/task2.conf
[program:task2]
command=/home/padznich/Downloads/SMYT/venv/bin/gunicorn task2.wsgi:application -c /home/padznich/Downloads/SMYT/task2/task2/gunicorn.conf.py
directory=/home/padznich/Downloads/SMYT/task2
user=padznich
autorestart=true
redirect_stderr=true
"""