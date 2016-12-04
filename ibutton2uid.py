import requests
def ibutton2uid(ibutton, url="http://ibutton2uid.app.csh.rit.edu/"):
    r = requests.get(url + ibutton)
    if r.status_code == 200:
        return r.text
    raise Exception("Zero or more than one result for iButton %s" % ibutton)
