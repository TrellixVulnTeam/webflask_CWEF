import datetime
from Core import user, base, products
import json
import os
import shutil

now = datetime.datetime.now()
date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
date_dir = now.strftime("%d_%m_%Y")


def max_id():
    with open('../PhieuNhap/id_phieu.txt', 'r') as string:
        line = string.readline()
        if len(line) > 0:
            # print(line)
            while line:
                str_to_reads = line.lstrip("NHKH")
                #print(str_to_reads)
                line = string.readline()
            return str_to_reads
        else:
            str_to_reads = '000'
            return str_to_reads


# max_id()
# print(max_id())

def update_hanghoa(sophieu):
    with open('../PhieuNhap/' + sophieu + '.json', 'r') as f:
        phieu = json.load(f)
        date_nhap = phieu["create_date"]
        for hanghoa in phieu["danhSachHangHoa"]:
            ten = hanghoa["ten"]
            soluong = int(hanghoa["soluong"])
            # print("ket qua sau khi doc:",ten,soluong)
            shutil.copy('../Data/products.csv', '../Data/products_temp.csv')
            with open('../Data/products_temp.csv', 'r') as f:
                with open('../Data/products.csv', 'w') as wfile:
                    line = f.readline()
                    while line:
                        str_to_reads = line.split("#")
                        if len(str_to_reads) > 1:
                            if ten.upper() == str_to_reads[1].upper():
                                stt = str_to_reads[0]
                                soluong_sp_trongkho = int(str_to_reads[4])
                                dongia = str_to_reads[2]
                                category = str_to_reads[3]
                                total_soluong = soluong + soluong_sp_trongkho
                                product_code = str_to_reads[5]
                                str_to_save = str(stt) + "#" + str(ten) + "#" + str(dongia) + "#" + str(category) + "#" + str(total_soluong) + "#" +  str(product_code) + "#" + str(date_nhap) + '\n'
                                line = wfile.write(str_to_save)
                                # print(str_to_save)
                            else:
                                # print(line)
                                line = wfile.write(line)
                        line = f.readline()
                wfile.closed


# update_hanghoa("NHKH007")

def create_phieuNhapKho(email):
    soPhieu = int(max_id()) + 1
    soPhieu = str(format(soPhieu, '03d'))
    print("moi ban tao hoa don so: NHKH" + soPhieu)
    phieu={}
    phieu["soPhieu"] = "NHKH" + soPhieu
    phieu["create_date"]= date_time
    phieu["tong_tien"] = 0
    phieu["seller"]= email
    phieu["danhSachHangHoa"] = []
    stt_hanghoa = 1
    nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
    while nhaphanghoa.upper() == 'Y':
        products.danhsach_hanghoa()
        hanghoa = {}
        hanghoa["stt"] = stt_hanghoa
        id_product = base.check_id_product(int(input("nhap id hang hoa: ")))
        while id_product is None:
            id_product = base.check_id_product(int(input("ID hang hoa sai. Hay nhap lai, : ")))
            base.view_list_products()
        while id_product is not None:
            data = base.load_id_products(int(id_product))
            hanghoa["ten"] = data[0]
            hanghoa["soluong"] = int(input("nhap so luong: "))
            hanghoa["dongia"] = int(data[1])
            hanghoa["thanhtien"] = hanghoa["soluong"] * hanghoa["dongia"]
            phieu["danhSachHangHoa"].append(hanghoa)
            phieu["tong_tien"] = hanghoa["thanhtien"] + phieu["tong_tien"]
            break 
        nhaphanghoa = input("=> Ban co muon nhap tiep hang hoa khong (y/n): ")
        stt_hanghoa += 1

    filename = "NHKH" + soPhieu +".json"
    with open('../PhieuNhap/' + filename, 'w') as f:
        json.dump(phieu, f)
    data = open("../PhieuNhap/id_phieu.txt", "a")
    data.write("NHKH" + soPhieu +"\n")
    update_hanghoa("NHKH" + soPhieu)




# create_phieuNhapKho('admin@123.com')

def file_name_exists():
    sophieu = ''
    while not os.path.isfile('../PhieuNhap/'+ sophieu +'.json'):
        sophieu = input("nhap so phieu nhap can xem:")  
    return sophieu

# sophieu = file_name_exists()
# print(sophieu)

def view_phieu():
    sophieu = file_name_exists()
    with open('../PhieuNhap/' + sophieu + '.json', 'r') as f:
        phieu = json.load(f)
        # print(invoice)
        # for hoadon in invoice:
        #Hoa don se in o day
        print("                          PHIEU NHAP HANG                                  ")
        print("So Phieu:",phieu["soPhieu"])
        print("Ngay Nhap:",phieu["create_date"])
        print("Nguoi Nhap Kho:",phieu["seller"])
        print("Tong Tien:",str(phieu["tong_tien"]))
        print("___________________________THONG TIN HANG HOA NHAP_______________________________")
        print("+-------+-------------------------+----------+---------------+------------------+")
        print("|  STT  |         hang hoa        | so luong |    don gia    |    thanh tien    |")
        print("+-------+-------------------------+----------+---------------+------------------+")
                    
        for hanghoa in phieu["danhSachHangHoa"]:
        #print("In dong hang hoa o day")
            print("|",str((hanghoa['stt'])).center(5),"|" ,hanghoa['ten'].rjust(23), "|",str(hanghoa['soluong']).center(8),"|",str(hanghoa['dongia']).center(13),"|",str(hanghoa['thanhtien']).center(16),"|")
        print("+-------+-------------------------+----------+---------------+------------------+")
        #end of Hoa don se in o day

# view_phieu()


