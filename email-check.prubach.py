email1 = 'pawel.rubach@sgh.waw.pl'
email2 = 'pawel.rubach#sgh.waw.pl'
email3 = '@sgh.waw.pl'
email4 = 'pawel@'
email5 = 'pawel@.pl'
email6 = 'pa@wel@wwa.pl'
email7 = 'ab@sgh@waw@pl'


def check_email(email):
    if not email:
        return False
    # TODO implement different checks
    if not (email.find('@') > 0 and email.find('@') < len(email)-1):
        print('@ not found or in wrong position')
        return False
    if not (email.find('@') == email.rfind('@')):
        print('@ too many of them')
        return False

    if not (email.find('.') > 0 and email.find('.') < len(email)-1):
        print('. not found or in wrong position')
        return False

    if not email.find(['@':'.'] < len(email)-1):
        print('. in wrong position')
        return False
    return True


for em in [email1, email2, email3, email4, email5, email6, email7]:
    print('{}: {}'.format(em, check_email(em)))

#for i in range(len(email4)):
#    print(email4[i])

email1 = "pawel.rubach@sgh.waw.pl"
email2 = "pawel.rubach@sgh.pl"
email3 = "p@sgh.waw.pl"
email4 = "pawel@"
email5 = ""
email6 = "pawel@.pl"
emails = [email1, email2, email3, email4, email5, email6]
def check_email(email):
    if not email:
        return "Missing mail"
    if not (email[-3:] == ".pl"):
        return False
    if not email.startswith("pawel"):
        return False
    if not email.split("@")[1]=="sgh.waw.pl":
        return False
    if re.match("[a-zA-Z\d]+(?:\.[a-zA-Z\d]+)*\@sgh\.waw\.pl", email):
        print("Absolute match")
    return True
for em in emails:
    print("\"{}\" - {}".format(em, str(check_email(em))))