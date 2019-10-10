from Core import base
import datetime
import hashlib
import shutil
import sys
import json
import os.path



class user():
    id = None
    status = None
    email = None
    account_name = None
    create_date = None
    def __init__(self,id,account_name):
        self.id = id
        self.account_name = account_name
        now = datetime.datetime.now()
        self.create_date = now.strftime("%d/%m/%Y, %H:%M:%S")

    def create_seller(self,status,email,password):
        self.status = status
        self.password = password
        self.email = email
        str_to_save = str(self.id) + "#" + str(self.status) + "#" + str(self.email) + "#" + str(self.password) + "#" + str(self.account_name) + "#" + str(self.create_date) + '\n'
        # with open('D:\Google Drive\Python\webflask\Data\seller_user.csv', 'a') as f:
        with open("Data/seller_user.csv", 'a') as f:
            str_to_save = f.write(str_to_save)

    def create_buyer(self,phone):
        self.phone = phone
        str_to_save = str(self.id) + "#" + str(self.phone) + "#" + str(self.account_name) + "#" + str(self.create_date) + '\n'
        with open('Data/buyer_user.csv', 'a') as f:
            str_to_save = f.write(str_to_save) 




sellerList = []
def loadUserSeller():
    with open('Data/seller_user.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                userSellerList = {}
                userSellerList["status"] = str_to_reads[1]
                userSellerList["email"] = str_to_reads[2]
                userSellerList["password"] = str_to_reads[3]
                sellerList.append(userSellerList)
            line = f.readline()
    # print("userSellerList:", sellerList)
    return  sellerList

# loadUserSeller()
# print("userSellerList:", sellerList)

def check_seller(email):
    sellerList.clear()
    loadUserSeller()
    for loai in sellerList:
        if loai["email"].upper() == email.upper():
            return loai

# id_exists = check_seller("admin10@gmail.com")
# print(id_exists)

buyerList = []
def loadUserBuyer():
    with open('Data/buyer_user.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                userBuyerList = {}
                userBuyerList["phone"] = str_to_reads[1]
                userBuyerList["name"] = str_to_reads[2]
                buyerList.append(userBuyerList)
            line = f.readline()
    return  buyerList

#loadUserBuyer()

def check_buyer(phone):
    buyerList.clear()
    loadUserBuyer()
    for phonelist in buyerList:
        if phonelist["phone"].upper() == phone.upper():
            return phone




# id_exists = check_buyer("admin10@gmail.com")
# print(id_exists)

def readUserSeller():
    readListUserSeller =[]
    with open('Data/seller_user.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                userSellerList = {}
                userSellerList["id"] = str_to_reads[0]
                userSellerList["status"] = str_to_reads[1]
                if int(userSellerList["status"]) == 1:
                    userSellerList["status"] = 'active'
                else:
                    userSellerList["status"] = 'inactive'
                userSellerList["email"] = str_to_reads[2]
                userSellerList["account_name"] = str_to_reads[4]
                userSellerList["create_date"] = str_to_reads[5]
                if userSellerList["create_date"].endswith('\n'):
                    userSellerList["create_date"] = userSellerList["create_date"][0:len(userSellerList["create_date"])-1]
                readListUserSeller.append(userSellerList)
            line = f.readline()
    # print("userSellerList:", readListUserSeller)
    print("__________________________________________DANH SACH SELLER_____________________________________________")
    print("+-------+---------------+-------------------------+-------------------------+-------------------------+")
    print("|  STT  |     Status    |        Email            |          Name           |        Create Date      |")
    print("+-------+---------------+-------------------------+-------------------------+-------------------------+")
    for lines in readListUserSeller:
        print("|",lines["id"].center(5),"|",lines["status"].ljust(13),"|",lines["email"].ljust(23),"|",lines["account_name"].ljust(23),"|",lines["create_date"].center(23),"|")
    print("+-------+---------------+-------------------------+-------------------------+-------------------------+")


# readUserSeller()



def readUserBuyer():
    readListUserBuyer =[]
    with open('Data/buyer_user.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                userBuyerList = {}
                userBuyerList["id"] = str_to_reads[0]
                userBuyerList["phone"] = str_to_reads[1]
                userBuyerList["account_name"] = str_to_reads[2]
                userBuyerList["create_date"] = str_to_reads[3]
                if userBuyerList["create_date"].endswith('\n'):
                    userBuyerList["create_date"] = userBuyerList["create_date"][0:len(userBuyerList["create_date"])-1]
                readListUserBuyer.append(userBuyerList)
            line = f.readline()
    # print("userBuyerList:", readListUserBuyer)
    # print("______________________________DANH SACH BUYLER______________________________")
    # print("+-------+---------------+-------------------------+-------------------------+")
    # print("|  STT  |     Phone     |        Email            |        Create Date      |")
    # print("+-------+---------------+-------------------------+-------------------------+")
    # for lines in readListUserBuyer:
    #     print("|",lines["id"].center(5),"|",lines["phone"].ljust(13),"|",lines["account_name"].ljust(23),"|",lines["create_date"].center(23),"|")
    # print("+-------+---------------+-------------------------+-------------------------+")
    return readListUserBuyer
# readUserBuyer()




def readOneUserBuyer(phone):
    readListUserBuyer =[]
    with open('Data/buyer_user.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                userBuyerList = {}
                userBuyerList["id"] = str_to_reads[0]
                userBuyerList["phone"] = str_to_reads[1]
                if userBuyerList["phone"].upper() == phone.upper():
                    userBuyerList["account_name"] = str_to_reads[2]
                    userBuyerList["create_date"] = str_to_reads[3]
                    if userBuyerList["create_date"].endswith('\n'):
                        userBuyerList["create_date"] = userBuyerList["create_date"][0:len(userBuyerList["create_date"])-1]
                    readListUserBuyer.append(userBuyerList)
            line = f.readline()
    return readListUserBuyer




def newUserSeller():
    loadUserSeller()
    email = input("email cua ban la gi: ")
    count = 0
    for sellerUser in sellerList:
        if email.upper() == sellerUser["email"].upper():
            count += 1
    if count > 0:
        print("Login name already exist!", email)
    else:
        id_list = base.get_id('../Data/seller_user.csv')
        # print(id_list["id"])
        idNew = int(id_list["id"]) + 1
        # print(idNew)
        account_name = input("Ten cua ban la gi?: ")
        password_text = input("Mat khau cua ban la gi?: ")
        password_encode = hashlib.md5(password_text.encode()).hexdigest()
        sellerAcc = user(idNew,account_name)
        sellerAcc.create_seller(1,email,password_encode)
    
# newUserSeller()


def newUserBuyer():
    loadUserBuyer()
    phone = input("So dien thoai cua ban la gi: ")
    count = 0
    for buyerUser in buyerList:
        if phone == buyerUser["phone"]:
            count += 1
    if count > 0:
        print("account name already exist!", phone)
    else:
        id_list = base.get_id('../Data/buyer_user.csv')
        idNew = int(id_list["id"]) + 1
        account_name = input("Ten cua ban la gi?: ")
        sellerAcc = user(idNew,account_name)
        sellerAcc.create_buyer(phone)

# newUserBuyer()


def newBuyer(msisdn,name):
    phone = msisdn
    id_list = base.get_id('Data/buyer_user.csv')
    idNew = int(id_list["id"]) + 1
    account_name = name
    sellerAcc = user(idNew,account_name)
    sellerAcc.create_buyer(phone)
    return account_name

def deactiveUserSeller():
    shutil.copy('../Data/seller_user.csv', '../Data/seller_user_temp.csv')
    email = input("account bạn muon deactive: ")
    id_exists = check_seller(email)
    while id_exists is None:
        email = input("account khong ton tai. xin moi nhap lai:")
        id_exists = check_seller(email)
    with open('../Data/seller_user_temp.csv', 'r') as f:
        with open('../Data/seller_user.csv', 'w') as wfile:
            line = f.readline()
            while line:
                str_to_reads = line.split("#")
                if len(str_to_reads) > 1:
                    if email.upper() == str_to_reads[2].upper():
                        email = str_to_reads[2]
                        newline = line.replace("#1#", "#0#")
                        # print("newSellerList 1:", newline)
                        newline = wfile.write(newline)
                    else:
                        # print("newSellerList 2:", line)
                        line = wfile.write(line)
                line = f.readline()
        wfile.closed
    #print("newSellerList:", newSellerList)
    

# deactiveUserSeller()


def updateUserSeller():
    shutil.copy('../Data/seller_user.csv', '../Data/seller_user_temp.csv')
    email = input("account bạn muon update: ")
    id_exists = check_seller(email)
    while id_exists is None:
        email = input("account khong ton tai. xin moi nhap lai:")
        id_exists = check_seller(email)
    with open('../Data/seller_user_temp.csv', 'r') as f:
        with open('../Data/seller_user.csv', 'w') as wfile:
            line = f.readline()
            while line:
                str_to_reads = line.split("#")
                if len(str_to_reads) > 1:
                    if email.upper() == str_to_reads[2].upper():
                        id = str_to_reads[0]
                        status = str_to_reads[1]
                        email = str_to_reads[2]
                        password_text = input("Nhap password moi neu ban muon thay doi:")
                        if len(password_text) > 0:
                            password = hashlib.md5(password_text.encode()).hexdigest()
                        else:
                            password = str_to_reads[3]
                        name = input("Nhap ten nguoi dung moi neu ban muon thay doi:")
                        if len(name) > 0:
                            account_name = name
                        else:
                            account_name = str_to_reads[4]
                        create_date = str_to_reads[5]
                        str_to_save = str(id) + "#" + str(status) + "#" + str(email) + "#" + str(password) + "#" + str(account_name) + "#" + str(create_date)
                        line = wfile.write(str_to_save)
                    else:
                        line = wfile.write(line)
                line = f.readline()
        wfile.closed
    #print("newSellerList:", newSellerList)

# updateUserSeller()

def oldUser():
    pass
