import re

text = "Email your feedback here: book@subeen.com py.book@subeen.com book"
text1 = "book at subeen.com, book At subeen.com, book(at) subeen dot com, book [at] subeen [dot] com"
text1_result = re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+','@',text1, flags=re.I)
result = re.findall(r'(\w+@\w+[.]\w+)',text)
print (result)

print(text1_result)
