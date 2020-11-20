# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    """returns sum of a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return (str(add(a,b)))

@app.route('/sub')
def sub_nums():
    """Subtracts b from a"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return (str(sub(a,b)))

@app.route('/mult')
def mult_nums():
    """Multiplies a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return (str(mult(a,b)))

@app.route('/div')
def div_nums():
    """Divide a by b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return (str(div(a,b)))



operations = {"add": add, "sub": sub, "mult": mult, "div":div}


@app.route('/math/<operation>')
def all_operations(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(operations[operation](a,b))







    

