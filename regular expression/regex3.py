import re
		    
s = "ABCD -1234 -2221"
result = re.sub(r'\d','0',s)		    
print(result) 
# output: ABCD -0000 -0000
