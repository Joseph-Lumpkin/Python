import pyperclip as pc, re


#Phone number regex
phoneRegex = re.compile(r'''(
		(\d{3}|\(\d{3}\))? 	 	 	 	# area code
		(\s|-|\.)? 	 	 	 	 	 	# separator
		(\d{3}) 	 	 	 	 	 	# first 3 digits
		(\s|-|\.)? 	 	 	 	 	 	# separator
		(\d{4}) 	 	  	 	 	 	# last 4 digits
		(\s*(ext|x|ext.)\s*(\d{2,5}))? 	# extension
		)''', re.VERBOSE)


#Email regex
emailRegex = re.compile(r'''(
		[a-zA-Z0-9._%+-]+ 	 	# Username
		@ 	 	 	 	 	 	# @ symbol
		[a-zA-Z0-9.-]+ 	 	 	# Domain name
		(\.[a-zA-Z]{2,4}) 	 	# Top level domain
		)''', re.VERBOSE)

#Establishing variables
text = str(pc.paste())
matches = []

#Add the found phone numbers to the matches list.
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)

#Add the ound emails to the matches list.
for groups in emailRegex.findall(text):
	matches.append(groups[0])

#Copy the results to the clipboard.
if len(matches) > 0:
	pc.copy('\n'.join(matches))
	print('Copied to the clipboard: ')
	print('\n'.join(matches))
	
else:
	print('No phone numbers or email addresses were found.')