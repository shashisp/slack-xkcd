import os
import xkcd
from flask import Flask, request, Response, redirect

app = Flask(__name__)


@app.route('/', methods=['get'])
def xkcd():
	import xkcd
	return xkcd.getRandomComic().link

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)