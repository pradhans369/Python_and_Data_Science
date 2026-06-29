temp = """Log Date: 2026-06-26T07:35:12Z | Server ID: SRV-8842-AX
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

print(re.findall(r"Log", temp))       # searching for the word "Log" anywhere in the string
print(re.findall(r"^Log", temp))      # searches for the word "Log" at the start of the string
print(re.findall(r"Log$", temp))      # searches for word "Log" at the end of the string

print(re.findall(r".$", temp))
print("---------------------------------------------------")


temp = """
202-555-0143
555-0199
703 555 0182
(202) 555-0174
(800) 555-0112
+1-202-555-0156
+1 (301) 555-0122
1-800-555-0199
202 555 0109
202.555.0109
3015550134
202-555-0148 ext. 941
(800) 555-0133 x42
!@#$%^&*()
"""


print(re.findall(r"\d\d\d", temp))                  # will the print all the numbers with 3 digits in it (as there are 3 "\d" has beed used)
print(re.findall(r"\d{4}", temp))                   # Same as above ("")

print(re.findall(r"\D", temp))                      # printing all the letters which are not digits

print("---------------------------------------------------")

print(re.findall(r"\d{3}-\d{3}-\d{4}", temp))
print(re.findall(r"\d{3} \d{3} \d{4}", temp))
print(re.findall(r"[^\w\s]", temp))                 # something that prints all the  "Special Characters" (Punctuation, symbols, math signs, but NOT letters/numbers) used in the string | BUT THIS IS NOT ABLE TO REOVE UNDERSCORES (_)

print("---------------------------------------------------")
print(re.sub(r"[^\w\s]", " ", temp))                 # replacing all the  "Special Characters" (Punctuation, symbols, math signs, but NOT letters/numbers) with space
print("---------------------------------------------------")

print(re.findall(r'[^\d]',temp))

print(re.findall(r"\d{3}.\d{3}.\d{4}", temp))           # matches any special chars btwn the digits
# In Regex, the dot . is a wildcard character that means "match absolutely any character here" (except a newline).
# Because it is a wildcard, it will match whatever separator is placed between the numbers—whether it is a dash, a space, a literal dot, or even a letter.
print(re.findall(r"\d{3}\.\d{3}\.\d{4}", temp))         # matches the dot exactly           
