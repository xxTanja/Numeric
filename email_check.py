#easily if you want to add a  TO-DO
# --> pretty easy to use as a reminder
# check lower bar: RUN, TO-DO, python packages etc

#should not start/finish with an @
# should not include more than 1 @
# WHAT ELSE?
#use conditions & loops

#print(ord('@'))
#print('---------')

#regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b

#import re

#def check(s):
 #   pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  #  if re.match(pat,s):
   #     print("Valid Email")
    #else:
     #   print("Invalid Email")

#Driver code
#if __name__=='__main__':

# Enter the email
 #   email = "ankitrai326@gmail.com"

    # calling run function
  #  check(email)

   # email = "my.ownsite@our-earth.org"
    #check(email)

    #email = "ankitrai326.com"
    #check(email)


print('-------------')

email1 = 't.grieshaber@web.de'
email2 = 't.grieshaber#web.de'
email3 = '@web.de'
email4 = 't.grieshaber@'
email5 = 't.grieshaber@de'
email6 = 't.gri@eshaber@de'

print(len(email1))
print('-----------')

def check_email(email):
    if not email:
        return False
    #TODO
    if not email.find('@') > 0 and email.find('0') < len(email)-1):
            and email.find('@')==email.rfind('@'):
        print('@ not found or in wrong position')
        return False
    if not email.find('@')== email.rfind('@')):
        print('@ too many of them')
        return False
    return True

    # rfind. reverse look from the last character
    # if not finding 'chr' it will return -1

    #if email:
        #for i in range(len(email1):
         #   print(em)
        #em[0 == 't']
       # em.str.startwith[0] == ('t')
        #return True
    #else:
     #   while em < 19:
      #      print(em)
       # em.str.startwith [0] == ('@')
       # return False


for em in [email1, email2, email3, email4, email5, email6]:
   print('{}: {}'.format(em, check_email(em)))

#for i range = this will output individual characters

#for i in range(len(email1)):
#print(email1[i])