def cargar_personajes(ruta):
    personajes = []
    with open(ruta, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            datos = linea.strip().split('|')
            if len(datos) == 4:
                nombre, apariencia, resistencia, debilidades = datos
                personajes.append({
                    'nombre': nombre,
                    'apariencia': apariencia,
                    'resistencia': int(resistencia),
                    'debilidades': debilidades.split(',')
                })
    return personajes

def generar_personaje(nivel):
    if nivel <= 10:
        ruta = 'src/data/personajes_nivel_1_a_10.txt'
    elif nivel <= 20:
        ruta = 'src/data/personajes_nivel_11_a_20.txt'
    else:
        ruta = 'src/data/personajes_nivel_21_a_30.txt'

    personajes = cargar_personajes(ruta)
    return personajes

def mostrar_personajes(personajes):
    for personaje in personajes:
        print(f"Nombre: {personaje['nombre']}")
        print(f"Apariencia: {personaje['apariencia']}")
        print(f"Resistencia: {personaje['resistencia']}")
        print(f"Debilidades: {', '.join(personaje['debilidades'])}")
        print("-" * 20)

def seleccionar_personaje():
    nivel = int(input("Seleccione el nivel del personaje (1-10, 11-20, 21-30): "))
    personajes = generar_personaje(nivel)
    mostrar_personajes(personajes)