import os
import pygame

def leer_personajes(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    personajes = contenido.split("Personaje:")
    personajes = [p.strip() for p in personajes if p.strip()]
    return personajes

def mostrar_personajes(personajes):
    for i, personaje in enumerate(personajes):
        nombre = personaje.split('\n')[0].strip()
        print(f"{i + 1}. {nombre}")

def mostrar_descripcion(personaje):
    print(f"Personaje: {personaje}")

def mostrar_imagen_personaje(nombre_personaje):
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(nombre_personaje)
    
    # Convertir el nombre del personaje a minúsculas y reemplazar espacios por guiones bajos
    nombre_archivo = nombre_personaje.lower().replace(' ', '_') + '.png'
    ruta_imagen = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', nombre_archivo)
    
    if not os.path.exists(ruta_imagen):
        print(f"No se encontró la imagen para {nombre_personaje}")
        return
    
    imagen = pygame.image.load(ruta_imagen)
    imagen = pygame.transform.scale(imagen, (200, 200))  # Escalar la imagen si es necesario
    
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
        
        pantalla.fill((0, 0, 0))
        pantalla.blit(imagen, (300, 200))  # Posicionar la imagen en el centro
        pygame.display.flip()
    
    pygame.quit()

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    archivos = {
        1: os.path.join(base_path, 'data', 'personajes_nivel_1_a_10.txt'),
        2: os.path.join(base_path, 'data', 'personajes_nivel_11_a_20.txt'),
        3: os.path.join(base_path, 'data', 'personajes_nivel_21_a_30.txt')
    }
    
    print("Seleccione un nivel:")
    print("1. Nivel 1 al 10")
    print("2. Nivel 11 al 20")
    print("3. Nivel 21 al 30")
    nivel = int(input("Ingrese el número del nivel: "))
    
    if nivel in archivos:
        archivo = archivos[nivel]
        personajes = leer_personajes(archivo)
        
        print("Personajes disponibles:")
        mostrar_personajes(personajes)
        
        seleccion = int(input("Seleccione un personaje por número: ")) - 1
        if 0 <= seleccion < len(personajes):
            personaje = personajes[seleccion]
            mostrar_descripcion(personaje)
            nombre_personaje = personaje.split('\n')[0].strip()
            mostrar_imagen_personaje(nombre_personaje)
        else:
            print("Selección inválida.")
    else:
        print("Nivel no disponible.")

if __name__ == "__main__":
    main()