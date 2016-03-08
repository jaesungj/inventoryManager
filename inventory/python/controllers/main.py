from flask import *
from mysqlCommunicator import *
import datetime
import os
import hashlib
from verifier import *


main = Blueprint('main', __name__, template_folder='views')


@main.route('/ol6hhqwipb9/inventory/')
def main_route():	
    return render_template("index.html")



@main.route('/ol6hhqwipb9/inventory/search')
def search_product():
    
    communicator = MySQLCommunicator()
    verifier = Verifier()
    barcode = request.args.get('barcode')
    sql_stmt = "Select * from product where barcode = '%s'"%(barcode)
    print sql_stmt
    product_info = communicator.executeQuery(sql_stmt)
    response = json.jsonify(barcode = barcode, productName = product_info[0][1],currentPrice=product_info[0][2])
    response.status_code = 200

    return response



