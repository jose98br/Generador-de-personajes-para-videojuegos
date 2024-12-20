# Proyecto Personajes

Este proyecto está diseñado para generar personajes de diferentes niveles en un entorno de juego. Los personajes se clasifican en tres categorías según su nivel: 1 a 10, 11 a 20 y 21 a 30. Cada categoría tiene su propio archivo de texto que contiene información detallada sobre los personajes, incluyendo su apariencia, resistencia, debilidades y una historia.

## Estructura del Proyecto

```
proyecto-personajes
├── src
│   ├── main.py                  # Punto de entrada de la aplicación.
│   ├── generador.py             # Funciones para generar personajes.
│   └── data
│       ├── personajes_nivel_1_a_10.txt  # Información sobre personajes de nivel 1 a 10.
│       ├── personajes_nivel_11_a_20.txt # Información sobre personajes de nivel 11 a 20.
│       └── personajes_nivel_21_a_30.txt # Información sobre personajes de nivel 21 a 30.
├── requirements.txt             # Dependencias necesarias para el proyecto.
└── README.md                    # Documentación del proyecto.
```

## Instrucciones de Uso

1. **Instalación de Dependencias**: Asegúrate de tener Python instalado. Luego, instala las dependencias necesarias ejecutando:
   ```
   pip install -r requirements.txt
   ```

2. **Ejecutar la Aplicación**: Para iniciar la aplicación, ejecuta el siguiente comando en la terminal:
   ```
   python src/main.py
   ```

3. **Seleccionar Personaje**: La aplicación te pedirá que selecciones el tipo de personaje que deseas crear. Puedes elegir entre:
   - Nivel 1 a 10
   - Nivel 11 a 20
   - Nivel 21 a 30

4. **Generación de Personaje**: Una vez que hayas hecho tu selección, la aplicación generará un personaje basado en la información contenida en los archivos de texto correspondientes.

## Ejemplos de Uso

- Al seleccionar un personaje de nivel 1 a 10, podrás ver personajes con características básicas y una historia introductoria.
- Los personajes de nivel 11 a 20 tendrán habilidades más complejas y desafíos adicionales.
- Los personajes de nivel 21 a 30 presentarán una resistencia y habilidades avanzadas, así como historias más elaboradas.

Este proyecto es ideal para desarrolladores que deseen crear un sistema de generación de personajes para juegos o aplicaciones interactivas.