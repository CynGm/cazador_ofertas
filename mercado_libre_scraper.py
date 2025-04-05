import requests
from bs4 import BeautifulSoup

def buscar_en_mercado_libre(producto):
    # Convertimos el nombre del producto para usarlo en la URL
    producto_url = producto.replace(" ", "-")
    url = f'https://listado.mercadolibre.com.mx/{producto_url}'

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}


    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        resultados = soup.find_all('li', class_='ui-search-layout__item')

        if resultados:
            primer_producto = resultados[0]

            titulo = primer_producto.h2.text
            precio = primer_producto.find('span', class_='andes-money-amount__integer').text

            print(f"🔍 Producto encontrado: {titulo}")
            print(f"💰 Precio: ${precio}")
        else:
            print("No se encontraron productos.")
    else:
        print("Error al conectar con Mercado Libre.")

# Prueba
buscar_en_mercado_libre("laptop")
