import re
s = "Afganistan, America, Bangladesh, Canada, Denmark, England,Greenland,Iceland,Netherlands,New Zealand,sweden, Switzerland"

li = re.findall(r'(\w+lands*)',s)
print (li)
