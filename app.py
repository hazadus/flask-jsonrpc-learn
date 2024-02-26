from flask import Flask
from flask_jsonrpc import JSONRPC
from flask_jsonrpc.exceptions import JSONRPCError

app = Flask("application")
jsonrpc = JSONRPC(app, "/api", enable_web_browsable_api=True)


@jsonrpc.method("App.sum")
def sum_(x: int, y: int) -> int:
    """Return sum of x and y."""
    return x + y


@jsonrpc.method("App.subtract")
def subtract(x: int, y: int) -> int:
    """Return difference of x and y."""
    return x - y


@jsonrpc.method("App.multiply")
def multiply(x: int, y: int) -> int:
    """Return x multiplied by y."""
    return x * y


@jsonrpc.method("App.divide")
def divide(x: int, y: int) -> float:
    """Return x divided by y."""
    if y == 0:
        error = JSONRPCError()
        error.code = -32602  # "Invalid method parameter(s)."
        error.status_code = 400
        error.data = {"message": "Can't divide by zero!"}
        raise error
    return x / y


@jsonrpc.method("App.pow")
def pow_(x: int, y: int) -> int:
    """Return x ** y."""
    return x**y


if __name__ == "__main__":
    app.run(debug=True)
