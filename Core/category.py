import os



def load_category():
    list_category = []
    files = os.listdir('Data')
    if "category.csv" not in files:
        return

    with open('Data/category.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                category = {}
                category["id"] = str_to_reads[0]
                category["category_code"] = str_to_reads[1]
                category_name = str_to_reads[2]
                if category_name.endswith('\n'):
                    category_name = category_name[0:len(category_name)-1]
                category["category_name"] = category_name
                list_category.append(category)
            line = f.readline()
        return list_category
    # print("list_category:", list_category)

def check_category(category_code):
    list_category.clear()
    load_category()
    for loai in list_category:
        if loai["category_code"].upper() == category_code.upper():
            return loai

# list_category = check_category("TPH")
# print(list_category)

def get_lastid():
    list_category = load_category()
    for line in list_category:
        id = line['id']
    return id

# x = get_lastid()
# print(x)

def danhsach_loaihanghoa():
    list_category.clear()
    load_category()
    print("______________DANH SACH LOAI SAN PHAM__________________")
    print("+-------+-------------+-------------------------------+")
    print("|  STT  |   Ma Loai   |       Ten loai san pham       |")
    print("+-------+-------------+-------------------------------+")
    for x in list_category:
        print("|",x["id"].center(5),"|",x["category_code"].center(11),"|",x["category_name"].ljust(29),"|")
    print("+-------+-------------+-------------------------------+")

# danhsach_loaihanghoa()

# def create_category():
#     data = {}
#     category_code = input("xin moi nhap ma loai hang hoa:")
#     while len(category_code) != 3:
#         category_code = input("ma hang hoa can co 3 ky tu:")
#     id_exists = check_category(category_code)
#     while id_exists is not None:
#         category_code = input("Ma hang loai hang hoa da ton tai. xin moi nhap lai:")
#         while len(category_code) != 3:
#             category_code = input("ma hang hoa can co 3 ky tu:")
#         id_exists = check_category(category_code)
#     id = get_lastid()
#     data["id"] = int(id) + 1
#     data["category_code"] = category_code.upper()
#     data["category_name"] = input("Xin moi nhap ten loai hang hoa:")
#     # list_category.append(data)
#     str_to_save = str(data["id"]) + "#" + data["category_code"] + "#"  + data["category_name"] + '\n'
#     with open('../Data/category.csv', 'a') as f:
#         data = f.write(str_to_save)

# create_category()

def create_category(category_code,category_name):
    data = {}
    id = get_lastid()
    data["id"] = int(id) + 1
    data["category_code"] = category_code.upper()
    data["category_name"] = category_name
    # list_category.append(data)
    str_to_save = str(data["id"]) + "#" + data["category_code"] + "#"  + data["category_name"] + '\n'
    with open('Data/category.csv', 'a') as f:
        data = f.write(str_to_save)

# view_category()

def sua_loaihanghoa(id, data):
    pass

def xoa_loaihanghoa(id):
    pass

