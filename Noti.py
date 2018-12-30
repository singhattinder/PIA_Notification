import requests
import commands
import os

def notify(title, text):
    os.system("""
        osascript -e 'display notification "{}" with title "{}"'
        """.format(text, title))

s = commands.getstatusoutput('head -n 100 /dev/urandom | shasum -a 256 | tr -d " -"')

URL = "http://209.222.18.222:2000/?client_id=" + s[1]

try:
    r = requests.get(URL)
    json = r.json()
    s = json['port']
    p = "port: " + str(s) + ", added to clipboard"
    os.system("echo '%s' | pbcopy" % s)
    notify("PIA port forward", p)

except:
    notify("PIA fetch Error", "Already activated or not supported region")
