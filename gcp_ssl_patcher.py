import os

# Function that tries to read the file
def read_file(path):
    try:
        with open(path, 'r') as file:
            file_data = file.read()
            return file_data
    except:
        print("File not found, please check gcloud cli installation, should be installed for all users in the computer for this script to work")
        input("Press Enter to exit...")
        raise

# Function to replace (disable SSL)
def disable_ssl(file_data):
    file_data = file_data.replace(old_string, new_string,1)
    return file_data

# Function to replace (enable SSL)
def enable_ssl(file_data):
    file_data = file_data.replace(new_string, old_string,1)
    return file_data

# Write the file
def overwrite(file_data):
    try:
        with open(file_path, 'w') as file:
            file.write(file_data)
    except:
        print("Couldn't write file. Are you running as admin?")
        input("Press Enter to exit...")
        raise
        

#Main:

# Path of the file we need to patch, feel free to change if installed elsewhere
file_path = r"C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\lib\third_party\requests\sessions.py"

# substitution it will perform: (only 1 occurence)
old_string = "prep.url, proxies, stream, verify, cert"
new_string = "prep.url, proxies, stream, False, cert"

print("This script will replace gcpcloud cli's source code to disabe SSL verification. Useful if you're having issues with Netskope or other company proxy.")
operation = int(input("Select the desired operation:\n1- Disable SSL verification\n2- Re-enable SSL verification\n"))

if operation == 1:
    file_data = read_file(file_path)
    file_data = disable_ssl(file_data)
    overwrite(file_data)
    print("File patched. Run gcloud again, it should bypass SSL verification from now on.")
elif operation == 2:
    file_data = read_file(file_path)
    file_data = enable_ssl(file_data)
    overwrite(file_data)
    print("SSL verification reactivated.")
else:
    print("Invalid option")

# Persist info on screen
input("Press Enter to exit...")
