import requests

def delete_category(category_id):
    pass

def delete_product(product_id):
    pass

def get_all_categories():
    return requests.get(_url('categories/'))

def get_all_products():
    return requests.get(_url('products/'))

def get_category(category_id):
    return requests.get(_url('/categories/{:d}/'.format(category_id)))

def get_product(product_id):
    pass

def update_category(category_id, product_id):
    pass

def update_product(product_id, name, quantity):
    pass

def _url(path):
    return '/' + path