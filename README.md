# gcloud_ssl_disabler
This script will replace gcpcloud cli's source code to disabe SSL verification. Useful if you're having issues with Netskope or other company proxy. It also offers the option to undo the changes and re-enable SSL verification.

USE THIS AT YOUR OWN RISK!

SSL verification is strongly advised, but sometimes nothing else works ¯\_(ツ)_/¯

This just automates the steps described in this article: https://stackoverflow.com/questions/70795283/installing-google-cloud-sdk-using-windows-ssl-error
All credits to the person who answered it.

HOW TO USE?

1- I'm assuming you have python and gcloud cli installed, also that you're using Windows

2- Save the .bat and the .py file in a folder

3- Run the .bat file as administrator

4- Profit
