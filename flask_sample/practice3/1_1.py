#型指定
from flask import Flask
app = Flask(__name__)
@app.route('/foo/bar')
def get_foobar():
    return 'you got\n'
@app.route('/foo/bar/<int:baz>', methods=['POST'])
def post_foobar(baz):
    return 'you posted {}\n'.format(baz)