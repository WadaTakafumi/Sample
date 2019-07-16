# -*- coding: utf-8 -*-
# Copyright © 2019 ABIST Co.,Ltd. and individual contributors. All rights reserved
# Proprietary and confidential:
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Written by Franz Weitl <f_weitl@abist.co.jp>, March 2019

"""
flask server: REST API wrapper for AutoML Anomaly Detection library; 
              back end for the anomaly detection playground GUI 
"""
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

class Todo:
    def __init__(self,content,done):
        self.content=content
        self.done=done





@app.route("/")
def index():
    return jsonify('server is running...')

'''
@app.route('/empl')
def employee():
    empl = {}
    empl["name"]={"firstName": "Bob", "lastName": "Smith"}
    empl["age"]=29
    return jsonify(empl)
'''

@app.route('/getNumberOfTodos')
def getNumTodos():
    numTodos = 3
    return jsonify(numTodos)

@app.route('/todolist')
def todolist():
    todo1=Todo("起きる",True)
    todo2=Todo("朝ごはんを食べる",False)
    todo3=Todo("学校に行く",False)
    todos=[todo1,todo2,todo3]
    todos=[todo.__dict__ for todo in todos]
    
    #todos=["起きる", "朝ごはんを食べる", "学校に行く"]
    return jsonify(todos)
    
@app.route('/todo')
def todo():
    todo1=Todo("起きる",True)

    #todo2=Todo("朝ごはんを食べる",False)
    #todo3=Todo("学校に行く",False)
    #todos=[todo1,todo2,todo3]
    #todos=["起きる", "朝ごはんを食べる", "学校に行く"]
    return jsonify(todo1.__dict__)
    

'''
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        abort(400, 'No file input field.')
    try:
        fileInfo = uploadMgr.upload(request.files['file'])
        app.logger.info("uploaded '%s'", uploadMgr.getPath(fileInfo["name"]))
        return jsonify(fileInfo)
    except fileUp.UploadError as e:
        app.logger.warning("upload failed (400):" + str(e))
        abort(400, e.args)
    except Exception as e:
        #app.logger.warning(e)
        app.logger.warning("upload failed (500):  " + str(e))
        abort(500, e.args)

@app.route('/file/<filename>', methods=['DELETE'])
def deleteFile(filename):
    try:
        deleted = uploadMgr.delete(filename)
        if deleted:
            app.logger.info("deleted file '%s'", uploadMgr.getPath(filename))
        return jsonify('file "'+ filename + '" ' + ('deleted.' if deleted else 'does not exist.'))
    except Exception as e:
        abort(500, e.args)

@app.route('/getFiles')
def getFiles():
    try:
        return jsonify(uploadMgr.getFiles())
    except Exception as e:
        abort(500, e.args)
'''

if __name__ == '__main__':
    app.run(port=5000,host='localhost', debug=True) # FIXME debug mode should be set in environment variable; see: https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app 