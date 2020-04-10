import requests


def add_product(name, quantity):
    return requests.post(_url('products/'), json={
        'name': name,
        'quantity': quantity
    })


def add_category(name):
    return requests.post(_url('categories/'), json={
        'name': name
    })


def delete_category(category_id):
    return requests.delete(_url('/categories/{:d}/'.format(category_id)))


def delete_product(product_id):
    return requests.delete(_url('products/{:d}/'.format(product_id)))


def get_all_categories():
    return requests.get(_url('categories/'))


def get_all_products():
    return requests.get(_url('products/'))


def get_category(category_id):
    return requests.get(_url('/categories/{:d}/'.format(category_id)))


def get_product(product_id):
    return requests.get(_url('/products/{:d}/'.format(product_id)))


def update_category(category_id, name):
    url = _url('/categories/{:d}/'.format(category_id))
    return requests.put(url, json={
        'name': name
    })


def update_product(product_id, name, quantity):
    url = _url('/categories/{:d}/'.format(product_id))
    return requests.put(url, json={
        'name': name,
        'quantity': quantity
    })


def _url(path):
    return '/' + path
