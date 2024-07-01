from datetime import date


# Crear el pedido con Cliente - Dia - Productos -  Total
def create_order():

    order = True
    # Lista de productos
    products = []

    # Datos clientes y dia
    client = input("Cliente: ")
    day = date.today()
    # Loop para agregar productos
    while order:
        print("")

        # Imprimir productos de la lista ya agregar si existen
        if len(products) > 0:
            print("Cant    Producto    Unit    Subtotal")
            for i, product in enumerate(products):
                print(
                    f"{i +1}- {product['amount']}     {product['product']}    {product['unit_price']}     {product['subtotal']}"
                )

        print("")

        user_action = input(
            "1- Agregar Producto\n2-Borrar Producto\n3-Finalizar Pedido\n"
        )

        print("")

        match user_action:
            case "1":
                # Agregar producto
                products.append(create_product())
            case "2":
                # Eliminar producto
                if len(products) > 0:
                    products.pop(eliminate_order())
                else:
                    print("No tiene productos para eliminar")

            case "3":
                # Retornar el pedido completo cuando decide finalizar
                return {
                    "client": client,
                    "day": day.strftime("%d-%m-%Y"),  # Formateo de fecha
                    "products": products,
                    "total": sum([product["subtotal"] for product in products]),
                }

            case _:
                print("Valor no valido.")


# Crear Producto
def create_product():
    amount = input("Cantidad: ")
    product = input("Producto: ")
    unit_price = input("Precio: ")
    subtotal = float(unit_price) * float(amount)

    return {
        "amount": amount,
        "product": product,
        "unit_price": unit_price,
        "subtotal": subtotal,
    }


# Eliminar Producto
def eliminate_order():
    user_select = int(input("Pedido para eliminar: "))
    return user_select - 1


# Imprimir boleta
def print_order(): ...


def main():
    # Start Program
    orders = []
    start_program = True

    while start_program:
        # Si ya hay un pedido hecho se imprime de bajo de las opciones
        if len(orders) > 0:
            for order in orders:
                print(order)
        print("")
        # Opciones: Crear Pedido, Borrar Pedido, Imprimir Boleta, Cerrar programa
        user_input = input(
            "1-Crear Pedido\n2-Borrar Pedido\n3-Imprimir Boleta\n4-Cerrar Programa\n"
        )
        print("")

        match user_input:
            case "1":
                # Funcion crear pedido
                orders.append(create_order())
            case "2":
                # Funcion Borrar pedido
                orders.pop(eliminate_order())
            case "3":
                # Funcion para imprimir la boleta
                ...
            case "4":
                # Cerrar Programa
                start_program = False

            case _:
                # Lanzar error
                ...


main()
