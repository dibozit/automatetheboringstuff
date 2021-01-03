#finds phone numbers and email addresses on the clipboard.

import pyperclip, re

#The pyperclip module has copy() and paste() functions that can send text to and receive text from your computer’s
# clipboard. Sending the output of your program to the clipboard will make it easy to paste it to an email, word processor, or some other software.

#TODO1: create phone regex

phoneRegex= re.compile(r'''(
( \d{3} | \(\d{3}\) )?               #area code
(\s | - | \.)?                       #seperator
(\d{3})                              #first 3 digits
(\s | - | \.)                        #seperator
(\d{4})                              #last 4 digits
(\s* (ext | x | ext.) \s* (\d{2,5}) )? #extension
)''', re.VERBOSE)

#The phone number begins with an optional area code, so the area code group is followed with a question mark. Since the area code can be just three digits (that is, \d{3}) or three digits within parentheses (that is, \(\d{3}\)), you should have a pipe joining those parts. You can add the regex comment # Area code to this part of the multiline string to help you remember what (\d{3}|\(\d{3}\))? is supposed to match.
#The phone number separator character can be a space (\s), hyphen (-), or period (.), so these parts should also be joined by pipes. The next few parts of the regular expression are straightforward: three digits, followed by another separator, followed by four digits. The last part is an optional extension made up of any number of spaces followed by ext, x, or ext., fol- lowed by two to five digits.


#TODO2: create e-mail regex

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ #username
@                 #@ symbol
[a-zA-Z0-9.-]+    #domain name
(\.[a-zA-Z]{2,4}) #dot-someting
)''', re.VERBOSE)

#The username part of the email addressuis one or more characters that can be any of the following: lowercase and uppercase letters, numbers, a dot, an underscore, a percent sign, a plus sign, or a hyphen. You can put all of these into a character class: [a-zA-Z0-9._%+-].
#The domain and username are separated by an @ symbolv. The domain namewhas a slightly less permissive character
# class with only letters, numbers, periods, and hyphens: [a-zA-Z0-9.-]. And last will be the “dot-com” part (technically known as the top-level domain), which can really be dot-anything. This is between two and four characters.
#The format for email addresses has a lot of weird rules. This regular expression won’t match every possible valid
# email address, but it’ll match almost any typical email address you’ll encounter.

#TODO3: Find matches in clipboard text

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# phone numbers : xxx (area code -group 1) x (seperator- group 2) xxx (first 3 digits -group 3) x (seperator -group 4)
# xxxx (last four digits -group 5) (\s* (ext | x | ext.) (extension -group 6) \s* (group 7) xxxxx (\d{2,5})(extension
# - group 8)
#sonuç şöyle çıkacak = aaa-aaa-aaaa xaaaaa

#TODO4: Copy results to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches)) #since pyperclip.copy() func takes only a single string value, not a list of
    # strings, we call the join() method on matches
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers of email addresses found.')
