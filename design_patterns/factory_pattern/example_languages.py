class EnglishLocalizer:
    def localize(self, msg):
        return msg

class FrenchLocalizer:
    def __init__(self):
        self.translations = {"car": "voiture", "bike":"bicyclette","cycle":"cyclette"}

    def localize(self, msg):
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta", "cycle": "ciclo"}

    def localize(self, msg):
        return self.translations.get(msg, msg)

def Factory(language="English"):
    localizers = {
        "English": EnglishLocalizer,
        "French": FrenchLocalizer,
        "Spanish": SpanishLocalizer,
    }
    return localizers[language]()

french = Factory("French")
print(french.localize("car"))
