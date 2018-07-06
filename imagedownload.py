import requests

url = "https://static.makeuseof.com/wp-content/uploads/2018/03/python-faq-670x335.jpg"
r = requests.get(url)

with open("pyboo1.png","wb") as f:
    f.write(r.content)
    
