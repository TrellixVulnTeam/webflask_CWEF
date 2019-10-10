import os
from Core import category, invoice
import datetime

now = datetime.datetime.now()
date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
date_dir = now.strftime("%d_%m_%Y")



def load_products():
    list_products = []
    files = os.listdir("Data")
    if "products.csv" not in files:
        return

    with open('Data/products.csv', 'r') as f:
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
                products["date_nhap"] = str_to_reads[6]
                if products["date_nhap"].endswith('\n'):
                    products["date_nhap"] = products["date_nhap"][0:len(products["date_nhap"])-1]
                list_products.append(products)
            line = f.readline()
    # print("list_products:", list_products)
    return list_products


def name_id_product():
    list_products.clear()
    load_products()
    name_id_product =[]
    for x in list_products:
        id = x["id"]
        name = x["ten"]
        lists =  name
        name_id_product.append(lists)
    return name_id_product

    




def check_product(product_code):
    list_products.clear()
    load_products()
    for loai in list_products:
        if loai["product_code"].upper() == product_code.upper():
            return loai

# a = check_product("COCA")
# print(a)

def get_lastid():
    list_products = load_products()
    for line in list_products:
        id = line['id']
    return id

def danhsach_hanghoa():
    list_products.clear()
    load_products()
    print("______________________________________DANH SACH SAN PHAM____________________________________________")
    print("+--------+-----------+----------------+------------+-----------+------------+----------------------+")
    print("|  STT   |  Ma hang  |  Ten san pham  |   Don gia  |  Ma loai  |  So luong  |       Ngay nhap      |")
    print("+--------+-----------+----------------+------------+-----------+------------+----------------------+")
    for x in list_products:
        print("|",x["id"].center(6),"|",x["product_code"].center(9),"|", x["ten"].ljust(14),"|",x["giaban"].ljust(10),"|",x["category_id"].center(9),"|",x["soluong"].ljust(10),"|",x["date_nhap"].ljust(20),"|")
    print("+--------+-----------+----------------+------------+-----------+------------+----------------------+")

# danhsach_hanghoa()




# def create_products():
#     data = {}
#     product_code = input("xin moi nhap ma hang hoa:")
#     while len(product_code) != 4:
#         product_code = input("ma hang hoa can co 4 ky tu:")
#     id_exists = check_product(product_code)
#     while id_exists is not None:
#         product_code = input("Ma hang hang hoa da ton tai. xin moi nhap lai:")
#         while len(product_code) != 4:
#             product_code = input("ma hang hoa can co 4 ky tu:")
#         id_exists = check_product(product_code)
#     id = get_lastid()
#     data["id"] = int(id) + 1
#     data["ten"] = input("xin moi nhap ten hang hoa:")
#     data["giaban"] = input("xin moi nhap gia ban:")
#     category_id = input("xin moi nhap ma loai hang hoa:")
#     get_category_id = category.check_category(category_id)
#     while get_category_id is None:
#         category.danhsach_loaihanghoa()
#         category_id = input("xin moi nhap ma loai hang hoa:")
#         get_category_id = category.check_category(category_id)
#     data["category_id"] = category_id.upper()
#     data["product_code"] = product_code.upper()
#     str_to_save = str(data["id"]) + "#" + data["ten"] + '#' + data["giaban"] + "#" +  data["category_id"] + '#' + str(0) + '#' + str(data["product_code"]) + '#' + str(date_time) + '\n'
#     with open('../Data/products.csv', 'a') as f:
#         data = f.write(str_to_save)
#     invoice.create_danhsachhanghoamua()
#     invoice.update_danhsachhanghoamua()


def create_products(product_code,ten,giaban,category_id):
    data = {}
    id = get_lastid()
    data["id"] = int(id) + 1
    data["ten"] = ten
    data["giaban"] = giaban
    data["category_id"] = category_id.upper()
    data["product_code"] = product_code.upper()
    str_to_save = str(data["id"]) + "#" + data["ten"] + '#' + data["giaban"] + "#" +  data["category_id"] + '#' + str(0) + '#' + str(data["product_code"]) + '#' + str(date_time) + '\n'
    with open('Data/products.csv', 'a') as f:
        data = f.write(str_to_save)
    invoice.create_danhsachhanghoamua()
    invoice.update_danhsachhanghoamua()



# create_products()



