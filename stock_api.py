import request_data as rd
from flask_cors import CORS
from flask import Flask,render_template,request,jsonify
app=Flask(__name__)
cors = CORS(app, resources={r"/StockData": {"origins": "*"}})
#print(help(Flask))
#print(help(app))
#print(rd.stockData())
@app.route('/StockData')
def api_func():
    #return "<pre>" +rd.stockData() + "</pre>"
    return "<pre>" +rd.stockData() + "</pre>"
    #return "hello_world"

#print(__name__)
if __name__== '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)