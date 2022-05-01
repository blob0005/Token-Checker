import colorama, requests
colorama.init(autoreset=True)
def token_checker():
	main = input("""
	1. Check 1 Token
	2. Check Tokens In tokens.txt
	> """)
	if main == "2":
		colorama.init(autoreset=True)
		try:
			donetokenlist = []
			print("Loading Tokens...")
			tokens = open("tokens.txt", "r")
			tokenlist = tokens.readlines()
			tokens.close()
			loaded_amount = 0
			for token in tokenlist:
			    donetokenlist.append(token[:-1])
			    loaded_amount = int(loaded_amount) + 1
			print(str(loaded_amount) + " Tokens Loaded, Press Enter To Start")
			input("")
		except Exception:
			print("Unable To Find tokens.txt")
			input("")
			return
		invite_code = "BbXykkqm"
		validtokens = []
		invalidtokens = []
		lockedtokens = []
		totaltoken = 0
		validtoken = 0
		lockedtoken = 0
		invalidtoken = 0
		for token in donetokenlist:
		    while True:
		        r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
		        r1 = str(r1)
		        if "429" not in r1:
		            break
		        if "429" in r1:
		            print(colorama.Fore.YELLOW + "Ratelimited, Retrying")
		    r1 = str(r1)
		    totaltoken = int(totaltoken) + 1
		    if "400" in r1:
		        print(colorama.Fore.RED + "Token Invalid")
		        invalidtokens.append(token)
		        invalidfile = open("invalid_tokens.txt", "a")
		        invalidfile.writelines(token+"\n")
		        invalidfile.close()
		        invalidtoken = int(invalidtoken) + 1
		    if "200" in r1:
		        while True:
		            r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": token})
		            r = str(r)
		            if "429" not in r:
		                break
		            if "429" in r:
		                print(colorama.Fore.YELLOW + "Ratelimited, Retrying")
		        r = str(r)
		        if "200" in r:
		            print(colorama.Fore.GREEN + "Token Valid")
		            validtokens.append(token)
		            validfile = open("valid_tokens.txt", "a")
		            validfile.writelines(token+"\n")
		            validfile.close()
		            validtoken = int(validtoken) + 1
		        if "403" in r:
		            print(colorama.Fore.RED + "Token Locked")
		            lockedtokens.append(token)
		            lockedfile = open("locked_tokens.txt", "a")
		            lockedfile.writelines(token+"\n")
		            lockedfile.close()
		            lockedtoken = int(lockedtoken) + 1
		print("\n\nStats:\n")
		print("Total Checked: " + str(totaltoken))
		print("Total Valid: " +  str(validtoken))
		print("Total Invalid: " +  str(invalidtoken))
		print("Total Locked: " +  str(lockedtoken))
		input("")
		return
	if main == "1":
		while True:
			tokens = input("Enter Token: ")
			r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
			if "200" not in str(r1):
				print(colorama.Fore.RED + "Invalid")
			if "200" in str(r1):
				r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
				if "200" in str(r):
					print(colorama.Fore.GREEN + "Valid")
				if "403" in str(r):
					print(colorama.Fore.YELLOW + "Locked")
			while True:
				main2 = input("Wanna Check Another Token, y/n: ")
				if main2 == "y" or main2 == "n":
					break
				else:
					print("Enter A Valid Choice")
			if main2 == "n":
				return
token_checker()
