from datetime import date
import json

class ProductsFile():

    def __init__(self):
        pass
    
    def updated(self):
        with open('products.txt', 'r') as file:
            if str(date.today()) == file.readline().strip():
                return True
            else:
                return False

    def read_products_file(self):
        with open('products.txt', 'r') as file:
            return file.read()

    def write_products_file(self, product_dict):
        with open('products.txt', 'w') as file:
            file.write(str(date.today())+"\n")
            file.write(json.dumps(product_dict))
