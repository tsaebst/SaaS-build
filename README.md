# SaaS-build
Practice 1: Python SaaS 
#To use this code you have to:
1) have your own key generated (use the link in weather_app.py)
2) have a Postman installed (10.22.9 is recommended)
3) have weather_app.py file on your jupyter notebook server
4) donnect to the file using the following command:
uwsgi --http 0.0.0.0:8000 --wsgi-file weather_app.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191 command.
5) insert the created token and key to the file weather_app.py

Additional notes:
1. Don't forget to upgrade your python version to 3.8.0 and pyenv to 2.3.35
2. Install requirements.txt via "pip install -r requirements.txt"
3. If you encounter any issues, please refer to the documentation or contact the developer.
 
Developed by: Spitkovska Vladyslava 
