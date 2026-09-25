Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #count()
>>> a="twinkle twinkle litter star"
>>> a.count("twinkle")
2
>>> #find a sring
>>> a="python"
>>> a[3]
'h'
>>> a.find("h")
3
>>> b="hello"
>>> b.find("l")
2
>>> b.find("h")
0
>>> #escape sequences
>>> #|n->new line
>>> #|t->tab space
>>> a="name:Akmal|nmobile no:7601022094|tcity:Hyderabad"
>>> print(a)
name:Akmal|nmobile no:7601022094|tcity:Hyderabad
>>> #replace
>>> a="wait until you succeed"
>>> a.replace("wait","work")
'work until you succeed'
>>> b="python and ml"
>>> b.replace("ml","ai")
'python and ai'
