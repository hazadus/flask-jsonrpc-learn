# flask-json-rpc-learn

JSON-RPC demo app.

Browsable API available at: http://127.0.0.1:5000/api/browse/

## Sample requests

```bash
curl -i -X POST  -H "Content-Type: application/json; indent=4" \
  -d '{
    "jsonrpc": "2.0",
    "method": "App.sum",
    "params": {
        "x": 1,
        "y": 2
    },
    "id": "1"
  }' http://127.0.0.1:5000/api
```

Sample response:

```http request
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.12.1
Date: Mon, 26 Feb 2024 09:30:59 GMT
Content-Type: application/json
Content-Length: 51
Connection: close

{
  "id": "1",
  "jsonrpc": "2.0",
  "result": 3
}
```

## References

- https://www.jsonrpc.org/specification
- https://github.com/cenobites/flask-jsonrpc