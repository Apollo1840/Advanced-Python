# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:44:01 2018

@author: zouco
"""


str1= 'this is good\nthis is new line'
print(str1)

dir(str1)

# create
this_string = '''dkljglakg:
dgfakdgja
    dfj'gadg'
"jdlfkaj"
'''
print(this_string)  

str2= r'this is good\nthis is new line'
print(str2)


# find
str1.count('t')
str1.index('t')
str1.find('t')

import re
find_all = lambda string,text: [m.start() for m in re.finditer(text, string)]
print(find_all(str1, 't'))

# replace
str1.replace('t','r')

str1.upper()
str1.lower()
str1.title()


# join
print('|'.join(['a','b','c']))
print(''.join(reversed(str1)))
print(str.upper(' '.join(list(str1))))



# re
#########################################################################

# [abc] will match any of the characters a, b, or c; this is the same as [a-c]. 
# If you wanted to match only letters, your RE would be [a-zA-Z].
# [^5] will match any character except '5'
# [\s,.] is a character class that will match any whitespace character, or ',' or '.'
# \d = [0-9]
# \D = [^0-9]
# \s = [ \t\n\r\f\v]
# \S = [^ \t\n\r\f\v]
# \w = [a-zA-Z0-9_]
# \W = [^a-zA-Z0-9_]

# . any character

# * is repeat
# ca*t (any times) matches ct cat caaat caaaat .. 
# ca+t (any times > 0) matches cat caaat caaaat .. 
# ca?t (0 or 1 time) matches ct cat
# [ca?t] = [ca{0,1}t]

import re

p = re.compile('t[a-z]{1,}') # one or more
m = p.match('tempo')

# or 
m = re.match('t[a-z]{1,3}', 'tempo')
bool(m)

if m:
    print('Match found: ', m.group())
    print(m.start())   # must be 0
    print(m.end())
    print(m.span())
else:
    print('No match')

p = re.compile('[A-Z]+')
m = p.search('ZCY goes to ATM to get some EURO.')
print(m.group())

p = re.compile('[A-Z]+')
m = p.search('ZCY goes to ATM to get some EURO.')
print(m.group())

# mulit-level: findall & finditer
p = re.compile('[A-Z]+')
m = p.findall('ZCY goes to ATM to get some EURO.')
print(m)


abbr = re.compile('[A-Z]+')
m = abbr.finditer('ZCY goes to ATM to get some EURO.')
print([(mm.start(),mm.group()) for mm in m])

# regrex:

# | or
# ^ start with
# $ end with
p = re.compile('ed$')
# \A start with (after each \n)
# \Z end with (after each \n)
# \b word boundary
p = re.compile(r'\bclass\b')

# grouping#
p = re.compile('(ab)*')

# level 
p = re.compile('(a(b)c)d')
m = p.match('abcd')
m.groups() # without group(0), in findall, if group exists, group(0) will also be ignore
m.group()
m.group(0)
# 'abcd'
m.group(1)
# 'abc'
m.group(2)
# 'b'
m.group(2,1,2)


# advance
p = re.compile(r'\b(\w+)\s+\1\b')  # \1 means exact(!) things in group1
p.search('Paris in the the spring').group()

re.findall(r'is(.)', str1)
re.findall(r'is(.)(.)', str1)
re.findall(r'is(?:.)(.)', str1)  # non-capture group

# ?P<> is group name
InternalDate = re.compile(r'INTERNALDATE "'
        r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'
        r'(?P<year>[0-9][0-9][0-9][0-9])'
        r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'
        r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'
        r'"')

m.groupdict()



m = re.findall('^a[a-z]{1,3}','abc\nAag\nail', flags=re.M)
m
m = re.findall('a[a-z]{1,3}','abc\nAag\nail', flags=re.I)
m
m = re.findall('.*','abc\nAag\nail', flags=re.S)   # re.DOTALL means dot now present all character
m

# mark!
m = re.search(r'\n','\n\n\n')
m.groups()
m = re.findall(r'\n','\n\n\n')
print(m)





# split
re.split('[,\.\?]','hello, how are you? iam fine, thank you. And you?')
re.split('([,\.\?])','hello, how are you? iam fine, thank you. And you?')

label = re.compile('<[^<>]+>')
content= re.compile('>([^<]+)<')
