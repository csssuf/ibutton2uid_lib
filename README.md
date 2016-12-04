ibutton2uid
===========

Takes a user's iButton and returns their uid. Optionally also takes a url to use
for the actual ibutton2uid operation.

```
james:tmp/ $ source .venv/bin/activate
(.venv) james:tmp/ $ pip install ibutton2uid
Collecting ibutton2uid
  Using cached ibutton2uid-1.0.0-py2.py3-none-any.whl
Collecting requests (from ibutton2uid)
  Using cached requests-2.12.3-py2.py3-none-any.whl
Installing collected packages: requests, ibutton2uid
Successfully installed ibutton2uid-1.0.0 requests-2.12.3
(.venv) james:tmp/ $ python
Python 3.4.5 (default, Nov 30 2016, 17:35:49)
[GCC 5.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from ibutton2uid import ibutton2uid
>>> ibutton2uid("")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/james/projects/tmp/.venv/lib/python3.4/site-packages/ibutton2uid.py", line 6, in ibutton2uid
    raise Exception("Zero or more than one result for iButton %s" % ibutton)
Exception: Zero or more than one result for iButton
>>> ibutton2uid("3D00244B9CCE")
'jmf'
>>>
(.venv) james:tmp/ $
```
