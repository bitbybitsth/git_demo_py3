import re

text = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
4567812390
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
192.122.100.300
192*122*100.300

10+20+30
45+50+60
90*45*1245
89*10*45

68.3.212.55
1.2.3.67
10.23.4.78
321-555-4321
123.555.1234
123*555*1234
123755571234
800-xxx-1234
900$555$1234
Mr_ Schafer
MrMmith
Ms Davis
Mrs. Robinson
MrT
Mr
M
Mrtu
1234567890
BBBa23
BBBb5678
BBB1
BBBa15655
BBBb145
BBB*
BBBp
BBBf
BBB4
BBB6
BBB3
BBBb
pain

bitbybitsth@gmail.com

abc
aaa
bbb
ccc
ccd
bac
cab
acb
bca
www.example.com
www.sample.com
www.e.com
cba
HDFC0003456
'''

pattern = re.compile("abc")
print(type(pattern))

#-----------------------------------------
# findinter returns an interator object of the pattern matches from the provided string.
# we can iterate over it to get more info

# matches = pattern.finditer(text)
# matches = pattern.finditer(text, endpos=8)
# matches = pattern.finditer(text, pos=50)
# matches = pattern.finditer(text, endpos=100, pos=10)

# matches = re.finditer(pattern, text)

# for match in matches:
#     print(match)
#     print(match.span())
#     print(match.end())
#     print(match.start())
#     print(match.string)

#-----------------------------------------
# findall - it return the list of all matches

# matches = pattern.findall(text)
# matches = pattern.findall(text,pos=50)
# matches = pattern.findall(text, endpos=50)
# matches = pattern.findall(text, pos=10, endpos=100)

# matches = re.findall(pattern, text)
# print(matches)

# -----------------------------------------
# search, return the first match object if found else None

# match = pattern.search(text)
# match = pattern.search(text, pos=50)
# match = pattern.search(text, endpos=50)
# match = pattern.search(text, pos=10, endpos=200)
# print(match)


#------------------------------------
# split - splits the text with given pattern

# splited_text = pattern.split(text)
# print(splited_text)