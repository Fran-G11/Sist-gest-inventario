inventario = {}

while True:
    print("\n--- Menú de Inventario ---")
    print("1. Agregar o actualizar un producto")
    print("2. Ver todos los productos")
    print("3. Calcular valor total del inventario")
    print("4. Buscar un producto")
    print("5. Eliminar unidades de un producto")
    print("6. Eliminar todas las existencias de un producto")
    print("7. Salir")
    
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == "1":
        # Agregar o actualizar un producto
        nombre = input("Ingrese el nombre del producto: ").strip().lower()
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad disponible: "))
            inventario[nombre] = {"precio": precio, "cantidad": cantidad}
            print(f"Producto '{nombre}' agregado o actualizado.")
        except ValueError:
            print("Error: Ingrese valores numéricos válidos para precio y cantidad.")
    
    elif opcion == "2":
        # Ver todos los productos
        if not inventario:
            print("El inventario está vacío.")
        else:
            print("\n--- Productos en Inventario ---")
            for nombre, datos in inventario.items():
                print(f"{nombre}: Precio = ${datos['precio']:.2f}, Cantidad = {datos['cantidad']}")
    
    elif opcion == "3":
        # Calcular valor total del inventario
        valor_total = sum(datos["precio"] * datos["cantidad"] for datos in inventario.values())
        print(f"El valor total del inventario es: ${valor_total:.2f}")
    
    elif opcion == "4":
        # Buscar un producto específico
        nombre = input("Ingrese el nombre del producto a buscar: ").strip().lower()
        if nombre in inventario:
            datos = inventario[nombre]
            print(f"{nombre}: Precio = ${datos['precio']:.2f}, Cantidad = {datos['cantidad']}")
        else:
            print(f"Error: El producto '{nombre}' no existe en el inventario.")
    
    elif opcion == "5":
        # Eliminar unidades de un producto
        nombre = input("Ingrese el nombre del producto: ").strip().lower()
        if nombre in inventario:
            try:
                cantidad_a_eliminar = int(input("Ingrese la cantidad a eliminar: "))
                if cantidad_a_eliminar <= inventario[nombre]["cantidad"]:
                    inventario[nombre]["cantidad"] -= cantidad_a_eliminar
                    print(f"Se eliminaron {cantidad_a_eliminar} unidades de '{nombre}'.")
                    # Si el stock llega a 0, eliminar el producto
                    if inventario[nombre]["cantidad"] == 0:
                        del inventario[nombre]
                        print(f"Producto '{nombre}' eliminado del inventario por falta de stock.")
                else:
                    print(f"Error: No hay suficientes unidades. Solo hay {inventario[nombre]['cantidad']} disponibles.")
            except ValueError:
                print("Error: Ingrese un número válido para la cantidad.")
        else:
            print(f"Error: El producto '{nombre}' no existe en el inventario.")
    
    elif opcion == "6":
        # Eliminar todas las existencias de un producto
        nombre = input("Ingrese el nombre del producto a eliminar: ").strip().lower()
        if nombre in inventario:
            del inventario[nombre]
            print(f"Producto '{nombre}' eliminado del inventario.")
        else:
            print(f"Error: El producto '{nombre}' no existe en el inventario.")
    
    elif opcion == "7":
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
