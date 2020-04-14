from flask import Flask, jsonify, redirect, url_for
from my_flasgger.apiwebscrape import scrape
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

specs_dict = {
  "tags": [
    "Merchandise API"
  ],
  "parameters": [
    {
      "name": "my_key",
      "in": "path",
      "type": "string",
      "required": "true",
      "description": "KEY"
    }
  ],
  "responses": {
    "200": {
      "description": "All products",
      "schema": {
        "id": "Products_id",
        "properties": {
          "products": {
            "type": "dict",
            "description": "Products",
            "default": {"greet": "hi"}
          }
        }
      }
    }
  }
}


@app.route('/')
def turn():
    return redirect("http://localhost:5000/apidocs/")


@app.route('/<my_key>', methods=['GET'])
@swag_from(specs_dict)
def index(my_key):
    """
    Endpoint returning a list of products
    """
    if my_key in ['2', '4', '6', '8', '0']:
        products = scrape()
        return jsonify(products)
    else:
        return "An error occurred, invalid key", 500


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
