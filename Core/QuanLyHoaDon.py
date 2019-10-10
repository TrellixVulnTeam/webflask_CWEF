from Core import user, base, main, category
import hashlib
import datetime

now = datetime.datetime.now()
date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
date_dir = now.strftime("%d_%m_%Y")


def session(email):
    session = hashlib.md5(email.encode()).hexdigest()
    str_to_save = email + "#" + date_time + '\n'
    with open('log/' + session + '.txt', 'w') as f:
        session = f.write(str_to_save)

# print("+----------------------------------------------+")
# print("|                QUAN LY HOA DON               |")
# print("+----------------------------------------------+")



def Login(email,password):
    loginlist = []
    logindict = {}
    sellerList = user.loadUserSeller()
    sellerCount = 0
    adminCount = 0
    count = None
    while count is None:
        # print("sellerList:", sellerList)
        logindict["status"] = '1'
        # logindict["email"] = input("Hay nhap acount cua ban:")
        # password_text = input("Hay nhap password cua ban:")
        logindict["email"] = email
        password_text = password
        print(logindict["email"],password_text)
        logindict["password"] = hashlib.md5(password_text.encode()).hexdigest()
        loginlist.append(logindict)
        for sellerUser in sellerList:
            if logindict["status"] == sellerUser["status"]  and logindict["email"] == sellerUser["email"] and logindict["password"] == sellerUser["password"]:
                sellerCount = 1
                if logindict["status"] == sellerUser["status"]  and logindict["email"] == sellerUser["email"] and logindict["password"] == sellerUser["password"] and logindict["email"] == 'admin@gmail.com':
                    adminCount = 1
            else:
                count = None
        if sellerCount > 0 and adminCount > 0:
            print("Xin chao ",logindict["email"]," ban da dang nhap thanh cong voi quyen ADMIN")
            session(logindict["email"])
            # main.menuDiplayAdmin(logindict["email"])
            return True
            break
        if sellerCount > 0 and adminCount == 0:
            print("Xin chao ",logindict["email"]," ban da dang nhap thanh cong voi quyen SELLER")
            session(logindict["email"])
            # main.menuDiplayClient(logindict["email"])
            return True
            break
        if count is None:
            # print("Sai USER hoac PASSWORD. Xin moi ban nhap lai")
            return False

# Login('admin@gmail.com','123')

