import os
from Core import category, products, invoice, base, user, phieunhapkho


          
def menuDiplayAdmin(email):
    print("+--------------MENU-----------------+")
    print("|Chon 1 de tao account seller       |")
    print("|Chon 2 de update thông tin seller  |")
    print("|Chon 3 de deactive account seller  |")
    print("|Chon 4 list danh sách SELLER       |")
    print("|Chon 5 list danh sách BUYER        |")
    print("|Chon 6 de vao QUAN LY HOA DON      |")
    print("|Chon E de logout                   |")
    print("+-----------------------------------+")
    print(email)
    while True:
        x=input("=> chon chuc nang:")
        print("=> ban da chon chuc nang:",x)
        if x == '1':
            user.newUserSeller()
        if x == '2':
            user.updateUserSeller()
        if x == '3':
            user.deactiveUserSeller()
        if x == '4':
            user.readUserSeller()
        if x == '5':
            user.readUserBuyer()
        if x == '6':
            menuDiplayClient(email)
            break
        if x.upper() == 'E':
            print("Tam biet! Hen gap lai")
            break


def menuDiplayClient(email):
    print("+--------------MENU---------------------+")
    print("|Chon THH de tao hang hoa               |")
    print("|Chon XHH de xem hang hoa trong kho     |")
    print("|Chon TLH de tao loai hang hoa          |")
    print("|Chon XLH de xem loai hang hoa          |")
    print("|Chon NHH de nhap hang hoa moi vao kho  |")
    print("|Chon XPH de xem phieu nhap hang        |")
    print("|Chon HHB de xem danh sach hang da ban  |")
    print("|Chon C de tao hoa don                  |")
    print("|Chon R de xem thong tin hoa don        |")
    print("|Chon T de tinh tong doanh thu          |")
    print("|Chon A de tinh tong hang hoa ban ra    |")
    print("|Chon E de thoat                        |")
    print("+---------------------------------------+")
    print(email)

    products.load_products()
    category.load_category()

    while True:
        x=input("=> chon chuc nang:")
        print("=> ban da chon chuc nang:",x)
        if x.upper() == 'TLH':
            category.create_category()
        if x.upper() == 'XLH':
            category.danhsach_loaihanghoa()
        if x.upper() == 'THH':
            products.create_products()
        if x.upper() == 'XHH':
            products.danhsach_hanghoa()
        if x.upper() == 'NHH':
            phieunhapkho.create_phieuNhapKho(email)
        if x.upper() == 'XPH':
            phieunhapkho.view_phieu()
        if x.upper() == 'HHB':
            invoice.danhsach_hanghoaban()
        if x.upper() == 'C':
            invoice.create_invoice()
        if x.upper() == 'R':
            invoice.view_invoice()
        if x.upper() == 'T':
            base.top_revenue()
        if x.upper() == 'A':
            base.top_sale_products()
        if x.upper() == 'E':
            print("Tam biet! Hen gap lai")
            break
            