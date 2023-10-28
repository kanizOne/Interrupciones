import random
import time

def operacion(tipo, duracion, n):
    if tipo == "resta":
        start_time = time.time()
        while time.time() - start_time < duracion:
            for _ in range(n):
                valor1 = random.randint(1, 100)
                valor2 = random.randint(1, 100)
                resultado = valor1 - valor2
                # Realizar operaciones de resta aquí
                print(f"{valor1} - {valor2} = {resultado}")
    elif tipo == "suma":
        start_time = time.time()
        while time.time() - start_time < duracion:
            for _ in range(n):
                valor1 = random.randint(1, 100)
                valor2 = random.randint(1, 100)
                resultado = valor1 + valor2
                # Realizar operaciones de suma aquí
                print(f"{valor1} + {valor2} = {resultado}")
    elif tipo == "division":
        start_time = time.time()
        while time.time() - start_time < duracion:
            for _ in range(n):
                valor1 = random.randint(1, 100)
                valor2 = random.randint(1, 100)
                if valor2 != 0:
                    resultado = valor1 / valor2
                    # Realizar operaciones de división aquí
                    print(f"{valor1} / {valor2} = {resultado}")
    elif tipo == "multiplicacion":
        start_time = time.time()
        while time.time() - start_time < duracion:
            for _ in range(n):
                valor1 = random.randint(1, 100)
                valor2 = random.randint(1, 100)
                resultado = valor1 * valor2
                # Realizar operaciones de multiplicación aquí
                print(f"{valor1} * {valor2} = {resultado}")

def main():
    n = 5  # Cantidad de operaciones por bloque
    tipos = ["resta", "suma", "division", "multiplicacion"]

    for tipo in tipos:
        duracion = random.randint(6, 9)
        print(f"Realizando {n} operaciones de {tipo} durante {duracion} segundos...")
        operacion(tipo, duracion, n)
        print(f"Operaciones de {tipo} finalizadas\n")

    # Ejecutar los bloques en orden inverso
    for tipo in reversed(tipos):
        duracion = random.randint(6, 9)
        print(f"Realizando {n} operaciones de {tipo} durante {duracion} segundos...")
        operacion(tipo, duracion, n)
        print(f"Operaciones de {tipo} finalizadas\n")

if __name__ == "__main__":
    main()
