# LEARNING BASICS OF REGEX
print("\tPradhans")                 # This one puts a tab
print(r"\tPradhans")                # Raw String : Converts everything into a string

text_to_search = """Log Date: 2026-06-26T07:35:12Z | Server ID: SRV-8842-AX
------------------------------------------------------
User alice_smith99@company.com logged in from IP 192.168.1.45 at 07:30:15.
She visited the billing portal: https://billing.company.com/invoice/INV-2026-004
Payment of $1,250.45 was processed successfully. 
Alternative contact: (555) 019-2834 or via email at support-desk@company.co.uk.

Error Code: 404 [Not Found] occurred at https://company.com/blog/regex-basics
Referrer IP: 10.0.0.254. Date occurred: 25/06/2026.
Database connection timed out for db_user_admin@prod-db.internal.net.
Contact database admin at +1-800-555-0199 ext. 423.

Transaction log:
- Item #4928: Laptop - $999.00 (Ordered by bob.jones@domain.org)
- Item #1042: Mouse - €25.50 (Ordered by charlie.brown+test@gmail.com)
- Item #8821: Keyboard - £85.00
Invalid emails found in database dumps: "invalid-email@", "@domain.com", "john.doe@domain..com".
Special Code: [ABC_123_XYZ] and [999_ERR_555]."""



import re
pattern = re.compile(r"user")           # case sensitive

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

print(text_to_search[565:569])

print("---------------------------------------------")

text = "Item #4928 costs $999, but mouse #1042 is only €25."


print(re.search(r'\d', text))         # Prints the first occuring of the integers
print(re.findall(r'\d', text))        # Prints (in list format) all the numbers used in the string
print(re.findall(r'\d.', text))       # Prints all the numbers and their next letter by one index (coz only one "." is used)
print(re.search(r'\d+', text))
print(re.findall(r'\d+', text))        # Prints the entire nums (not by printing one int at a time)

print("---------------------------------------------")

temp = "Ha HaHa abcHade Ha efHa"
print(re.findall(r"\bHa", temp))                    # Only finds words from the beginning of the letters
print(re.findall(r"\bItem", text_to_search))        # Searching for the word "Item"





