# Flask quickstarter guide
####Below you can find the post that was made together with this project for the beginner track of the *Google Challenge Scholarship: Front-End Web Dev*.

**Hi everybody**

Earlier this week [I finished building my first Front/Back-end project](http://130.204.57.83:3126/) from scratch, and shared it in [this post](https://discussions.udacity.com/t/ive-just-built-my-first-webapp-front-and-back-end-from-scratch/507317). You guys were really super nice and supportive. Thank you so much for that! :)

I believe that the most valuable part of that project was everything that I learned in the process, and in this post I'll try to share a bit of exactly that. 

Following up on some of your requests: [here is the full code for the project](https://github.com/kepelrs/personal_finance), and below you will find my 5 minute guide for how to host your own starting pages easily.

**For this guide you will not need to have any more knowledge than what the course has provided.** But please keep in mind that this will be basic, and in order to build a more serious back end, you will need to go on learning more about the back end language of your choice. 

By the end of this guide you will be able to **host your pages from your own computer and internet using Python.** As a bonus there are a couple of back end starter samples at the end of this guide.

I hope you have as much fun as I had with this, and may it be just as insightful to you as it was for me!
    
**TL;DR**

1. Install the requirements.
2. Download the [Project Folder](https://github.com/kepelrs/flask_quickstart/archive/master.zip) from GitHub.
3. Replace the files in the folder with your own files.
4. Share the link with your friends.

**Installing requirements**

_Install Python_

 - Download and install the latest version of Python 3 here: https://www.python.org/downloads/
       *(During the instalation, make sure you have checked the box "add Python to PATH".)*

_Install Flask_

 - After Python, [open an administrator command prompt](https://www.google.bg/search?q=how+to+open+admin+command+prompt), and install Flask by typing:
       >pip install flask

_Get ngrok (no installation required)_

 - Download ngrok and save it somewhere: https://ngrok.com/download/
       1. *To keep this guide easy for everyone we will use ngrok. It's great, it's free and no installation is required.*  
       2. *With ngrok you won't need to configure any port forwarding on your router or waste time setting up dynamic DNS solutions.*
       3. *If you still would like to know how to setup the port forwarding manually [click
   here](http://www.noip.com/support/knowledgebase/general-port-forwarding-guide/).*

**Replace files**

In the _short_guide_ folder, replace the files **/templates/index.html**, **/static/app.js** and **/static/styles.css** with your own files. Make sure that you have correctly set up the paths in your own html file with: 

    <head>
    <script src="../static/app.js"></script>
    <link rel="stylesheet" type="text/css" href="../static/styles.css">
    </head>
(You can copy paste this into your own html file.)


**Serve your own files!**

To start serving your own files, download the project folder [here](https://github.com/kepelrs/flask_quickstart/archive/master.zip) if you haven't already and unzip it:

1. Run your flask app by opening a command prompt, [navigate to](https://www.colorado.edu/geography/gcraft/tips/doshelp.html#dir) your *"/short_guide"* folder and type "python myWebApp.py". 
2. Open the ngrok.exe file that you downloaded earlier and type "ngrok.exe http 3126". Copy the *http* or *https* link under "*Forwarding*" and share it with friends, family, and our community,! :)

**Done!**

The short version of this guide ends here, but if you want to see a bit more of back end interaction:


 - I have included the file [*"longer_version.zip"*](https://github.com/kepelrs/flask_quickstart/blob/master/longer_version.zip) in the GitHub folder.
*This project allows your page to interact with the "posts.txt" file in your computer. It's the same "short_guide" but adding two simple methods (save and load)* . *There are comments explaining everything.*
 
 - If you wish to see my beginner attempt at building a back end with databases, login systems and etc you can find the full code for my [personal_finance project here](https://github.com/kepelrs/personal_finance).

If you want to keep going from here you will need to learn more about Python. It's a great and fun language, and I highly recommend it! :)

I'm running late for work! I hope you find this useful, and let me know what you think! ;)
Big hug!
Davi