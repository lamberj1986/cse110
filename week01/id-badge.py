# Input of the key ID elements
first = input('First Name: ')
last = input('Last Name: ')
email = input('Email Address: ')
phone = input('Phone Number: ')
job_title = input('Job Title: ')
id_num = input('ID Number: ')

#Input for the additional information
hair = input('Hair color: ')
eye = input('Eye color: ')
start_month = input('Start Month: ')
adv_train = input('Advance Training [Y/N]: ')
line = '-'*45
indent = len(start_month) + 5

# Printing out the ID in proper format
print()
print('The ID Card is:')
print()
print(line) 
print(last.upper() + ', ' + first.capitalize())
print(job_title.title())
print('ID: ' + id_num)
print()
print(email.lower())
print(phone)
print()

# Printing out the additional information, using the :<20 to set the 
# minimum space between the two new columns and getting them aligned
print(f"{'Hair: ' + hair:<20}  Eyes: {eye}")
print(f"{'Month: ' + start_month:<20}  Training: {adv_train}")
print(line)