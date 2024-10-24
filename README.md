# gcloud_ssl_disabler
This script will replace gcpcloud cli's source code to disabe SSL verification. Useful if you're having issues with Netskope or other company proxy. It also offers the option to undo the changes and re-enable SSL verification.

USE THIS AT YOUR OWN RISK!

SSL verification is strongly advised, but sometimes nothing else works ¯\_(ツ)_/¯

This just automates the steps described in this article: https://stackoverflow.com/questions/70795283/installing-google-cloud-sdk-using-windows-ssl-error
All credits to the person who answered it.

HOW TO USE? (SSL error during installation)

1- After the installation fails, click on close

2- Download the executable OR Donwload the .bat and the .py file in the same folder

3- Run the .exe OR .bat file as administrator, patch the file (option 1)

4- Go to C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk and run install.bat as admin

5- Profit

HOW TO USE? (Error after installing gcloud cli)

1- I'm assuming you have python and gcloud cli installed, also that you're using Windows

2- Download the executable OR Donwload the .bat and the .py file in the same folder

3- Run the .exe OR .bat file as administrator, patch the file (option 1)

4- Profit
