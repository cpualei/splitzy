<h1 align="center">splitzy</h1>

<p align="center">A full-stack bill-splitting application.
<br><br>   
splitzy provides users the ability to search and add other users as friends and bill them for their dues. Users also have the ability to make notes/add comments to existing bills. To make use of these features, users are required to sign up for an account.
<br><br><b>LIVE LINK: https://splitzyapp-fd4923ca97e0.herokuapp.com/login</b></p>
<br>

## Technologies Used
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## Building the App
1. Clone the main repository

   ```bash
   git clone https://github.com/cpualei/splitzy.git
   ```

2. Install the dependencies

      ```bash
      pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
      ```

3. Create a **.env** file based on the example with proper settings for your
   development environment
4. Setup your PostgreSQL user, password and database and make sure it matches your **.env** file

5. Get into your pipenv, migrate your database, seed your database, and run your flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

6. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.

<br>

### Application Architecture

splitzy is built with Flask (backend), React and Redux (frontend), and PostgresSQL (database).

<br>

### Future Features
We plan to refactor our code to create a dynamic single page application that will mirror that of Splitwise. Refactoring our code will provide enhanced efficiency, fetching required information from the Redux store rather than from backend routes. Our bonus feature, transactions, will also be something to consider including in our splitzy app. More features we plan on implementing is the ability to settle a bill and the ability to subtract from a bill's amount based on recorded payments.

<br>

## Demo Screens

### Splash
![ezgif com-gif-maker (20)](https://user-images.githubusercontent.com/93879557/206110206-ff1ea873-fce6-42f2-9bc9-76445995d51b.gif)

### Add an expense
![ezgif com-gif-maker (22)](https://user-images.githubusercontent.com/93879557/206111425-52056f86-6164-4b2d-864f-3c0fc2fa0e68.gif)

### Edit existing expense
![ezgif com-gif-maker (23)](https://user-images.githubusercontent.com/93879557/206112592-9ec2ab56-0f79-487d-a1d3-d1fbc6b62042.gif)

### Add and edit comment
![ezgif com-gif-maker (24)](https://user-images.githubusercontent.com/93879557/206113627-42700abe-3cdb-487d-b948-24013ee82759.gif)

### Search and add users as friends or unfriend
![ezgif com-gif-maker (26)](https://user-images.githubusercontent.com/93879557/206115239-08ed82cb-eb06-4575-9c27-1574d73a44ed.gif)

### About page
![ezgif com-gif-maker](https://user-images.githubusercontent.com/93879557/206116191-230a4eca-8bc8-4e7c-adba-1f72afad1c61.png)



## Contact Us
* Uki:  <a href="https://www.linkedin.com/in/ukipavlovic/">Linkedin</a> | <a href="https://github.com/ukiukica/">Github</a> 
* Olivia:  <a href="https://www.linkedin.com/in/olivia-bir-74b16b7b/">Linkedin</a> | <a href="https://github.com/oliviabir">Github</a>
* Danny: <a href="https://www.linkedin.com/in/dannytoan/">Linkedin</a> | <a href="https://github.com/dannytoan">Github</a>
* Caitlin:  <a href="https://www.linkedin.com/in/caitlin-buen-lucas/">Linkedin</a> | <a href="https://github.com/cpualei/">Github</a> 
