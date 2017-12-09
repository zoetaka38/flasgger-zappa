from flask import Flask, jsonify
from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)
Swagger(app)

@app.route('/colors/<palette>/')
@swag_from('colors.yml')
def colors(palette):
    all_colors = {
        'cmyk': ['cian', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }
    if palette == 'all':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)