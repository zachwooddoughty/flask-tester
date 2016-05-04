import os

from flask import Flask, request, redirect, render_template


app = Flask(__name__)

tags_dict = {
    'cat': {'title': 'Cool cats', 'description': 'These cats are very cool'},
    'dog': {'title': 'Bad dogs', 'description': 'These dogs are bad af'},
}

@app.route('/<path:path>')
def fallback(path=None):
    return render_template("test.html", tags=tags_dict.get(path))

@app.route('/')
def base():
    return app.send_static_file("test.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.config['FLASKS3_BUCKET_NAME'] = "discoverboard"
    app.run(host='0.0.0.0', port=port)
