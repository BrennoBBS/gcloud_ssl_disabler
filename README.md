# gcloud_ssl_disabler

This script will replace gcloud cli's source code to disabe SSL verification. Useful if you're having issues with Netskope or other company proxy while installing gcloud cli or running gcloud commands. It also offers the option to undo the changes and re-enable SSL verification.

Use this at your own risk!

SSL verification is strongly advised, but sometimes nothing else works ¯\_(ツ)_/¯

This just automates the steps described here: https://stackoverflow.com/questions/70795283/installing-google-cloud-sdk-using-windows-ssl-error
All credits to the person who answered it.

I'm assuming you have python installed and that you're using Windows.

**HOW TO USE? (SSL error during installation)**

1- After the installation fails, click on close

2- Download the executable OR Download the .bat and the .py file from this git in the same folder

3- Run the .exe OR .bat file as administrator, select option 1

4- Go to C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk and run install.bat as admin

5- Profit


**HOW TO USE? (Error running commands after installing gcloud cli)**

1- Download the executable OR Download the .bat and the .py file in the same folder

2- Run the .exe OR .bat file as administrator, select option 1

3- Profit
