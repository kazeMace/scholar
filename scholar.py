from flask import Flask,jsonify
from scholar_search import search_scholar

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get/baidu_scholar/<wd>/<page>',methods=['GET'])
def get_scholar(wd, page):
    data = search_scholar(wd, page)
    return jsonify({'data':data})
if __name__ == '__main__':
    app.run()
