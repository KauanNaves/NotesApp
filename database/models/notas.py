from peewee import Model, CharField, FloatField, DateTimeField
from database.database import db
from datetime import datetime

class Notas(Model): # TABELA
    nome = CharField()
    nota1 = FloatField()
    nota2 = FloatField()
    nota3 = FloatField()
    media = FloatField()
    data_registro = DateTimeField(default=datetime.now)

    class Meta:
        database = db # BANCO DE DADOS