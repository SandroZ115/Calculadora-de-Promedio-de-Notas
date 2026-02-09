def calcular_promedio():
    print("--- Calculadora de Promedio Universitario ---")
    
    nombre = input("Ingresa tu nombre: ")
    curso = input("Ingresa el nombre del curso: ")
    
    # Pedimos las notas
    try:
        nota1 = float(input("Ingresa la nota del primer parcial: "))
        nota2 = float(input("Ingresa la nota del segundo parcial: "))
        nota3 = float(input("Ingresa la nota del examen final: "))
        
        # Calculamos el promedio
        promedio = (nota1 + nota2 + nota3) / 3
        
        print(f"\nEstudiante: {nombre}")
        print(f"Curso: {curso}")
        print(f"Tu promedio final es: {round(promedio, 2)}")
        
        if promedio >= 61:
            print("Estado: APROBADO ✅ :D")
        else:
            print("Estado: REPROBADO ❌ D:")
            
    except ValueError:
        print("Error: Por favor ingresa solo números.")

# Ejecutamos la función
if __name__ == "__main__":
    calcular_promedio()
