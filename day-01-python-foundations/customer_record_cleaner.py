#Program to clean the data

#input
raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "


#Cleaning
clean_name=raw_name.strip().title()
clean_city=raw_city.strip().title()
clean_age=int(raw_age.strip())
clean_email=raw_email.strip().lower()
status="Adult" if clean_age >=18 else "Minor"

#Output
print(f'''Name: {clean_name}
City: {clean_city}
Age: {clean_age}
Email: {clean_email}
Status: {status}
''')