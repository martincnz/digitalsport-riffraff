from bs4 import BeautifulSoup, SoupStrainer
from multiprocessing import Pool
from timeit import default_timer as timer
import requests as req
from ProductsFile import ProductsFile

def process_products(soup):
    prods_dict = {}
    for prod in soup:
        aux = {}
        aux["Nombre"] = prod["data-title"]
        aux["Precio"] = prod["data-price"]
        aux["SKU"] = prod["data-sku"]

        prod_info = {}
        prod_info[prod["data-brand"]] = aux

        prods_dict[prod["productid"]] = prod_info
    return prods_dict


def scrape_products(page):
    r = req.get(f'https://www.digitalsport.com.ar/search/?page={page}').text
    soup = BeautifulSoup(r, features='html.parser', parse_only=SoupStrainer('a',{'class':'product'}))
    prods_dict = process_products(soup)
    return prods_dict

if __name__ == '__main__':
    start = timer()
    file = ProductsFile()
    if file.updated():
        prods = file.read_products_file()
        print("... Reading products from file ...")
    else:
        print("... Scraping products from website ...")
        with Pool(30) as p:
            prods = p.map(scrape_products, list(range(0,210)))
        file.write_products_file(prods)

    end = timer()
    #print(prods)
    print(end - start)









