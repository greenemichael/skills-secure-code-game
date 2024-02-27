# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class TaxPayer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        # assume that image is returned on screen after this
        return getPath(path)

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        # assume that tax data is returned on screen after this
        return getPath(path)
        
def getPath(fileName=None):
    if not fileName:
        raise Exception("Missing file name when requesting to open a file")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.normpath(os.path.join(base_dir, fileName))
    return filepath if base_dir == os.path.commonpath([base_dir, filepath]) else None

def getBufferReader(fileName=None):
    filePath = getPath(fileName)
    return open(getPath(fileName), 'rb') if filePath else None