import requests

url1=" http://13.127.155.43/api_v0.1/sending"

d={}

for i in ["Phone_Number","Name","College_Name","Branch"]:
    d[i] = raw_input("Enter "+i+": ")

 
r= requests.post(url=url1,json=d) 


t=r.text
print t
   

ph_no=raw_input("enter phone no: ")
url2="http://13.127.155.43/api_v0.1/receiving?Phone_Number={0}".format(ph_no)


resp=requests.get(url=url2)
c=resp.json()
print c



