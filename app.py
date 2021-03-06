from flask import Flask, request, jsonify, render_template, session, redirect, url_for, escape
from controllers import url_controller, db_controller
import os, json, threading, time
import pandas as pd
import numpy as np
from datetime import datetime
from models import room as t_rom, account, request_item

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = db_controller.getDB()
# timeRoom = t_rom.initTimeRoom()
indexRoom = t_rom.createIndexRoom()
primaryItemId = ["" for _ in range(5)]

@app.route("/dang-nhap", methods=["GET"])
def renderPageLogin():
    return render_template('render/login.html')

@app.route("/submit-dang-nhap", methods=["POST"])
def login():
    return url_controller.submitLogin()

@app.route("/dang-xuat", methods=["GET"])
def logout():
    return url_controller.logout()

@app.route("/submitSignup", methods=["POST"])
def submitSignup():
    return account.submitSignup()

@app.route("/checkAccount/<username>", methods=["GET"])
def checkAccount(username):
    return app.response_class(json.dumps({"result": db_controller.checkAccount(username)}), mimetype='application/json')

@app.route("/cac-phong-dau-gia", methods=["GET"])
def rooms():
    return render_template('render/category.html')

@app.route("/phong-dau-gia/<loaiphong>", methods=["GET"])
def room(loaiphong):
    session["typeroom"] = loaiphong
    return render_template('render/bid.html')

@app.route("/", methods=["GET"])
def home():
    return url_controller.homeController()

@app.route("/dang-ky", methods=["GET"])
def signup():
    return render_template('render/signup.html')

# ben B tra gia san pham
@app.route("/tra-gia", methods=["POST"])
def bid():
    return db_controller.bid()

@app.route("/tra-gia-db/<typeroom>", methods=["POST"])
def biddb(typeroom):
    return t_rom.bid(typeroom)

@app.route("/so-du", methods=["GET"])
def getAccountBalance():
    return db_controller.getAccountBalance()

@app.route("/san-pham-chinh/<loaiphong>", methods=["GET"])
def getItem(loaiphong):
    return db_controller.getPrimaryItemInRoom(loaiphong)

@app.route("/createRoom/<loaiphong>", methods=["GET"])
def createRoom(loaiphong):
    return t_rom.createRoom(loaiphong)

@app.route("/pricemax-time-db/<loaiphong>", methods=["GET"])
def getPricemaxTimedb(loaiphong):
    return t_rom.getPricemaxTimedb(loaiphong)

@app.route("/pricemax-time/<loaiphong>", methods=["GET"])
def getPricemaxTime(loaiphong):
    return db_controller.getPricemaxTime(loaiphong)

@app.route("/chi-tiet-san-pham/<id>", methods=["GET"])
def getDetailItem(id):
    db_controller.checkToSaveInfo(id)
    return render_template('render/detail_item.html')

@app.route("/thong-tin-san-pham/<id>", methods=["GET"])
def getInfoItem(id):
    return db_controller.getInfoItem(id)

@app.route("/thong-tin-ben-a/<id>", methods=["GET"])
def getInfoAuctioneer(id):
    return db_controller.getInfoAuctioneer(id)

@app.route("/san-pham-tiep-theo/<loaiphong>", methods=["GET"])
def nextItem(loaiphong):
    return db_controller.nextItem(loaiphong)

@app.route("/lich-su-dau-gia", methods=["GET"])
def historyAuction():
    return url_controller.historyAuction()

@app.route("/getNameAccount", methods=["GET"])
def getNameAccount():
    return account.getNameAccount()

# tim gio cua file category
@app.route("/getTimeRemaining", methods=["GET"])
def timeRemaining():
    return t_rom.timeRemaining()

@app.route("/getItemInRoom/<loaiphong>", methods=["GET"])
def getItemInRoom(loaiphong):
    return t_rom.getItemInRoom(loaiphong)

@app.route("/chinh-sua-thong-tin", methods=["GET"])
def editAccount():
    return url_controller.editAccount()

@app.route("/ben-a", methods=["GET"])
def benA():
    return render_template('render/account_a.html')

@app.route("/getInfoBidder", methods=["GET"])
def getInfoBidder():
    return account.getInfoBidder()

@app.route("/setInfoBidder", methods=["POST"])
def setInfoBidder():
    return account.setInfoBidder()

@app.route("/getAllHistoryAuction", methods=["GET"])
def getAllHistoryAuction():
    return account.getAllHistoryAuction()

@app.route("/ben-c", methods=["GET"])
def benC():
    return render_template('render/account_c.html')

@app.route("/getAllRequestFromA", methods=["GET"])
def getAllRequestFromA():
    return request_item.getAllRequestFromA(session["id"])

@app.route("/createRequestFromA", methods=["POST"])
def createRequestFromA():
    return request_item.createRequestFromA()

@app.route("/getIdAuctioneer", methods=["GET"])
def getIdAuctioneer():
    return account.getIdAuctioneer()

@app.route("/getAllRequestFromC", methods=["GET"])
def getAllRequestFromC():
    return request_item.getAllRequestFromC()

@app.route("/acceptRequest", methods=["POST"])
def acceptRequest():
    return request_item.acceptRequest()

@app.route("/refuseRequest/<id>", methods=["GET"])
def refuseRequest(id):
    return request_item.refuseRequest(id)

@app.route("/xoaTaiKhoan/<username>", methods=["GET"])
def deleteAccount(username):
    return account.deleteAccount(username)

@app.route("/filterItem", methods=["POST"])
def filterItem():
    return request_item.filterItem()

@app.route("/test", methods=["GET"])
def test():
    # now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # return app.response_class(json.dumps([{"test": str(dt_string)}]),mimetype='application/json')
    return render_template('render/account_c_old.html')

if __name__ == "__main__":
    app.run(debug=True)