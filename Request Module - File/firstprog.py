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
