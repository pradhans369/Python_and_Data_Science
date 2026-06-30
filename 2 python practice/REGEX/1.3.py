import re

temp = """
Mr. kashMr.fiuhe
Mr fasdhf
Mrs sfjoijdsoif
Mrs. ashdfius

"""

print(re.findall(r'Mr\.?\S',temp))








