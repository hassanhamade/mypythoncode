import requests, time
r=requests.post('http://requestb.in/1mi3ysg1', data={"SUPER TETA":time.time()})
print (r.status_code)
print (r.content)
