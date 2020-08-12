<h1 align="center">ClassRoom</h1>


![](https://img.shields.io/github/repo-size/itsvinayak/django-classroom.svg?label=Repo%20size&style=flat-square)&nbsp; ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square)&nbsp;

A Online ClassRoom created using python (django framework) at backend .
Some of the features of website include implementation of login/logout system for students/teacher ,
it's a responsive website which is also a standalone progressive web app and provide dynamic notification and content from backend.

<p align="center"><img src="img/screen.png"/></p>

# Why Django ?

Django is an open-source python web framework used for rapid development, pragmatic, maintainable, clean design, and secures websites. A web application framework is a toolkit of all components need for application development. The main goal of the Django framework is to allow developers to focus on components of the application that are new instead of spending time on already developed components. Django is fully featured than many other frameworks on the market. It takes care of a lot of hassle involved in the web development; enables users to focus on developing components needed for their application.


[![Made with python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://github.com/itsvinayak/django-classroom)

## Virtualenv & Dependencies

create a virtualenv and run requirements.txt<br/>
<b>virtualenv</b>

<pre>pip install virtualenv</pre>

<b> what is virtual environment ? </b><br/>
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.
<br/>
<a href="https://www.geeksforgeeks.org/python-virtual-environment/" >read more... </a>

to run requirements.txt

<pre>$ pip install -r requirements.txt</pre>
 
here <b>env/</b> folder contains all dependencies

## use docker to run 
(Working on it)
<a href="https://www.geeksforgeeks.org/how-to-install-and-configure-docker-in-ubuntu/" tagret="_black" >How to Install and Configure Docker in Ubuntu?</a>

<a href="https://www.geeksforgeeks.org/dockerizing-a-simple-django-app/" target="_black">Dockerizing a simple Django app</a>

pull docker image using 
<pre>$ docker push itssvinayak/django-classroom:latest</pre>

run docker file using
<pre>$ sudo docker run -p 8000:8000 django-classroom</pre>

## Features

<ul>
  <li>responsive bootstrap design </li>
  <li>Students/Teacher login and registration feature</li>
  <li>news section with users feedback (like and comment button include )</li>
  <li>Online assignment feature</li>
  <li>auto attendance management system</li>
  <li>admin system for management</li>
</ul>


## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/itsvinayak/django-classroom 


<strong>made by vinayak with 💕 and 💻</strong>
