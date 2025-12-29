from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def create(self):
        pass

class PDFDocument(Document):
    def create(self):
        return "PDF document created."

class WordDocument(Document):
    def create(self):
        return "Word document created."

class ExcelDocument(Document):
    def create(self):
        return "Excel document created."

class DocumentCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def create_document(self):
        document = self.factory_method()
        return document.create()

class PDFCreator(DocumentCreator):
    def factory_method(self):
        return PDFDocument()

class WordCreator(DocumentCreator):
    def factory_method(self):
        return WordDocument()

class ExcelCreator(DocumentCreator):
    def factory_method(self):
        return ExcelDocument()

# Usage
pdf_creator = PDFCreator()
print(pdf_creator.create_document())

excel_creator = ExcelCreator()
print(excel_creator.create_document())
