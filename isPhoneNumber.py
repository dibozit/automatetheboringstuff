def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('moshi moshi is a phone number:')
print(isPhoneNumber('moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found:' + chunk)
print('Done')

#isPhoneNumber() works for regular expressions but fails when it comes to xxx.xxx.xxxx versions or numbers with
# extensions like 415-555-4242 x99.
# REGULAR EXPRESSIONS (regexes) are descriptions for a pattern or a text.
# \d stands for a digit character (any single numeral 0 to 9
# \d\d\d-\d\d\d-\d\d\d\d is same with isPhoneNumber()
# adding {3} after a pattern means 'match this pattern three times
# \d{3}-\d{3}-\d{4}

import re

#Passing raw string to re.compile() : \ normalde escape character yaratmak için kullanılır. örn: \t = tab,
# \n = new line, \r = carriage return. Bu sebeple biz raw string kullanıyoruz burada: Python raw string is created by prefixing a string literal with ‘r’ or ‘R’. Python raw string treats backslash (\) as a literal character. This is useful when we want to have a string that contains backslash and don’t want it to be treated as an escape character.

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #r' > bunu yaparak raw string yapmış oluyoruz
matchingObject = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: '+ matchingObject.group()) #group> return a string of the actual matched text

#https://www.regexpal.com > bu sitede de direkt metni yapıştırıp aradığın keyword'ü buldurabiliyormuşsun

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo= phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1)) #415
print(mo.group(2)) #555-4242
print(mo.group(0)) #415-555-4242
print(mo.group()) #415-555-4242
print(mo.groups()) #('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode) #415
print(mainNumber) #555-4242

#eğer fazladan karaker varsa kurtulmam gereken, o zaman da mesela () örneği için  \( xxx \) kullanıyorum:
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo= phoneNumRegex.search('My number is (415) 555-4242.')
print(mo.group(1)) #415
print(mo.group(2)) #555-4242

#matching multiple groups with the pipe(|) (for exp: r'Batman|Tina Fey' will match either 'Batman' or 'Tina Fey'.
# ikisi aynı anda olursa ilk yakaladığını getirecektir.

heroRegex = re.compile(r'Batman|Tina Fey')
mo1= heroRegex.search('Batman and Tina Fey.')
mo1.group()
print(mo1.group()) #Batman
mo2= heroRegex.search('Tina Fey and Batman.')
mo2.group()
print(mo2.group()) #Tina Fey

#You can also use the pipe to match one of several patterns as part of your regex.

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo=batRegex.search('Batmobile lost a wheel')
print(mo.group()) #Batmobile
print(mo.group(1)) #mobile

#Optional Matching with the Question Mark

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group()) #Batman
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group()) #Batwoman

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group()) #415-555-4242
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group()) #555-4242
#You can think of the ? as saying, “Match zero or one of the group pre- ceding this question mark.”. If you need to
# match an actual question mark character, escape it with \?.

#Matching Zero or More with the Star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batwowowowoman')
print(mo1.group()) #Batwowowowoman
batRegex = re.compile(r'Bat(wo)*man')
mo2 = batRegex.search('The Adventures of Batman')
print(mo2.group()) #Batman


#Matching One or More with the Plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwowowowoman')
print(mo1.group()) #Batwowowowoman
batRegex = re.compile(r'Bat(wo)+man')
mo2 = batRegex.search('The Adventures of Batman')
print(mo2) #None

#While * means “match zero or more,” the + (or plus) means “match one or more.” Unlike the star, which does not require its group to appear in the matched string, the group preceding a plus must appear at least once. It is not optional.

#Matching Specific Repetitions with Curly Brackets
#(Ha){3} > (Ha)(Ha)(Ha)
#(Ha){3,5} > ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group()) #HaHaHa
greedyhaRegex = re.compile(r'(Ha){3,5}')
mo2 = greedyhaRegex.search('HaHaHaHaHa')
print(mo2.group()) #HaHaHaHaHa
#Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible.

#greedy and nongreedy matching
nongreedyhaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyhaRegex.search('HaHaHaHaHa')
print(mo2.group()) #HaHaHa

#The findall() method

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #has no groups
matchingObject = phoneNumRegex.findall('Cell: 415-555-4242 Work: 212-555-0000')
print(matchingObject) #['415-555-4242', '212-555-0000'] , returned a list of strings (as long as there are no groups
# in regex

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #has groups
matchingObject = phoneNumRegex.findall('Cell: 415-555-4242 Work: 212-555-0000')
print(matchingObject) #[('415', '555', '4242'), ('212', '555', '0000')] , returned a list of tuples, each tuple
# represents a found match


#Character Classes

#\d > Any numeric digit from 0 to 9.
#\D > Any character that is not a numeric digit from 0 to 9.
#\w > Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
#\W > Any character that is not a letter, numeric digit, or the underscore character.
#\s > Any space, tab, or newline character. (Think of this as matching “space” characters.)
#\S > Any character that is not a space, tab, or newline.

#The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+), followed by a whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+). The findall() method returns all matching strings of the regex pattern in a list.

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo) #['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

#Making your own character classes
vovelRegex = re.compile(r'[aeiouAEIOU]')
mo = vovelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo) #['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

#You can also include ranges of letters or numbers by using a hyphen. For example, the character class [a-zA-Z0-9]
# will match all lowercase letters, uppercase letters, and numbers. Class [0-5.] will match digits 0 to 5 and a
# period. You do not need to write it as [0-5\.].

#By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character
# class. A negative character class will match all the characters that are not in the character class.

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo1 = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo1) #['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

#The Caret and Dollar sign characters : You can also use the caret symbol (^) at the start of a regex to indicate
# that a match must occur at the beginning of the searched text. Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern.

beginsWithHello = re.compile(r'^Hello')
a =beginsWithHello.search('Hello World!')
print(a) #<re.Match object; span=(0, 5), match='Hello'>
b =beginsWithHello.search('hello World!')
print(b) #none

endsWithNumber = re.compile(r'\d$')
c =endsWithNumber.search('Your number is 42')
print(c) #<re.Match object; span=(16, 17), match='2'>
endsWithNumber = re.compile(r'\d+$')
d =endsWithNumber.search('Your number is 42')
print(d) #<re.Match object; span=(15, 17), match='42'>

wholeStringIsNum = re.compile(r'^\d+$')
e = wholeStringIsNum.search('1234567890')
print(e) #<re.Match object; span=(0, 10), match='1234567890'>

wholeStringIsNum = re.compile(r'^\d+$')
f = wholeStringIsNum.search('ababab df 1234567890')
print(f) #None

#I always confuse the meanings of these two symbols, so I use the mnemonic “Carrots cost dollars” to remind myself that the caret comes first and the dollar sign comes last.

#The Wildcard Character (dot means any single character except newline)

atRegex = re.compile(r'.at')
m =atRegex.findall('The cat in the hat sat on the flat mat.')
print(m) #['cat', 'hat', 'sat', 'lat', 'mat']

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print( mo.group(1)) #Al
print( mo.group(2)) #Sweigart

#The dot-star uses greedy mode: It will always try to match as much text as possible. To match any and all text in a nongreedy fashion, use the dot, star, and question mark (.*?).

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group()) #<To serve man>

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group()) #<To serve man> for dinner.>

#Matching Newlines with the Dot Character (as .* will match everything except a newline, you should use re.DOTALL to
# catch them all)

noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group()
#'Serve the public trust.'
newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group()
#'Serve the public trust.\nProtect the innocent.\nUphold the law.'

# REVIEW OF REGEX SYMBOLS
# • The ? matches zero or one of the preceding group.
# • The * matches zero or more of the preceding group.
# • The + matches one or more of the preceding group.
# • The {n} matches exactly n of the preceding group.
# • The {n,} matches n or more of the preceding group.
# • The {,m} matches 0 to m of the preceding group.
# • The {n,m} matches at least n and at most m of the preceding group.
# • {n,m}? or *? or +? performs a nongreedy match of the preceding group.
# • ^spam means the string must begin with spam.
# • spam$ means the string must end with spam.
# • The . matches any character, except newline characters.
# • \d, \w, and \s match a digit, word, or space character, respectively.
# • \D, \W, and \S match anything except a digit, word, or space character, respectively.
# • [abc] matches any character between the brackets (such as a, b, or c).
# • [^abc] matches any character that isn’t between the brackets.

#Case-Insentive Matching (re.IGNORECASE veya r.I yazarak büyük küçük harf hassasiyetini yok edebilirsin)

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group()) #RoboCop
print(robocop.search('ROBOCOP protects the innocent.').group()) #ROBOCOP

#Substituting Strings with the sub() Method
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')) #CENSORED gave the secret documents to CENSORED.

agentNamesRegex = re.compile(r'Agent (\w)\w*') #The \1 in that string will be replaced by whatever text was matched by group 1— that is, the (\w) group of the regular expression.
print(agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')) #A**** told C**** that E**** knew B**** was a double agent.

#managing complex regexes with re.VERBOSE (bu sayede tek satırda yazmak yerine satırlara bölebiliyorsun yazacağını
# içine notlar ekleyerek:

phoneRegex= re.compile(r'''(
(\d{3}|\(\d{3}\))?              #area code
(\s|-|\.)?                      #seperator
(\d{3})                         #first 3 digits
(\s|-|\.)                       #seperator
(\d{4})                         #last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
)''', re.VERBOSE)

#combining re.IGNORECASE, re.VERBOSE and re.DOTALL (re.compile() function takes only a single value as its second
# argument. to get around this limitation, you can combine re.IGNORECASE, re.VERBOSE and re.DOTALL with a pipe(|).

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL) #a regular expression that’s case-insensitive and includes newlines to match the dot character
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE) #all three options


# How would you write a regex that matches a number with commas for every three digits? It must match the following:
# • '42'
# • '1,234'
# • '6,368,745'
# but not the following:
# • '12,34,567' (which has only two digits between the commas)
# • '1234' (which lacks commas)

numberRegex = re.compile( r'(\d{1,3})(\,\d{3})*')
mo1 = numberRegex.search('1')
print(mo1.group())



# 21. How would you write a regex that matches the full name of someone whose last name is Nakamoto? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
# • 'Satoshi Nakamoto'
# • 'Alice Nakamoto'
# • 'RoboCop Nakamoto' but not the following:
# • 'satoshi Nakamoto' (where the first name is not capitalized)
# • 'Mr. Nakamoto' (where the preceding word has a nonletter character)
# • 'Nakamoto' (which has no first name)
# • 'Satoshi nakamoto' (where Nakamoto is not capitalized)

nakamatoRegex = re.compile(r'(^[A-Z][a-zA-Z]*\sNakamato)')
mo2 = nakamatoRegex.search('Mr Nakamato')
print(mo2.group())


# 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
# • 'Alice eats apples.'
# • 'Bob pets cats.'
# • 'Carol throws baseballs.'
# • 'Alice throws Apples.'
# • 'BOB EATS CATS.' but not the following:
# • 'RoboCop eats apples.'
# • 'ALICE THROWS FOOTBALLS.'
# • 'Carol eats 7 cats.'

garipRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)',re.I)
mo3 = garipRegex.search('caRol Eats apples')
print(mo3.group())