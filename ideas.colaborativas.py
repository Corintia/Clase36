# Clase 36: Nuestras Ideas para Proyectos Colaborativos de IA
# ¡Cada miembro del equipo añadirá su nombre y una idea en la lista de abajo!

# Las ideas se guardarán como diccionarios, cada uno con un nombre y una idea.
# Ejemplo: {"nombre": "Profesor/a", "idea": "Un asistente de IA para organizar libros en la biblioteca"}

ideas_de_proyectos_ia = [
    # --- ¡Añade tu propia contribución debajo de esta línea! ---
    # No borres lo que otros compañeros hayan añadido.
    # Asegúrate de que cada idea sea un diccionario y esté separada por una coma si no es la última.
    # Por ejemplo:
    # {"nombre": "Juanita", "idea": "Una IA que prediga el clima para organizar excursiones"},
    # {"nombre": "Pedrito", "idea": "Un robot de IA que clasifique la basura en la escuela"},

    # ¡Tu contribución va aquí!
]

# Este código adicional sirve para mostrar todas las ideas al final.
print("--- Ideas de Proyectos de IA Colaborativos ---")
if not ideas_de_proyectos_ia:
    print("Aún no hay ideas. ¡Sé el primero en añadir la tuya!")
else:
    for idea in ideas_de_proyectos_ia:
        print(f"- **{idea['nombre']}**: {idea['idea']}")

print("\n¡Gracias por colaborar en este proyecto!")
