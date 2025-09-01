
def calcular_impuesto (costo_comida) :
   #Calculamos impuesto 
    if costo_comida > 50 :
        impuesto = costo_comida * 0.15
    else:
        impuesto = costo_comida * 0.10
    return impuesto

def calcular_propina (costo_comida) :
    #Calcular la propina con respecto al tota de la comida
    if costo_comida > 50 :
        propina = costo_comida * 0.20
    else:
        propina = costo_comida * 0.15
    return propina

try:
    # Se le pregunta al usuario costo de comida 
    print ("Hola, bienvenido")
    costo_comida = float (input("Ingresa el costo de la comida: "))

# Operaciones necesarias
    monto_impuesto = calcular_impuesto (costo_comida)
    monto_propina = calcular_propina (costo_comida)
    total = costo_comida + monto_impuesto + monto_propina

    # Desglose
    print ("Su cuenta es de: ")
    print(f"Costo original: $ {costo_comida}")
    print(f"Impuesto aplicado: $ {monto_impuesto}")
    print(f"Propina sugerida: $ {monto_propina}")
    print(f"Costo total a pagar: $ {total}")

except ValueError:
    print("Por favor, ingresa un número válido para el costo de la comida.")
