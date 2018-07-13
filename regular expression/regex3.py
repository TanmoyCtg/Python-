import re
		    
s = "ABCD -1234 -2221"
result = re.sub(r'\d','0',s)		    
print(result) 
# output: ABCD -0000 -0000

>>> s = "22/07/2017, 20/01/2017, 01/01/2018"
		    
>>> new_s = re.sub(r'(\d{2})/(\d{2})/(\d{4})',r'\3-\2-\1',s)
		    
>>> new_s
		    
'2017-07-22, 2017-01-20, 2018-01-01'


