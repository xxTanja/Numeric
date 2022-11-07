email1 = 't.grieshaber@web.de'
email2 = 't.grieshaber#web.de'
email3 = '@web.de'
email4 = 't.grieshaber@'
email5 = 't.grieshaber@de'

#easily if you want to add a  TO-DO
# --> pretty easy to use as a reminder
# check lower bar: RUN, TO-DO, python packages etc

#should not start/finish with an @
# should not include more than 1 @
# WHAT ELSE?
#use conditions & loops

def check_email(email):
    #TODO implement different checks
    if email:
    print('em')
        return True
    else:
    #check 1
    # check 2
        return False


for em in [email1, email2, email3, email4, email5]:
    print('{}: {}'.format(em, check_email(em)))

#for i range = this will output individual characters

for i in range(len(email4)):
   print(email4[i])
