# app.py
import os.path
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from Core import QuanLyHoaDon, invoice, category, products, user
import json
import shutil

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect('/menu')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    login = QuanLyHoaDon.Login(request.form['username'],request.form['password'])
    if login is True:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route("/invoice")
def view_invoices():
    lines = invoice.list_invoice()
    data = invoice.view_invoice("IN001")
    return render_template('invoice.html', invoice = data, lines = lines )

@app.route("/invoice/<path:sub_path>")
def take_to_subpath(sub_path):
    invoice.create_file_invoice(sub_path)
    # Accepts any string with slashes.
    # print(sub_path)
    lines = invoice.list_invoice()
    data = invoice.view_invoice(sub_path)
    # return data
    return render_template('invoice.html', invoice = data, lines = lines )



# data = take_to_subpath("IN002")
# print(data)

@app.route("/createinvoice",methods=['GET', 'POST'])
def createinvoice():
    if request.method == 'GET':
        return render_template('createinvoice.html')
    else:
        phone = request.form['phone']
        print(phone)
        data = user.check_buyer(phone)
        print(data)
        if data is not None:
            max_id = int(invoice.max_id()) + 1
            new_id = "IN" + str(format(max_id,'03d'))
            # return render_template('createinvoice.html', new_id = new_id, phone= data )
            return redirect(url_for('createinvoice_addproduct',new_id = new_id, phone= data))
        else:
            return redirect('/createbuyer')

@app.route("/createinvoice/listproduct")
def createinvoice_listproduct():
    product_list = products.load_products()
    response = app.response_class(
        response=json.dumps(product_list),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/createinvoice/addproduct",methods=['GET', 'POST'])
def createinvoice_addproduct():
    invoice_ojb = {}
    if request.method == 'GET':
        invoice_ojb["sohoadon"] = request.args.get('new_id', '')
        invoice_ojb["phone"] = request.args.get('phone', '')
        invoice.session_cache(invoice_ojb["sohoadon"],invoice_ojb)
        invoice_data = invoice.load_session_cache(invoice_ojb["sohoadon"])
        return render_template('addcustomer.html', invoice_id = invoice_data["sohoadon"], phone= invoice_data["phone"], data = invoice_data  )
    else:
        invoice_ojb["sohoadon"] = request.form['invoice_id']
        invoice_data = invoice.load_session_cache(invoice_ojb["sohoadon"])
        invoice_ojb["phone"] = invoice_data["phone"]
        invoice_ojb["hanghoa"] = request.form['hanghoa']
        invoice_ojb["soluong"] = request.form['soluong']
        invoice_data = invoice.create_invoice(invoice_ojb["sohoadon"],invoice_ojb["phone"],"1",invoice_ojb["hanghoa"],invoice_ojb["soluong"])
        print(invoice_data)
        invoice.session_cache(invoice_ojb["sohoadon"],invoice_data)
        return render_template('addproduct.html', invoice_id = invoice_data["sohoadon"], phone= invoice_data["phone"], data = invoice_data)


# @app.route("/createinvoice", ,methods=['GET', 'POST'])
# def createinvoice_sub():
#     max_id = int(invoice.max_id()) + 1
#     new_id = "IN" + str(format(max_id,'03d'))
#     phone = request.form['phone']
#     phone_data = user.check_buyer("phone")
#     if phone_data.upper() == phone.upper():
#         return render_template('createinvoice.html', new_id = new_id, phone = phone)
#     else:
#         return redirect('/createbuer')




@app.route('/createbuyer',methods=['GET', 'POST'])
def createbuyer():
    if request.method == 'GET':
        data = user.readUserBuyer()
        # print(data)
        return render_template('createbuyer.html', readListUserBuyer= data)
    else:
        phone = request.form['phone']
        name = request.form['name']
        data = user.check_buyer(phone)
        print (data)
        if data is not None:
            detailPhone = user.readOneUserBuyer(data)
            return render_template('createbuyer.html', readListUserBuyer= detailPhone, Note = "Số điện thoại này đã được đăng ký")
        else:
            user.newBuyer(phone,name)
            detailPhone = user.readOneUserBuyer(phone)
            return render_template('createbuyer.html', readListUserBuyer= detailPhone, Note = "Tạo thành công Buyer")


@app.route("/createproduct/listcategory")
def listcategory():
    category_list = category.load_category()
    response = app.response_class(
        response=json.dumps(category_list),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/createproduct",methods=['GET', 'POST'])
def createproduct():
    if request.method == 'GET':
        category_list = category.load_category()
        return render_template('createproduct.html', category_list = category_list)
    else:
        name = request.form['name']
        codename = request.form['codename']
        codecategory = request.form['codecategory']
        price = request.form['price']
        products.create_products(codename,name,price,codecategory)
        products_list = products.load_products()
        return render_template('dansachhanghoa.html', products_list = products_list)

@app.route("/createcategory",methods=['GET', 'POST'])
def createcategory():
    if request.method == 'GET':
        return render_template('createcategory.html')
    else:
        category_name = request.form['name']
        category_code = request.form['codename']
        category.create_category(category_code,category_name)
        category_list = category.load_category()
        return render_template('danhsachloaihanghoa.html', category_list = category_list)



@app.route("/dansachhanghoa",methods=['GET', 'POST'])
def dansachhanghoa():
    if request.method == 'GET':
        products_list = products.load_products()
        return render_template('dansachhanghoa.html', products_list = products_list)
    else:
        return OK


@app.route("/danhsachloaihanghoa")
def danhsachloaihanghoa():
    if request.method == 'GET':
        category_list = category.load_category()
        return render_template('danhsachloaihanghoa.html', category_list = category_list)
    else:
        return OK


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host="0.0.0.0",debug=True)
