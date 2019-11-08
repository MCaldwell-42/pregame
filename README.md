# Pregame 
A web app for planning "pregames" around events already happening in a city. 
Users are able to post details to where they will be hanging out before the event and other users can see these details and say they are coming. 



## Screenshots
![image of pregame website](https://raw.githubusercontent.com/MCaldwell-42/pregame/master/pregame_screen.png)

## Installation Instructions
- Clone down this repo
- At the root of the project, run `pip install`
- Create a database for 
  - Add a web app to the project and enable Google authentication
  - Create a real-time database and seed it with the data from the database directory
- Create a file named `/helpers/data/apiKeys.json` and add your Firebase keys using the `apiKeys.example.json` as a template

## How to Run
- In your terminal, type `npm start`

***Note**: if you want to make a production build of this project, type `npm run build`.  This will create a folder called build with all the minified code you need.*

## How to deploy
- In your terminal, type `npm run deploy`