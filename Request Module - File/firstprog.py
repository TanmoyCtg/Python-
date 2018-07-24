import requests as r

url = "http://subeen.com/allposts"
response = r.get(url)
print (response)

# what type it is
print (type(response))
#requests package models module Response class object.
# what is the attribute of response object

print (dir(response))

print (response.ok)
print(response.status_code)
print(response.reason)
print(response.encoding)
print (response.json)

# now get the html text
# grab the url, use the text

res = r.get("http://example.com")
print (res.ok)

getHtmlText = res.text

#what type getHtmlText is ?

print (type(getHtmlText))

print (getHtmlText)

fp = open ("html.txt","w")
# write in the file
fileWrite = fp.write("This file was created using python")
#close file

fp.close()

print(type(fileWrite))
print (fp)
