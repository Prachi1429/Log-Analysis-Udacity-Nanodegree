## **LOG ANALYSIS PROJECT**
### **INTRODUCTION:**
This is the third project under Udacity FullStack Nanodegree Program.The database contains newspaper articles, as well as the web server log for the newspaper site. The log has a database row for each time a reader loaded a web page. Using that information, this code will answer questions about the site's user activityIn this project, we work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths.

### Requirements:
To start on this project, we need database software (provided by a Linux virtual machine) and the data to analyze.
1. Vagrant : Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.
2. Virtual Box : VirtualBox is the software that actually runs the virtual machine. Download from virtualbox.org 
3. Python : For downloading Python, Visit: https://www.python.org/downloads/
- In this project Python 3.6 (32-bit ) was used.

### Installation:
1. Install Virtual Box and Vagrant.
2. Bring the virtual machine online with vagrant up. Then log into it with vagrant ssh.
3. Unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
4. To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql

### Error Handling
If this command gives an error message, such as —
psql: FATAL: database "news" does not exist
psql: could not connect to server: Connection refused
— this means the database server is not running or is not set up correctly. This can happen if you have an older version of the VM configuration from before this project was added. 

### How to run the application:
1. Login into the Vagrant subdirectory with cd /vagrant.
2. Then, run the command python Log.py on the command.

