import json
import os
from Core import products, base, user, category
import datetime
import hashlib
import shutil

now = datetime.datetime.now()
date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
date_dir = now.strftime("%d_%m_%Y")


def max_id():
    with open('HoaDon/id_invoice.txt', 'r') as string:
        line = string.readline()
        while line:
            str_to_reads = line.lstrip("IN")
            #print(str_to_reads)
            line = string.readline()
        return str_to_reads
    

danhsachhoadon=[]
hanghoaban = {}

def create_danhsachhanghoamua():
    while not os.path.isfile('Data/products_mua.csv'):
        with open('Data/products.csv', 'r') as f:
            line = f.readline()
            while line:
                str_to_reads = line.split("#")
                if len(str_to_reads) > 1:
                    stt = str_to_reads[0]
                    ten = str_to_reads[1]
                    soluong_ban = 0
                    dongia = str_to_reads[2]
                    category = str_to_reads[3]
                    products_code = str_to_reads[5]
                    date_ban = date_time
                    str_to_save = str(stt) + "#" + str(ten) + "#" + str(dongia) + "#" + str(category) + "#" + str(soluong_ban)+ "#" + str(products_code)+ "#" + str(date_ban) + '\n'
                    with open('Data/products_mua.csv', 'a') as wf:
                        line = wf.write(str_to_save)
                line = f.readline()

# create_danhsachhanghoamua()

def update_danhsachhanghoamua():
    shutil.copy('Data/products_mua.csv', 'Data/products_mua_temp.csv')
    with open('Data/products.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads_kho = line.split("#")
            if len(str_to_reads_kho) > 1:
                stt = str_to_reads_kho[0]
                ten_kho = str_to_reads_kho[1]
                soluong_ban = 0
                dongia = str_to_reads_kho[2]
                category = str_to_reads_kho[3]
                products_code = str_to_reads_kho[5]
                date_ban = date_time
                str_to_save = str(stt) + "#" + str(ten_kho) + "#" + str(dongia) + "#" + str(category) + "#" + str(soluong_ban)+ "#" + str(products_code)+ "#" + str(date_ban) + '\n'
                with open('Data/products_mua_temp.csv', 'r') as wf:
                    wline = wf.readline()
                    count = 0
                    while wline:
                        str_to_reads_ban = wline.split("#")
                        if len(str_to_reads_ban) > 1:
                            ten_ban = str_to_reads_ban[1]
                            if ten_kho.upper() == ten_ban.upper():
                                count += 1
                        wline = wf.readline()
                if count == 0 :
                    with open('Data/products_mua.csv', 'a') as save:
                        data = save.write(str_to_save)
            line = f.readline()
                
# update_danhsachhanghoamua()



def update_hanghoamua(invoice):
    create_danhsachhanghoamua()
    update_danhsachhanghoamua()
    with open('HoaDon/' + invoice + '.json', 'r') as f:
        hoadon = json.load(f)
        date_nhap = hoadon["ngayhoadon"]
        for hanghoa in hoadon["danhsachhanghoa"]:
            ten = hanghoa["ten"]
            soluong = int(hanghoa["soluong"])
            # print("ket qua sau khi doc:",ten,soluong)
            shutil.copy('Data/products_mua.csv', 'Data/products_mua_temp.csv')
            with open('Data/products_mua_temp.csv', 'r') as f:
                with open('Data/products_mua.csv', 'w') as wfile:
                    line = f.readline()
                    while line:
                        str_to_reads = line.split("#")
                        if len(str_to_reads) > 1:
                            if ten.upper() == str_to_reads[1].upper():
                                stt = str_to_reads[0]
                                soluong_ban = int(str_to_reads[4])
                                dongia = str_to_reads[2]
                                category = str_to_reads[3]
                                total_soluong = soluong_ban + soluong
                                product_code = str_to_reads[5]
                                str_to_save = str(stt) + "#" + str(ten) + "#" + str(dongia) + "#" + str(category) + "#" + str(total_soluong)+ "#" + str(product_code) + "#" + str(date_nhap) + '\n'
                                line = wfile.write(str_to_save)
                            else:
                                line = wfile.write(line)
                        line = f.readline()
                wfile.closed

# update_hanghoamua("IN006")


def update_kho(invoice):
    with open('HoaDon/' + invoice + '.json', 'r') as f:
        hoadon = json.load(f)
        date_nhap = hoadon["ngayhoadon"]
        for hanghoa in hoadon["danhsachhanghoa"]:
            ten = hanghoa["ten"]
            soluong = int(hanghoa["soluong"])
            # print("ket qua sau khi doc:",ten,soluong)
            shutil.copy('Data/products.csv', 'Data/products_temp.csv')
            with open('Data/products_temp.csv', 'r') as f:
                with open('Data/products.csv', 'w') as wfile:
                    line = f.readline()
                    while line:
                        str_to_reads = line.split("#")
                        if len(str_to_reads) > 1:
                            if ten.upper() == str_to_reads[1].upper():
                                stt = str_to_reads[0]
                                soluong_ban = int(str_to_reads[4])
                                dongia = str_to_reads[2]
                                category = str_to_reads[3]
                                total_soluong = soluong_ban - soluong
                                product_code = str_to_reads[5]
                                str_to_save = str(stt) + "#" + str(ten) + "#" + str(dongia) + "#" + str(category) + "#" + str(total_soluong)+ "#"  + str(product_code) + "#" + str(date_nhap) + '\n'
                                line = wfile.write(str_to_save)
                                # print(str_to_save)
                            else:
                                line = wfile.write(line)
                        line = f.readline()
                wfile.closed

# update_kho("IN010")



def check_nguoimua(msisdn):
    with open('Data/buyer_user.csv', 'r') as f:
        line = f.readline()
        count = 0
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                msisdn_buyer = str_to_reads[1]
                if msisdn == msisdn_buyer:
                    name_buyer = str_to_reads[2]
                    count +=1
            line = f.readline()
        if count == 0:
            name_buyer = user.newBuyer(msisdn)
        return name_buyer

def get_name_buyer(msisdn):
    name_buyer = ''
    with open('Data/buyer_user.csv', 'r') as f:
        line = f.readline()
        count = 0
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                msisdn_buyer = str_to_reads[1]
                if msisdn == msisdn_buyer:
                    name_buyer = str_to_reads[2]
            line = f.readline()
        return name_buyer


# name_buyer1 = check_nguoimua('0914412556')
# print(name_buyer1)

# def create_invoice():
#     sohoadon = int(max_id()) + 1
#     sohoadon = str(format(sohoadon, '03d'))
#     print("moi ban tao hoa don so: IN" + sohoadon)
#     hoadon={}
#     hoadon["sohoadon"] = "IN" + sohoadon
#     hoadon["ngayhoadon"]= date_time
#     phone = input("nhap so dien thoai nguoi mua hang :")
#     while len(phone) != 10:
#         phone = input("Ban da nhap sai so dien thoai. Hay nhap lai:")
#     hoadon["phone"] = phone
#     hoadon["nguoimua"] = check_nguoimua(hoadon["phone"])
#     hoadon["tongtientruocthue"] = 0
#     hoadon["thue"] = 0.10
#     hoadon["tongtien"] = 0
#     hoadon["danhsachhanghoa"] = []
#     stt_hang_invoice = 1
#     nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
#     while nhaphanghoa.upper() == 'Y':
#         products.danhsach_hanghoa()
#         hanghoa = {}
#         hanghoa["stt"] = stt_hang_invoice
#         id_product = base.check_id_product(int(input("nhap id hang hoa: ")))
#         while id_product is None:
#             id_product = base.check_id_product(int(input("ID hang hoa sai. Hay nhap lai, : ")))
#             products.danhsach_hanghoa()
#         while id_product is not None:
#             data = base.load_id_products(int(id_product))
#             hanghoa["ten"] = data[0]
#             hanghoa["soluong"] = int(input("nhap so luong: "))
#             hanghoa["dongia"] = int(data[1])
#             hanghoa["thanhtien"] = hanghoa["soluong"] * hanghoa["dongia"]
                
#             if hanghoa["ten"] in hanghoaban:
#                 hanghoaban[hanghoa["ten"]]["tongso"] = hanghoaban[hanghoa["ten"]]["tongso"] + hanghoa["soluong"]
#                 hanghoaban[hanghoa["ten"]]["doanhthu"] = hanghoaban[hanghoa["ten"]]["doanhthu"] + hanghoa["thanhtien"]
#             else:
#                 hanghoaban[hanghoa["ten"]] = {
#                 "tongso": hanghoa["soluong"],
#                 "doanhthu": hanghoa["thanhtien"]
#                 }

#             hoadon["danhsachhanghoa"].append(hanghoa)
#             hoadon["tongtientruocthue"] = hoadon["tongtientruocthue"] + (hanghoa["thanhtien"])
#             break 
#         nhaphanghoa = input("=> Ban co muon nhap tiep hang hoa khong (y/n): ")
#         stt_hang_invoice += 1
#     hoadon["tongtien"] = hoadon["tongtientruocthue"] + hoadon["tongtientruocthue"] * hoadon["thue"]
#     #danhsachhoadon.append(hoadon)
#     filename = "IN" + sohoadon +".json"
#     with open('../HoaDon/' + filename, 'w') as f:
#         json.dump(hoadon, f)
#     data = open("../HoaDon/id_invoice.txt", "a")
#     data.write("IN" + sohoadon +"\n")
#     update_hanghoamua("IN" + sohoadon)
#     update_kho("IN" + sohoadon)
#     view_invoice("IN" + sohoadon)

def session_cache(invoice_id,data):
    session = hashlib.md5(invoice_id.encode()).hexdigest()
    with open('log/' + session + '.txt', 'w') as f:
        json.dump(data, f)

def load_session_cache(invoice_id):
    session = hashlib.md5(invoice_id.encode()).hexdigest()
    with open('log/' + session + '.txt', 'r') as f:
        invoice_data = json.load(f)
        return invoice_data      

def load_last_id_session_cache(invoice_id):
    session = hashlib.md5(invoice_id.encode()).hexdigest()
    with open('log/' + session + '.txt', 'r') as f:
        invoice_data = json.load(f)
        if invoice_data.get("danhsachhanghoa") == None:
            id_session_cache = 1
        else:
            for hanghoa in invoice_data["danhsachhanghoa"]:
                id_session_cache = int(hanghoa["stt"]) + 1
        return id_session_cache   

def create_invoice(sohoadon,phone,stt_hang_invoice,name_product,soluong):
    hoadon={}
    hanghoa = {}
    hoadon = load_session_cache(sohoadon)
    print(hoadon)
    if hoadon.get("danhsachhanghoa") != None:
        get_stt = load_last_id_session_cache(sohoadon)
        data = base.load_name_products(name_product)
        hanghoa["stt"] = int(get_stt)
        hanghoa["ten"] = data[0]
        hanghoa["soluong"] = soluong
        hanghoa["dongia"] = int(data[1])
        hanghoa["thanhtien"] = int(hanghoa["soluong"]) * int(hanghoa["dongia"])
            
        if hanghoa["ten"] in hanghoaban:
            hanghoaban[hanghoa["ten"]]["tongso"] = int(hanghoaban[hanghoa["ten"]]["tongso"]) + int(hanghoa["soluong"])
            hanghoaban[hanghoa["ten"]]["doanhthu"] = int(hanghoaban[hanghoa["ten"]]["doanhthu"]) + int(hanghoa["thanhtien"])
        else:
            hanghoaban[hanghoa["ten"]] = {
            "tongso": hanghoa["soluong"],
            "doanhthu": hanghoa["thanhtien"]
            }
        hoadon["danhsachhanghoa"].append(hanghoa)
        hoadon["tongtientruocthue"] = int(hoadon["tongtientruocthue"]) + int(hanghoa["thanhtien"])
    else:
        hoadon["sohoadon"] = sohoadon
        hoadon["ngayhoadon"]= date_time
        hoadon["phone"] = phone
        hoadon["nguoimua"] = get_name_buyer(phone)
        hoadon["tongtientruocthue"] = 0
        hoadon["thue"] = 0.10
        hoadon["tongtien"] = 0
        hoadon["danhsachhanghoa"] = []

        hanghoa["stt"] = stt_hang_invoice

        data = base.load_name_products(name_product)
        hanghoa["ten"] = data[0]
        hanghoa["soluong"] = soluong
        hanghoa["dongia"] = int(data[1])
        hanghoa["thanhtien"] = int(hanghoa["soluong"]) * int(hanghoa["dongia"])
            
        if hanghoa["ten"] in hanghoaban:
            hanghoaban[hanghoa["ten"]]["tongso"] = int(hanghoaban[hanghoa["ten"]]["tongso"]) + int(hanghoa["soluong"])
            hanghoaban[hanghoa["ten"]]["doanhthu"] = int(hanghoaban[hanghoa["ten"]]["doanhthu"]) + int(hanghoa["thanhtien"])
        else:
            hanghoaban[hanghoa["ten"]] = {
            "tongso": hanghoa["soluong"],
            "doanhthu": hanghoa["thanhtien"]
            }

        hoadon["danhsachhanghoa"].append(hanghoa)
        hoadon["tongtientruocthue"] = int(hoadon["tongtientruocthue"]) + int(hanghoa["thanhtien"])

        print(hoadon["thue"])
        hoadon["tongtien"] = int(hoadon["tongtientruocthue"]) + int(hoadon["tongtientruocthue"]) * hoadon["thue"]
    
    return hoadon
    #danhsachhoadon.append(hoadon)
    # filename = "IN" + sohoadon +".json"
    # with open('../HoaDon/' + filename, 'w') as f:
    #     json.dump(hoadon, f)
    # update_hanghoamua("IN" + sohoadon)
    # update_kho("IN" + sohoadon)
    # view_invoice("IN" + sohoadon)


# data = create_invoice("IN016","0974412556","1","1","1")
# print(data)






def add_product_to_invoice():
    hoadon = create_invoice(sohoadon,phone,stt_hang_invoice,id_product,soluong)


def file_name_exists():
    sohoadon_canxem = ''
    while not os.path.isfile('../HoaDon/'+ sohoadon_canxem +'.json'):
        sohoadon_canxem = input("nhap so hoa don can xem:")  
    return sohoadon_canxem


def create_file_invoice(invoice_id):
    while not os.path.isfile('HoaDon/'+ invoice_id +'.json'):
        session = hashlib.md5(invoice_id.encode()).hexdigest()
        id1 = max_id()
        id2 = invoice_id.lstrip("IN")
        if id1 < id2:
            data = open("HoaDon/id_invoice.txt", "a")
            data.write(invoice_id +"\n")
            source = "log/" + session + ".txt"
            destination = "HoaDon/" + invoice_id + ".json"
            shutil.copy(source,destination)
            update_hanghoamua(invoice_id)
            update_kho(invoice_id)
    return invoice_id

# file_name_exists()
# print(file_name_exists())
 
def view_invoice(sohoadon = None):
    if sohoadon == None:
        sohoadon_canxem = file_name_exists()
    else:
        sohoadon_canxem = sohoadon
    with open('HoaDon/' + sohoadon_canxem + '.json', 'r') as f:
        invoice = json.load(f)
        # print(invoice)
        # for hoadon in invoice:
        #Hoa don se in o day
        #################################################################################
        # print("                          HOA DON MUA HANG                                  ")
        # print("So hoa don:",invoice["sohoadon"])
        # print("Ngay xuat:",invoice["ngayhoadon"])
        # print("Ten khach hang:",invoice["nguoimua"])
        # print("Tong tien truoc thue",str(invoice["tongtientruocthue"]))
        # print("Tong tien sau thue ",str('%.2f' % invoice["tongtien"]))
        # print("_______________________________THONG TIN HANG HOA________________________________")
        # print("+-------+-------------------------+----------+---------------+------------------+")
        # print("|  STT  |         hang hoa        | so luong |    don gia    |    thanh tien    |")
        # print("+-------+-------------------------+----------+---------------+------------------+")
                    
        # for hanghoa in invoice["danhsachhanghoa"]:
        # #print("In dong hang hoa o day")
        #     print("|",str((hanghoa['stt'])).center(5),"|" ,hanghoa['ten'].rjust(23), "|",str(hanghoa['soluong']).center(8),"|",str(hanghoa['dongia']).center(13),"|",str(hanghoa['thanhtien']).center(16),"|")
        # print("+-------+-------------------------+----------+---------------+------------------+")
        # #end of Hoa don se in o day
        ##########################################################################
        return invoice

# view_invoice("IN011")

list_products_daban = []

def load_products_daban():
    files = os.listdir("../Data")
    if "products_mua.csv" not in files:
        return

    with open('Data/products_mua.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                products = {}
                products["id"] = str_to_reads[0]
                products["ten"] = str_to_reads[1]
                products["giaban"] = str_to_reads[2]
                products["category_id"] = str_to_reads[3]
                products["soluong"] = str_to_reads[4]
                products["product_code"] = str_to_reads[5]
                products["date_ban"] = str_to_reads[6]
                if products["date_ban"].endswith('\n'):
                    products["date_ban"] = products["date_ban"][0:len(products["date_ban"])-1]
                list_products_daban.append(products)
            line = f.readline()
    # print("list_products:", list_products)
    return list_products_daban


def danhsach_hanghoaban():
    list_products_daban.clear()
    load_products_daban()
    print("___________________________________DANH SACH SAN PHAM DA BAN________________________________________")
    print("+--------+-----------+----------------+------------+-----------+------------+----------------------+")
    print("|  STT   |  Ma hang  |  Ten san pham  |   Don gia  |  Ma loai  |  So luong  |       Ngay nhap      |")
    print("+--------+-----------+----------------+------------+-----------+------------+----------------------+")
    for x in list_products_daban:
        print("|",x["id"].center(6),"|",x["product_code"].center(9),"|", x["ten"].ljust(14),"|",x["giaban"].ljust(10),"|",x["category_id"].center(9),"|",x["soluong"].ljust(10),"|",x["date_ban"].ljust(20),"|")
    print("+--------+-----------+----------------+------------+-----------+------------+----------------------+")

# danhsach_hanghoaban()


def list_invoice():
    list_line = []
    with open('HoaDon/id_invoice.txt', 'r') as string:
        line = string.readline()
        while line:
            if line.endswith('\n'):
                line = line[0:len(line)-1]
            # list_line = list_line + line + "\n"
            list_line.append(line)
            line = string.readline()
        return list_line