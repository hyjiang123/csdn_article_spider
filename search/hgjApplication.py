from flask import Flask, request, jsonify

from searchcsdnspider import CSDN

app = Flask(__name__)

scraped_data = []

# def start_spider(keyword):


@app.route('/search', methods=['GET'])
def search():
    # 从请求参数中获取 keyword
    keyword = request.args.get('keyword')
    page = request.args.get('page')

    result = CSDN(search_keyword=keyword, search_page=page).main()

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False)
