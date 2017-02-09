import datetime
from flask import Flask
from flask import request
from flask import json
from newspaper import Article

app = Flask(__name__)

@app.route("/")
def home():
    url = request.args.get('url')
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    data = {}
    data['title'] = article.title
    data['summary'] = article.summary
    data['text'] = article.text
    data['image'] = article.top_image
    data['keywords'] = article.keywords
    data['authors'] = article.authors
    if isinstance(article.publish_date, datetime.date):
        data['published'] = article.publish_date.strftime("%Y-%m-%d %H:%M:00")
    else:
        data['published'] = ""

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=38765)