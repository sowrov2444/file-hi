s="Afganistan,America,Bangladesh,Canada,Denmark,Eangland,Greenland,Iaceland,Natherland,Nethrlands,New zealand"
countries=s.split(",")
print(countries)
li=[item for item in countries if item.endswith("land")]
print(li)
li=[item for item in countries if item.endswith("land") or item.endswith("lands")]
print(li)

import re
s="Afganistan,America,Bangladesh,Canada,Denmark,Eangland,Greenland,Iaceland,Natherland,Nethrlands,New zealand"
li=re.findall(r'(\w+lands*)',s)
print(li)

import re
match=re.search("Bangla","Bangladesh")
print(match)
print(match.group())
match=re.search("desh","Bangladesh")
print(match.group())
match=re.search("des","Bangladesh")
print(match.group())
matche=re.search("dets","Bangladesh")#matching na hoile none dekhabe
#print(matche.group())#vul lekhle eita lekhle error asbe
print(matche)
print(type(matche))

import re
s="Bangladesh"
match=re.search(".",s)
print(match.group())
match=re.search("B.n",s)
print(match.group())
match=re.search("B.n...",s)
print(match.group())
s="Bangladesh is our homland"
match=re.search("............",s)
print(match.group())
s="Bangladesh is our homland"
match=re.search("o\w\w",s)
print(match.group())
match=re.search("i\w\w",s)#vul lekhle none ashe
print(match)
s="Bangladesh is our homland"
match=re.search("l\w+h",s)
print(match.group())
match=re.search("B.+u",s)#jot dur porjonto u ache toto dur jabe
print(match.group())
match=re.search("B.+?s",s)#first s porjonto jae
print(match.group())

text="Phon number: 01885867015."
match=re.search("\d+",text)#digit er jonno \d+ dite hoi
print(match.group())
text="house number:5,phon number:01885867015."
match=re.search("\d+",text)#first 5 asbe
print(match.group())
match=re.search("\d{11}",text)#joto gula number thakbe toto gula
print(match.group())
text="house number:5,phon number:018 85867015."#judi space thake
match=re.search("\d{3}\s*\d{8}",text)
print(match.group())

#multiple number ber korte
test="multiple phon number,01773256748,01398763439,01933593866,00000000000,123-123"
number=re.findall(r"\d{3}\s*\d{8}",test)#sob 11 digit asbe
print(number)
number=re.findall(r"01\s*\d{8}",test)#nidristo kore bole diyar jonno
print(number)

#ragular expecion
s="Bangla english bangla"
fi=re.findall(r"english",s)
print(fi)
fi=re.findall(r"^english",s)
print(fi)
fi=re.findall(r"english$",s)
print(fi)
fi=re.findall(r"^Bangla",s)
print(fi)
ri=re.findall(r"bangla$",s)
print(ri)
s="Bangla english Bangla"
fi=re.findall(r"bangla$",s)
print(fi)
fi=re.findall(r"bangla$",s,re.IGNORECASE)
print(fi)
fi=re.findall(r"bangla$",s,re.I)
print(fi)

with open("file.text","r")as f:
    text=f.read()
print(text)

import re
fi=re.findall(r"^.*?$",text)
print(fi)
fi=re.findall(r"^.*?$",text,re.MULTILINE)#.ba * er bodol+ dile faka gula asbe na#Multiline ke M bola jai
print(fi)

s="<li>Sowrov</li><li>Shakib</li><li>Mahmudullah</li><li>Momin</li>"
result=re.findall(r"<li>(.*?)</li>",s)#jei gula bat dibo oigula
print(result)


