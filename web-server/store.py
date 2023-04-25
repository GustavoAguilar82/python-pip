import requests

def get_categories():
    r= requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    #status_code es el estado
    print(r.text)
    #.text es la respuesta en formato string
    categories= r.json()
    for category in categories:
        print(category["name"])