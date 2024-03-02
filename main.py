from flask import Flask
from infrastructure.api.rest.hotel_controller import hotel_blueprint
from infrastructure.api.rest.user_controller import user_blueprint

app = Flask(__name__)

app.register_blueprint(hotel_blueprint, url_prefix='/api')
app.register_blueprint(user_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
