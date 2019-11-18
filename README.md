# Pregame 
A web app for planning "pregames" around events already happening in a city. 
Users are able to post details to where they will be hanging out before the event and other users can see these details and say they are coming. 



## Screenshots
![image of pregame website](https://raw.githubusercontent.com/MCaldwell-42/pregame/master/pregame_screen.png)

### Installing

1. Clone down this repository and cd into it.
2. Once inside this repository, cd into `pregameproject`
1. Create your virtual environment
```
python -m venv pregameenv
```
* Start virtual environment on Mac
```
source ./pregameenv/bin/activate
```
* Start virtual environment on Windows
```
source ./pregameenv/Scripts/activate
```
5. Run `cd ..` You should be in a directory containing `requirements.txt`
6. Install the app's dependencies:
```
pip install -r requirements.txt
```
7. Run makemigrations
`python manage.py makemigrations pregameApp`

8. Run migrate
`python manage.py migrate`
>This will create all the migrations needed for Django Framework to post items to the database based on the models in the Models/ directory
9. You'll need to creat an account with google maps API and obtain an api key<br>

 Once you have an api key, create a file called 'maps.py' in the views directory and put your key inside <br>
 ```
 Mapkey="your API_KEY here"
 ```
## Run Server
make sure you're inside of the 'pregame' directory

`python manage.py runserver `
Ctrl+C to quit

10. Go to http://127.0.0.1:8000/ and create an account <br>

11. begin hosting and finding pregames! 