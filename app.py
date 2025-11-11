from flask import Flask
from routes.main_routes import main_routes
from routes.students_routes import studants_routes 

app = Flask(__name__) # Criando a aplicação Flask

# Registrando rotas dos blueprints
app.register_blueprint(main_routes)
app.register_blueprint(studants_routes)


if __name__ == '__main__':
    from database.connection import create_table_notes
    create_table_notes()
    app.run(host='0.0.0.0', port=10000)