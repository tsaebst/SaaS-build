# SaaS-build
Practice 1: Python SaaS 
#To use this code you have to:
1) have your own key generated (use the link in weather_app.py)
2) have a Postman installed (10.22.9 is recommended)
3) have weather_app.py file on your jupyter notebook server
4) don't forget to connect to the file using  uwsgi --http 0.0.0.0:8000 --wsgi-file weather_app.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191 command.
5) insert the created token and key to the file weather_app.py


# Developed by: Spitkovska Vladyslava
