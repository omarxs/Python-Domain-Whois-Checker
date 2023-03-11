import whois


def domainCheck(domainX):

	domain = whois.query(domainX)


	print("================ "+domain.name.upper()+" ================")
	print("")
	print("DOMAIN NAME: " + domain.name.upper())
	print("-------------------------------------------")
	print("DOMAIN REGISTRAR: " + domain.registrar)
	print("-------------------------------------------")	
	print("CREATION DATE: " + str(domain.creation_date))
	print("-------------------------------------------")
	print("EXPIRY DATE: " + str(domain.expiration_date))
	print("-------------------------------------------")
	print("NAMESERVERS: " + str(domain.name_servers))
	print("")
	print("===========================================")
	print("")

def fileHandler():
	f = open('domains.txt', 'r')
	for line in f:
		try:
			domainCheck(line)
		except Exception:
			print("NOT A VALID DOMAIN: "+ line)
	f.close()


def fileCreator(numberOfLines):
	file = open("domains.txt", "w")
	for line in range(0, numberOfLines):
		file.write(input("Please enter a valid domain.. ")+"\n")
	print("Thank you! domains.txt has been created successfully.. ")
	file.close()



try:
	fileHandler()

except Exception:
	print("You don't have a domains file..")
	x = input("Wanna create one? y/n ")
	if(x=="y"):
		number = int(input("Please enter number of domains.. "))
		fileCreator(number)
		fileHandler()
	else:
		print("Goodbye!")




