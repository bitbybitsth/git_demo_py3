import re
from regular_expression import text

# Metacharacters

# --------------------------
# \d      - Digit (0-9) - searches for numbers 0-9 in the string
# \D      - searches for anything except number -

# pattern = re.compile(r"\d")
#
# # pattern = re.compile(r"192\.\d\d\d\.\d\d\d\.\d\d\d")
# matches = pattern.findall(text)
# print(matches)
# print(len(matches))

#------------------------------------------
#\w   -  Word charcter alphabet (a-z, A-Z,0-9, _)
# #\W   - Not a word charcter
#
# pattern = re.compile(r"\w\w\w\w\w")
# matches = pattern.findall(text)
# print(matches)
# print(len(matches))

"HDFC0002356"

# "\w+@\w+\.\w+" email pattern

# ------------------------
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)


pattern = re.compile(r"\w\w\s\S")
matches = pattern.findall(text)
print(matches)

pattern = re.compile(r"\d\d\d\.\d\d\d\.\d\d\d\d")
matches = pattern.findall(text)
print(matches)

# * o or more
pattern = re.compile(r"M\w*")
match = pattern.findall(text)
print(match)

# + 1 or more
pattern = re.compile(r"M\w+")
match = pattern.findall(text)
print(match)

# ?  zero or 1

pattern = re.compile(r"Mr\w?")
match = pattern.findall(text)
print(match)

# # {num} , exact number
pattern = re.compile(r"H\w{3}000\d{4}")
match = pattern.findall(text)
print(match)

# {n1,n2} number range separated by comma
pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
match = pattern.findall(text)
print(match)


# [] Matches Characters in brackets,  [^] matches charcters not in brackets

pattern = re.compile(r"BBB[a-j][1-4]")  # aaa   abb abc baa bab
match = pattern.findall(text)
print(match)

pattern = re.compile(r"BBB[^a-j]")  # aaa   abb abc baa bab
match = pattern.findall(text)
print(match)


# |   either/or

x = "there is no gain without pain, rain"

pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|H\w{3}000\d{4}")
match = pattern.findall(text)
print(match)

pattern  =re.compile(r"w{3}\.\w+\.\w+")
matches = pattern.findall(text)
print(matches)

text = """The link of this question: https://stackoverflow.com/questions/6038061/regular-expression-to-find-urls-within-a-string
Also there are some urls: www.google.com, facebook.com, http://test.com/method?param=wasd, http://test.com/method?param=wasd&params2=kjhdkjshd
The code below catches all urls in text and returns urls in list."""

urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', text)
print(urls)



