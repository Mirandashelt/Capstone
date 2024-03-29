# Credits

**This project was created by:**
- [Rodolfo Hernandez-Noria](mailto:RHERNA70@mail.depaul.edu)
- [Kyle Mastrangeli](https://github.com/kylem164)
- [Genevive Myers](https://github.com/genevievemmyers)
- [Ross Nelson](https://rossnelson.me)
- [Arielle Reese](https://github.com/Arreese16)
- [Miranda Shelton](https://github.com/Mirandashelt)
- [Jonathan Smajo](mailto:jnsmajoj@gmail.com)

This project is our Capstone project for CSC394 at [DePaul University's College of Computing and Digital Media](https://www.cdm.depaul.edu/).

# Tutorial

**What you will need to run the project:**
- [Python 3.6](https://www.python.org/)
- [Pip 9.0.1](https://pypi.org/project/pip/)
- [Channnels 2.3.1](https://channels.readthedocs.io/en/latest/)
- [Django 2.2.7](https://www.djangoproject.com/)
- [Git 2.17](https://git-scm.com/)

**Notes:**
- This tutorial assumes that you are using a Linux-based operating system. If you are using Windows 10, you can install the Ubuntu subsystem by following [this](https://docs.microsoft.com/en-us/windows/wsl/install-win10) tutorial. After completing that installation, you should then be able to follow this tutorial.
- This project uses [Redis.io](https://redis.io) in order for the chat to function correctly. Setting up Redis will not be covered in this tutorial so the chat box will be shown but will not be functioning unless Redis is setup.


**Steps:**

**0. Initial setup**

If you have Python3 and Pip3 installed you may skip this step.
- Please make sure that you have python 3.6 and pip 9.0.1 by typing `python3 --version` and `pip3 --version` into the command line. If either are not installed please install them. [This](https://www.itsmarttricks.com/how-to-install-python-3-6-on-linux-using-terminal-interface/) tutorial should help. By installing Python3, Pip3 should also be installed.

**1. Installing Django**

Django is the framework that was used to create our project, you will need Django 2.2.7 to run the local server, if you have another version installed it may not work. You can check your version of Django by typing `django-admin.py version` into the command line.
- Download Django by typing `pip3 install Django==2.2.7` into the command line, or consult [this](https://docs.djangoproject.com/en/2.2/topics/install/) tutorial. This process will take a few minutes.

**2. Installing Channels**
- Install Channels by typing `pip3 install -U channels` into the command line, or by consulting [this](https://channels.readthedocs.io/en/latest/installation.html) tutorial. 

**3. Installing Git**

At this point you should have Channels and Django installed. Now we need to install Git. If you already have Git installed, you may skip this step. To check if you already have Git installed, type `git --version`.
- If Git is not installed, install it by following [this](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) tutorial.

**4. Cloning the project**

Once you have Git installed you will clone this project to your system.
- Navigate to a directory on your system (using `cd` on the command line) that you want to clone this project to. Once there, type `git clone https://github.com/Mirandashelt/Capstone.git` to clone our project. If you have trouble with this, consult [this](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) tutorial.
- Now that the project has been cloned, when you type `ls` you should see the `Capstone` directory in your current directory. If you do not see it, you should retry the cloning process and consult the tutorial.
    - Confirm that you are on the master branch by typing `cd Capstone && git checkout`. The following message should be printed: `Your branch is up to date with 'origin/master'.`.
    - If, while using the project or editing it's code, you break it, return to the direcory you cloned the project into by using `cd ..`. When, after typing `ls`, you see the directory `Capstone`, type `rm -rf Capstone` to delete it. Then, reclone it using the steps above.

**5. Starting the server**

Now that you have Django and Channels installed, and the project cloned to your system, you should be able to start a local server.
- Navigate to the directory with the `manage.py` file by typing `cd csc394`. You should be able to see the `manage.py` file displayed by typing `ls`.
- To start the server type `python3 manage.py runserver`. There should be some information printed including the address of the server, usually it is `http://127.0.0.1:8000/` but may be different for you.
    - Keep in mind that you may quit the server at any time by typing `^C` (Control + C) into the command line.

**6. Using the project**

Now you have the local server running and are able to try the project.
- Open a web browser and navigate to the address that was printed out after running the server.

**7. Closing the server**
- When you are finished using the project, return to the command line and type `^C` (Control + C) to close the server.
