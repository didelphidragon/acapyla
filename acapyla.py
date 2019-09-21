import requests
import string
import urllib
import random
import json
import sys

quote = sys.argv[1]
print(quote)
try:
    voiceid = "enu_" + sys.argv[2] + "_22k_ns.bvcu"
except IndexError:
    voiceid = "enu_willfromafar_22k_ns.bvcu"
letters = string.ascii_lowercase
premail = ''.join(random.choice(letters) for i in range(64))
email = premail + "@gmail.com"
print("Email string: " + email)
noncerl = "https://acapelavoices.acapela-group.com/index/getnonce/"
noncedata = {'googleid':email}
noncer = requests.post(url = noncerl, data = noncedata)
nonce = noncer.text[10:50]
synthrl = "http://www.acapela-group.com:8080/webservices/1-34-01-Mobility/Synthesizer"
synthdata = "req_voice=" + voiceid + "&cl_pwd=&cl_vers=1-30&req_echo=ON&cl_login=AcapelaGroup&req_comment=%7B%22nonce%22%3A%22" + nonce + "%22%2C%22user%22%3A%22" + email + "%22%7D&req_text=" + quote + "&cl_env=ACAPELA_VOICES&prot_vers=2&cl_app=AcapelaGroup_WebDemo_Android"
headers = {'content-type': 'application/x-www-form-urlencoded'}
synthr = requests.post(url = synthrl, data = synthdata, headers = headers)
minuspre = synthr.text[synthr.text.find('http://'):]
minussuf = minuspre.split(".mp3", 1)[0]
synthresult = minussuf + ".mp3"
urllib.request.urlretrieve(synthresult, quote + ".mp3")