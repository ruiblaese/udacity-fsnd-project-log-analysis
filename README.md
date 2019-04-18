# Project: Log Analysis (Full Stack Web Developer Nanodegree)

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>


My first project for courses [Full Stack Web Developer Nanodegree program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Intro](#intro)
- [Installation](#installation)
- [Instructions](#instructions)
- [Supporting](#supporting)

## Intro

In the next part of this course, you'll use a virtual machine (VM) to run an SQL database server and a web app that uses it. The VM is a Linux server system that runs on top of your own computer. You can share files easily between your computer and the VM; and you'll be running a web service inside the VM which you'll be able to access from your regular browser.

## Installation

- Install VirtualBox, instructions for VirtualBox [here](https://github.com/udacity/fullstack-nanodegree-vm)

## Instructions

### - Restore database, instructions:
Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
Here's what this command does:

- psql — the PostgreSQL command line program   
- -d news — connect to the database named news which has been set up for you
- -f newsdata.sql — run the SQL statements in the file newsdata.sql   

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.


### - Execute project on vagrant, instructions:

  `cd /vagrant`    
  `git clone https://github.com/ruiblaese/udacity-fsnd-project-log-analysis.git`   
  `cd udacity-fsnd-project-log-analysis`  

  first option:  
  `python analysis_report.py`  
  
  second option, create http server com report:

  `python analysis_server.py`  
  open browser in: http://localhost:8000


## Supporting 
ruiblaese@gmail.com


[(Back to TOC)](#table-of-contents)