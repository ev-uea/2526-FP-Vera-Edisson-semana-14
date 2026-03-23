def calcular_promedio(nota1, nota2, nota3):
    """
    Función que recibe tres notas, calcula el promedio
    y retorna el resultado.
    """
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    return promedio

print("--- Sistema de Calificaciones ---")

n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))

resultado_final = calcular_promedio(n1, n2, n3)

print(f"\nEl promedio final del estudiante es: {resultado_final:.2f}")