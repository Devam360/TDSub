import re
pattern= "ballapp"
if re.match('app',pattern):
    print("True")
else:
    print("False")
#print(re.findall('p',pattern))
if re.search('lap',pattern, flags=0) :
    print("True")
else:
    print("False")
print(re.findall('lap',pattern, flags=0))

string= "Devam Sarin"
pattern=" "
nstr= re.sub(pattern,"RKM",string, count=0, flags=0)
print(nstr)

string="Itgg ag dog"
pattern="g$"
print(re.findall(pattern,string,flags=0))
string="ItII aI doI"
pattern="^I"
print(re.findall(pattern,string,flags=0))
string="It's a dog"
pattern="^I...."
print(re.findall(pattern,string,flags=0))
string="It's a dog"
pattern="...g$"
print(re.findall(pattern,string,flags=0))
string="It's a dog 56"
pattern="\d"
print(re.findall(pattern,string,flags=0)) #5, 6
string="56's 3 2o5"
pattern="\D"
print(re.findall(pattern,string,flags=0))
string="It's a dog"
pattern="\s"
print(re.findall(pattern,string,flags=0))
string="It's a dog"
pattern="\S"
print(re.findall(pattern,string,flags=0))
string="It's a dog"
pattern="\s"
print(re.findall(pattern,string,flags=0))
string="call aunty na"
pattern="au*"
print(re.findall(pattern,string,flags=0))
string="call aunty na"
pattern="au"
print(re.findall(pattern,string,flags=0))


