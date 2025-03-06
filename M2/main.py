import re
import csv

#cargar el HTML
def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()


def extraer_productos(html):
    # buffers 
    nombres = []
    imagenes = []

    # expresión regular 
    regex_producto = re.compile(
        r'<a class="product-summary_product-summary__9uDl8.*?" .*?title="(.*?)" href=".*?">'
        r'.*?<img src="(https://cdn.kemik.gt/.*?\.jpg)".*?>', re.DOTALL
    )

    # extraer los datos y llenar los buffers
    productos_extraidos = regex_producto.findall(html)

    for nombre, imagen in productos_extraidos:
        nombres.append(nombre)
        imagenes.append(imagen)

    #centinela (zip) para emparejar correctamente los datos
    productos = list(zip(nombres, imagenes))

    return productos

# exportar los datos a un CSV
def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre del Producto", "URL de la Imagen"])
        writer.writerows(productos)

#rutas de los archivos
archivo_html = "Kemik.html"
archivo_salida_csv = "productos_kemik.csv"

html = cargar_html(archivo_html)  # Cargar el HTML
productos = extraer_productos(html)  # Extraer datos con buffers y centinelas
exportar_csv(productos, archivo_salida_csv)  # Exportar a CSV

