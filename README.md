# iconographic


# Release Update - April 20, 2018

**Features**

● Content of End-User Licensing Agreements (EULA) displayed through icons
● User can download the analysis summary of EULA
● Admin functionality of changing icon names, descriptions, and images
● Displays the analysis of the most popular EULAs
● New admin accounts can be added
● User has ability to submit report if error is encountered somewhere in the site
● Summary of the meaning of icons listed at the top of the results page

**Bug Fixes**

● Status of issue shown; resolved issues cannot resolved for a second time (error prevention)
● Database error message parsed to give user clear indication of encountered problem
● Accepted file input types now includes .pdf,.doc,.txt
● Implemented session persistence so admin stays logged in even if they navigate to new page

**Known Bugs**

● When another user tries to analyze an EULA while the first user is on the results page, the download a
summary button will download the results of the second user’s result
● Only docx files can be analyzed on the tool; older versions of word documents will not work for analysis
● When resolving an issue, sometimes the issue will not disappear immediately. If this should happen, refresh
the page and the resolved issue should disappear
● When reading in EULA for analysis either through file or plain text, some of the characters will be changed
due to unicode errors
● If a user reports an issue from the results page, it will redirect the user to the “Input an EULA” page


# Install Guide:

● ​ **Pre-requisites:** ​ what is the required configuration of software and hardware that the customer must
have before they can begin the installation process?
```
1 ) Using a windows computer for the installation process is HIGHLY recommended
2 ) Install the latest version of Python 3
https://www.python.org/downloads/
```
● ​ **Dependent libraries that must be installed:** ​ what third party software must be installed for your
       software to function?
```
1 ) Install Swig from
https://sourceforge.net/projects/swig/files/swigwin/swigwin- 3. 0. 12 /swigwin- 3. 0. 12 .zip/download
?use_mirror=superb-dca 2 ​ and add to path environment variable. In order to do this, search for
path variables in your computer’s search bar. From there, enter the “edit environment variables
for your account. Add the local path to swig’s bin folder to the path variables.
2 ) Install dependencies
Click on the “Install Dependencies.bat” file to install the dependencies.
```
● ​ **Download instructions:** ​ how will the customer and users get access to the project?
```
1 ) Navigate to the REUL Labs Github account and clone/download the iconographic repository.
```
● ​ **Build**
```
1 ) No build necessary.
```
●  **Installation of actual application:** ​what steps have to be taken after the software is built? What
      directories are required for installation?
```
1 ) Run flask
Contact your web server admin for instructions on how to connect the site to a domain. Then, on
the server machine, once everything is set up, click on run.bat
```
● ​ **Run instructions:** ​ what does the user/customer have to do to get the software to execute?

```
1 ) Adding data to the neural network
In order to add more data to the neural network, you first need to add data to the csv file named
‘traindata.csv’. Scroll down to the first empty row and start entering the data from there. The first
column should be the text. The second column will be the icon number that corresponds with the
list that the REUL Lab provided us. This must be a number between 0 and 32 with 0 being ‘No
Icon’ and 32 being the last icon on the list. If any number over 32 or under 0 is entered, the
retraining process will throw an error. The last column is the company that the EULA came from.
Once all the data is entered, click on the RetrainClassifier.bat file. This will change the neural
network and the changes will be present immediately.
```
● ​ **Troubleshooting:** ​what are common errors that occur during installation and what is the corrective
       action?
```
1 ) Problems with adding data to the neural network
Sometimes, the neural network, when being retrained will throw an error. This error will claim
that there was a problem with unicode. After clicking the RetrainClassifier.bat, if the command
line window closes quickly without displaying anything, it is very likely this error occurred. To
verify this, open up a command line terminal and navigate to the file that TrainClassifier.py is
located in. Then run the command python TrainClassifier.py (if you renamed the python 3
executable file use the name that it currently is). In order to resolve this, you must take out all
hyperlinks and special characters (i.e. ™, ©). If this still does not work, upload the csv to google
drive and then re download it. This will work because google drive will encode and decode the
file using its own algorithm that the tool will be able to read.If it continues to not work, delete the
data.
```

