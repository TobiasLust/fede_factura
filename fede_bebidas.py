from datetime import date

## PARA MAÑANA EDITAR LAS FUNCIONES DE CREAR PRODUCTO Y CREAR BOLETA. Crear funcion para editar boleta


# Crear boleta con los datos Client, day, products[], total
def create_order():
    # order = True Por ahora no me sirve
    products = []
    client = input("Cliente: ")
    day = date.today()

    while True:  # Puede ser una variable luego
        print("")

        if len(products) > 0:
            print("Cant    Producto         Unit     Subtotal")
            for i, product in enumerate(products):
                print(
                    f"{i+1} {product['amount']:<8}{product['product']:<16}{product['unit_price']:<9}{product['subtotal']}"
                )

        print("")

        user_action = input(
            "1- Agregar Producto\n2- Borrar Producto\n4- Editar producto\n5- Terminar pedido"
        )

        print("")

        match user_action:
            case "1":
                products.append(create_product())
            case "2":
                if len(products) > 0:
                    products.pop(eliminate_order(products))
                else:
                    print("No hay productos para eliminar")
            case "3":
                if len(products) > 0:
                    user_select = int(
                        input(f"Producto para editar (1 - {len(products)}): ")
                    )
                    products[user_select - 1] = edit_product(products[user_select - 1])

                else:
                    print("No hay pedidos para editar")

            case "4":
                return {
                    "client": client,
                    "day": day.strftime("%d-%m-%Y"),
                    "products": products,
                    "total": sum(product["subtotal"] for product in products),
                }
            case _:
                print("Opción no válida.")


# Crear y agregar a products[] con datos de Amount, product, unit_price, subtotal
def create_product():
    amount = input("Cantidad: ")
    product = input("Producto: ")
    unit_price = float(input("Precio: "))
    subtotal = unit_price * float(amount)
    return {
        "amount": amount,
        "product": product,
        "unit_price": unit_price,
        "subtotal": subtotal,
    }


# Eliminar el producto si es que existen
def eliminate_order(products):
    user_select = int(input("Producto para eliminar (1 - {}): ".format(len(products))))
    if 1 <= user_select <= len(products):
        return user_select - 1
    else:
        print("Selección no válida.")
        return -1


# Editar boleta


# Editar producto
def edit_product(product):
    new_product = product.copy()
    user_choice = input(f"Que deseas cambiar {new_product.keys()} ")

    if user_choice in new_product.keys():
        if user_choice == "unit_price" :
            new_product[user_choice] = float(input(f"{user_choice.title()}: "))
            new_product["subtotal"] = int(new_product["amount"]) * new_product["unit_price"]
        else:
            new_product[user_choice] = input(f"{user_choice.title()}: ")
    else:
        print("No existe.")

    return new_product


# Visualizar la boleta ( proximamente impresion de pdf )
def print_order(order):
    print(f"Cliente: {order['client']}   Fecha: {order['day']}")
    print("Cant    Producto         Unit     Subtotal")
    for product in order["products"]:
        print(
            f"{product['amount']:<8}{product['product']:<16}{product['unit_price']:<9}{product['subtotal']}"
        )
    print(f"Total: {order['total']:.2f}")


def main():
    # List que contiene las boletas creadas
    orders = []

    # Boolean para funcionamiento del programa
    start_program = True

    # Comienzo programa
    while start_program:

        # Opciones para el usuario
        user_input = input(
            "1- Crear Pedido\n2- Borrar Pedido\n3- Editar boleta\n4- Imprimir Boleta\n4- Cerrar Programa\n"
        )
        print("")

        match user_input:
            case "1":
                orders.append(create_order())
            case "2":
                if len(orders) > 0:
                    orders.pop(eliminate_order(orders))
                else:
                    print("No hay pedidos para eliminar")
            case "4":
                if len(orders) > 0:
                    user_print = int(
                        input(
                            f"Selecciona el número de boleta a imprimir: (1-{len(orders)}) "
                        )
                    )
                    if 1 <= user_print <= len(orders):
                        print_order(orders[user_print - 1])
                    else:
                        print("Selección no válida.")
                else:
                    print("No hay boletas para imprimir")
            case "5":
                start_program = False
            case _:
                print("Opción no válida.")


if __name__ == "__main__":
    main()
