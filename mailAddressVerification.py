import re
firstRegex = '([\w-]+)@([a-zA-Z\d]+)$'
secondRegex = '([\w-]+)@([a-zA-Z\d]+).([a-z]){2,3}$'
thirdRegex = '([\w-]+)@([a-zA-Z\d]+).([a-z]{2,3}).([a-z]){2}$'
def EmailDogrula(uzunluk,email):
    if(uzunluk == 1):
        if(re.match(firstRegex,email)):
            return True
        else:
            return False
    elif(uzunluk == 2):
        if(re.match(secondRegex,email)):
            return True
        else:
            return False
    elif(uzunluk == 3):
        if(re.match(thirdRegex,email)):
           return True
        else:
           return False
    else:
       print("Girilen uzunluk geçersizdir.")

def Dogrulama():
    uzunluk = int(input("Uzunluk giriniz:"))
    email = input("Email adresini giriniz:")
    if(EmailDogrula(uzunluk,email)):
        print(str(uzunluk)+"\n"+email+"\n"+"Mail adresiniz doğrudur.")
    else:
        print(str(uzunluk)+"\n"+email+"\n"+"Mail adresiniz yanlıştır.")

Dogrulama()