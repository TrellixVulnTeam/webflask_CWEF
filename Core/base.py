import os
import json

def load_id_products(id):
    files = os.listdir("Data")
    if "products.csv" not in files:
        return

    with open('Data/products.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                #products["id"] = str_to_reads[0]
                if int(str_to_reads[0]) == id:
                    products = {}
                    products["id"] = str_to_reads[0]
                    products["ten"] = str_to_reads[1]
                    products["giaban"] = str_to_reads[2]
                    products["category_id"] = str_to_reads[3]
                    if products["category_id"].endswith('\n'):
                        products["category_id"] = products["category_id"][0:len(products["category_id"])-1]
            line = f.readline()

    #print("list_products:", products)
    return products["ten"],products["giaban"]

# load_id_products(2)
# print (load_id_products(2))




def load_name_products(name_product):
    files = os.listdir("Data")
    if "products.csv" not in files:
        return

    with open('Data/products.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                if str_to_reads[1].upper() == name_product.upper():
                    products = {}
                    products["id"] = str_to_reads[0]
                    products["ten"] = str_to_reads[1]
                    products["giaban"] = str_to_reads[2]
                    products["category_id"] = str_to_reads[3]
                    if products["category_id"].endswith('\n'):
                        products["category_id"] = products["category_id"][0:len(products["category_id"])-1]
            line = f.readline()

    #print("list_products:", products)
    return products["ten"],products["giaban"]




def view_list_products():
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
                if products["category_id"].endswith('\n'):
                    products["category_id"] = products["category_id"][0:len(products["category_id"])-1]
                print( products["id"],"\t",products["ten"].ljust(20),"\t",products["giaban"],"\t",products["category_id"] )
            line = f.readline()
    return view_list_products

#view_list_products()

def check_id_product(id):
    with open('Data/products.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            products = {}
            products["id"] = str_to_reads[0]
            #print(products["id"])
            if int(products["id"]) == int(id):
                #print(products["id"])
                return products["id"]
            line = f.readline()
            


# check_id_product(2)
# print(check_id_product(4))


id_list = []
def get_id(path):
    id_dict = {}
    if os.stat(path).st_size == 0:
        id_dict["id"] = '0'
        id_list.append(id_dict)
        return id_dict
    else:
        with open(path, 'r') as f:
            line = f.readline()
            while line:
                str_to_reads = line.split("#")
                # print(str_to_reads[0])
                id_dict["id"] = str_to_reads[0]
                line = f.readline()
            id_list.append(id_dict)
        # print(id_dict["id"])
        return id_dict


# get_id('../Data/seller_user.csv')
# print(id_list)





files = []
def load_all_file(path):
    files.clear()
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.json' in file:
                files.append(os.path.join(r, file))
    return files

list_sale_product = []
def count_sale_product(product_name,total_sale):
    for f in files:
        with open(f, 'r') as line:
            invoice = json.load(line)
            for hanghoa in invoice["danhsachhanghoa"]:
                if hanghoa['ten'] == product_name:
                    total_sale = total_sale + hanghoa['soluong']
    count_sale_product1 = {}
    count_sale_product1['product_name'] = product_name
    count_sale_product1['total_sale'] = total_sale
    list_sale_product.append(count_sale_product1)
    # return list_sale_product


def total_sale_for_products():
    load_all_file('../HoaDon/')
    with open('../Data/products.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                products = {}
                products["ten"] = str_to_reads[1]
                total_sale = 0
                count_sale_product(products["ten"],total_sale)
            line = f.readline()



def top_sale_products():
    total_sale_for_products()
    max_list = max(list_sale_product, key=lambda x:x['total_sale'])
    min_list = min(list_sale_product, key=lambda x:x['total_sale'])
    print("______SAN PHAM BAN TOT NHAT_______")
    print("+----------------+---------------+")
    print("|", max_list['product_name'].ljust(14), "|" , str(max_list['total_sale']).ljust(13),"|" )
    print("+----------------+---------------+")
    print("______SAN PHAM BAN IT NHAT________")
    print("+----------------+---------------+")
    print("|", min_list['product_name'].ljust(14), "|" , str(min_list['total_sale']).ljust(13),"|" )
    print("+----------------+---------------+")
    list_sale_product.clear()

# top_sale_products()

list_money_product = []
def count_money_product(product_name,total_money):
    for f in files:
        with open(f, 'r') as line:
            invoice = json.load(line)
            for hanghoa in invoice["danhsachhanghoa"]:
                if hanghoa['ten'] == product_name:
                    total_money = total_money + hanghoa['thanhtien']
    count_money_product1 = {}
    count_money_product1['product_name'] = product_name
    count_money_product1['total_money'] = total_money
    list_money_product.append(count_money_product1)


def total_money_for_products():
    load_all_file('../HoaDon/')
    with open('../Data/products.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                products = {}
                products["ten"] = str_to_reads[1]
                total_money = 0
                count_money_product(products["ten"],total_money)
            line = f.readline()




def top_revenue():
    total_money_for_products()
    print("________TOP SACH DOANH THU________")
    print("+----------------+---------------+")
    print("|  Ten san pham  |   Doanh Thu   |")
    print("+----------------+---------------+")
    for x in list_money_product:
        print("|", x['product_name'].ljust(14), "|" , str(x['total_money']).ljust(13),"|" )
    print("+----------------+---------------+")
    max_list = max(list_money_product, key=lambda x:x['total_money'])
    min_list = min(list_money_product, key=lambda x:x['total_money'])
    print("______SAN PHAM BAN TOT NHAT_______")
    print("+----------------+---------------+")
    print("|", max_list['product_name'].ljust(14), "|" , str(max_list['total_money']).ljust(13),"|" )
    print("+----------------+---------------+")
    print("______SAN PHAM BAN IT NHAT________")
    print("+----------------+---------------+")
    print("|", min_list['product_name'].ljust(14), "|" , str(min_list['total_money']).ljust(13),"|" )
    print("+----------------+---------------+")
    list_money_product.clear()

# top_revenue()

