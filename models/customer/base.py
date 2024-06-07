from django.db import models


class ModelGenerator:
    def __init__(self, fields, db_table):
        self.fields = fields
        self.db_table = db_table
        self.model = self.create_model()

    def create_model(self):
        # Meta sınıfını dinamik olarak oluşturun
        class Meta:
            db_table = self.db_table

        # Model sınıfı için attribute'ları oluşturun
        attrs = {
            '__module__': self.__class__.__module__,
            'Meta': Meta,
        }
        attrs.update(self.fields)

        # Yeni model sınıfını dinamik olarak oluşturun
        model = type(self.db_table.capitalize(), (models.Model,), attrs)
        return model
