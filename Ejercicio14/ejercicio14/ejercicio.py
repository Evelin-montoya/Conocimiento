class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None  # Se inicializa a None hasta que se calcule.

    def calcular_precio_de_venta(self, margen_de_venta):
        if margen_de_venta <= 0:
            raise ValueError("El margen de venta debe ser mayor que 0")
        return self.costo / (1 - margen_de_venta)

    def registrar_producto(self, callback):
        margen_de_venta = float(input("Ingrese el margen de venta del producto: "))
        self.precio_de_venta = self.calcular_precio_de_venta(margen_de_venta)
        callback(self)
        print(f"Producto {self.nombre} registrado.")

def imprimir_listado(productos):
    for id, producto in productos.items():
        print(f"ID: {id}, Nombre: {producto.nombre}, Descripción: {producto.descripcion}, Costo: {producto.costo}, Cantidad: {producto.cantidad}, Precio de Venta: {producto.precio_de_venta}")

# Ejemplo de uso:
productos = {}

def agregar_producto(producto):
    productos[producto.id] = producto

while True:
    print("1. Registrar Producto")
    print("2. Imprimir Listado de Productos")
    print("3. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        id = int(input("ID del producto: "))
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción del producto: ")
        costo = float(input("Costo del producto: "))
        cantidad = int(input("Cantidad del producto: "))
        producto = Producto(id, nombre, descripcion, costo, cantidad, 0)  # El margen de venta se establece a 0 temporalmente
        producto.registrar_producto(agregar_producto)
    elif opcion == "2":
        imprimir_listado(productos)
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intente de nuevo.")