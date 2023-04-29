## What is this

This is a full stack web application that aims to make it easier for people (primarily students) to get work done. This was built at the 2023 BitCamp hackathon in 36 hours with a team of 4. It uses the concept of body doubling to increase productivity - this is when you work at the same time as someone else and essentially hold each other accountable for getting work done. Users of this app would login and have their list of tasks to do for the week - which they can edit, add new, mark as done, etc. In addition to the to-do list, there is a friends page which allows users to connect with other registered users and view their friends' progress as well as a leaderboard. We included a calendar as well which syncs to your to-do list and automatically updates. 

Check out the devPost here: https://devpost.com/software/hoosterrapin

## The tech

**Front end:** 

Bootstrap HTML used to create a dynamic full-featured web app. Built to expand with highly modular code using block architecture.

**Back end:**

Django framework for web development. Built with scaleable design patterns and loosely-coupled components.

Auth0 for secure user-authentication.
          
CockroachDB distributed, serverless database system, used to handle all user data securely and efficiently.

## Set up the project requirements

https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb-django.html#step-3-install-the-application-requirements

```
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
since we're using cockroach db, we need to use a virtual environment. 

## To run and try the program
```
python manage.py runserver
```
This will start a dev server hosted on your machine, follow the provided link to view the site
