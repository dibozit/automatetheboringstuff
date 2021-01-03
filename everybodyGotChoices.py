a= "Ever told on a nigga?"
b= "Ever squeezed a trigger?"
c = "Ever set a nigga up?"
d = "Ever helped a brother out when he was down on his luck?"
e= "You a sap?"
f= "You a boss player, you a mack?"
g= "Let me hold a couple dollars"
h= "Y'all still be poppin' y'all collars?"
i= "Stock rims on a scraper"
j="Paint wetter than a lake"
k= "Poodle in my blood"

Choices =[a,b,c,d,e,f,g,h,i,j,k]
x=0
while x<len(Choices):
    choice = Choices[x]
    print(choice)
    if (x%2)==0 :
        print('nope')
        x += 1
    else:
        print('yup!')
        x += 1