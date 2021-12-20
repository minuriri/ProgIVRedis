import redis

redis = redis.Redis(
    host= 'localhost',
    port= '6379',
    db=1)


def principal():


    menu = """
a) Agregar nueva palabra
b) Editar palabra existente
c) Eliminar palabra existente
d) Ver listado de palabras
e) Buscar significado de palabra
f) Salir
Elige: """
    eleccion = ""
    while eleccion != "f":
        eleccion = input(menu)
        if eleccion == "a":
            palabra = input("Ingresa la palabra: ")
            # Comprobar si no existe
            posible_significado = buscar_significado_palabra(palabra)
            if posible_significado:
                print(f"La palabra '{palabra}' ya existe")
            else:
                significado = input("Ingresa el significado: ")
                agregar_palabra(palabra, significado)
                print("Palabra agregada")
        if eleccion == "b":
            palabra = input("Ingresa la palabra que quieres editar: ")
            nuevo_significado = input("Ingresa el nuevo significado: ")
            editar_palabra(palabra, nuevo_significado)
            print("Palabra actualizada")
        if eleccion == "c":
            palabra = input("Ingresa la palabra a eliminar: ")
            eliminar_palabra(palabra)
        if eleccion == "d":
            print("=== Lista de palabras ===")
            palabras = obtener_palabras()

        if eleccion == "e":
            palabra = input(
                "Ingresa la palabra de la cual quieres saber el significado: ")
            significado = buscar_significado_palabra(palabra)




def agregar_palabra(palabra, significado):
    redis.set(palabra, significado)


def editar_palabra(palabra, nuevo_significado):
    redis.delete(palabra)
    redis.set(palabra, nuevo_significado)


def eliminar_palabra(palabra):
    redis.delete(palabra)


def obtener_palabras():
    palabras=redis.hgetall(redis)
    print(palabras)

def buscar_significado_palabra(palabra):
    palabras=redis.get(palabra)
    print(palabras)

if __name__ == '__main__':
    principal()
