import subprocess
import re
from colorama import init, Fore

# Initialize colorama
init()

# Define the path to the text file containing JS endpoints
js_endpoints_file = 'jsfiles.txt'

# Define the keyword pattern to search for
keyword_pattern = r'aws_access_key|aws_secret_key|api key|passwd|pwd|heroku|slack|firebase|swagger|aws_secret_key|aws key|password|ftp password|jdbc|db|sql|secret jet|config|admin|pwd|json|gcp|htaccess|.env|ssh key|.git|access key|secret token|oauth_token|oauth_token_secret'

# Create a function to print colored text
def print_in_red(text):
    print(f"{Fore.RED}{text}{Fore.RESET}")

def print_in_green(text):
    print(f"{Fore.GREEN}{text}{Fore.RESET}")

# Read the JS endpoints from the text file
with open(js_endpoints_file, 'r') as file:
    js_endpoints = file.read().splitlines()

# Loop through each JS endpoint and search for keywords
for endpoint in js_endpoints:
    print(f"Analyzing {endpoint} ...")
    
    # Make a cURL request to the JS endpoint and capture the response
    try:
        response = subprocess.check_output(['curl', '-s', endpoint]).decode('utf-8')
    except subprocess.CalledProcessError:
        response = ''
    
    # Search for keywords in the response
    matches = re.findall(keyword_pattern, response, re.IGNORECASE)
    
    # If matches are found, print them in green color
    if matches:
        print_in_red(f"Found matches in {endpoint}:")
        for match in matches:
            print_in_green(match)
        print()

# Print the completion message in red
print_in_red("Hey Hacker, My Work Here Is Done. Feel Free To Run Me Again")
