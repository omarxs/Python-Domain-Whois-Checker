# Simple Domain Whois Checker (Python)

This python script checks the information of domains listed in a text file called 'domains.txt'. If the file doesn't exist, the script will ask the user to create it.

## Required Dependencies

The following dependency must be installed prior to running this script:

`sudo apt-get install python3-whois`


## Usage

To run the script, navigate to the directory containing the script and run the following command:

`python3 domains.py`


## Output

The script will print the following information for each domain listed in the 'domains.txt' file:

Domain Name:
Domain Registrar:
Creation Date:
Expiry Date:
Nameservers:


## Sample 'domains.txt' file

example1.com
example2.net
example3.org


Note: Please ensure that each domain name is listed on a separate line in the 'domains.txt' file.