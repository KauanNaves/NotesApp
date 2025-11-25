from flask import Flask
from configuration import configure_all

app = Flask(__name__) # Criando a aplicação Flask

configure_all(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)