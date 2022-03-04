PROJECT WORK REPORT
This is a project on a Simple data driven project with flask web framework. The basic design structure of this project is It should be able to tap into a database of blog post and render them to a template in an ideal way.
To begin with, we have to know the dependencies and the technologies that are going to be used in this project. These are:
•	Flask : which is going to be the major framework for the project
•	SqlAlchemy : which will be used to design the database for the project
•	Template files: to render the data from the backend to the frontend.
•	Conda : for setting up a virtual env
•	Gunicorn: to help in hosting the project.

After knowing this we can start working on the project. 
Step1:  Setting up the project
•	Create a folder called Blog_app.
•	Cd into Blog_app and create a virtual env by running the code “conda create -n blog_app “. Make sure you have Anaconda installed on you pc. 
•	In your terminal run “conda activate blog_app”.
•	Now that the env has been created successfully we can now start working on the application.

Step2:  Running your first flask app 
•	Create a file app.py which will house all our code.
•	Inside this file add the following code:
 
•	Now go back into your terminal and run “python app.py”
•	This will run a local server at port 5000. If everything worked fine then we can start creating our routes and database.

Step3 :  Creating routes and hooking it up to the templates and css files 
•	Before we hook up routes to templates we need first create the templates. 
•	Inside the Blog_app dir create a folder called “templates” inside this folder you can add all you html templates. So here we add “index.html”, “new_post.html”, and “detail.html” which can be find in the github repo
 
•	After bringing in these files into the templates folder. Come back to the app.py
 
•	Now we can render the templates by:
 
•	Also to add css and image files we need to create a dir called static 
 
•	Now we can rerun the server to see the changes.


Step 4 :  Creating the database with SqlAchemy
•	Now that we have our templates in place we can now start creating the database 
•	Before that in our terminal we need to run “pip install flask-sqlalchemy”.
•	Now in app.py 
 
•	And the we add this: 
 
•	We can now start creating our database table. Since we are going to have two tables Category and Post.
 
•	Now to commit the changes we need to 
 

•	By running this the database is now created with these tables.
•	You’ll now see a blog.db file in the current directory

Step 5:  Parsing open data source into the database
•	First we need to get the file TechCrunch1.csv from the repo and drop it into our Blog_app dir
•	Now we create a new file “parse-csv.py”.
•	Inside this file we need to first import csv and create_engine which we will use to connect to the database.
•	We then set engine to the name of our database and create a connection to our database 
 
•	Now using the code below we create a for loop to loop through our file to get the records we are looking for 
•	The last step now inserts the data we looped for into the database 
 
•	After everything, you code should look like this: 
 


Step 6:  Parsing the data into the front end
•	After parsing the data into the database we have to render it into the template files.
•	In app.py 
 
•	This queries the database for all the Posts and Categories and is parsed into the templates with the names posts and categories.
•	Now inside index.html we can now loop through posts and categories to get the post titles and all the other values we need using Jinja syntax
 

Step 7:  Hosting the application on Heroku
•	To host the application on Heroku  first create an account with Heroku 
•	Install Heroku cli
•	Come back into you project and create a file “Procfile”
•	Inside this file insert: 
 
•	Open your terminal and in the Blog_app dir type
•	pip install pipreq
•	now type pipreq .  this will generate a requirements.txt file for you .NB without this file the application cannot be hosted
 
•	Now in your terminal type Heroku login
•	This will open in the web browser for you to login 
•	You can now run heroku create 
•	This will create a new app with a random name.
•	Run git push Heroku master
•	Now the application should successfully be deployed.

•	This video  https://www.youtube.com/watch?v=Li0Abz-KT78  gives a detailed explanation to hosting the project on Heroku.