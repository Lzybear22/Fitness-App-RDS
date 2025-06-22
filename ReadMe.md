# Overview

{Important! Do not say in this section that this is college assignment. Talk about what you are trying to accomplish as a software engineer to further your learning.}

This program is a health and fitness tracker made with Python that is connected to a Amazon RDS database. The data is stored in the cloud instead of on your personal computer. With this program you can add workouts, log health information, view what you have logged and delete data if you want to. 

The purpose of making this program is to keep track of diffrent workouts and health data. I wanted to make sure my data couldn't be lost and be accessed anywhere so I hosted a database in a Amazon RDS database in the cloud. This program also helped me learn how to connect a python program to a cloud database and use it to hold information.


Youtube Video: https://youtu.be/VgjTBqqpLrM

# Cloud Database

I am using Amazon's Relational Database Service(RDS) or my cloud database. This lets me run a database in the cloud so I can store data without running my own server and database. Also I can always access it on any computer.

My database is called workout and has two tables. One is Workouts and it has user_id which is the id of the user, exercise_name which allows users to add the name of the workout. Duration which is how long the workout lasted. Weight which is how much weight you used in pounds. And finally workout_date which is the day the workout happend. The second table is health_data which has user_id to store who made the querys. Weight which is how much you weigh. Calories_burned which is how much calories you've burned. And finaly health_date which just tracks the day you added them.

# Development Environment

To make this program I used Python and connected it to a Amazon RDS database. Python is a object oriented program languge that can work with MySQL. For the database I used Amazon RDS lets me store data remotely. To connect my python program to RDS I used pymysql library. This lets my Python code to connect with MySQL databases. And I used datetime to record the dates of when the workouts were logged.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- AWS(https://docs.aws.amazon.com/rds/)
- MySQLTutorial(https://www.mysqltutorial.org/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Add user authentication to make data more secure
- Add milestone data to automaticlly show off how you've done the past month
- Make it so it can be used on phones so its more user friendly 