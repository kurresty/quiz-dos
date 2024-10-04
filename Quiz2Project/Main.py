nombre = input("Ingrese el nombre: ")
dias_laborados = int(input("Ingrese los dias laborados: "))
salario = float(input("Ingrese el salario: "))



prima = salario * dias_laborados/360
cesantías = salario * dias_laborados/360
intereses_cesantías = cesantías * 0.12/dias_laborados
vacaciones = salario * dias_laborados / 720
liquidacion = salario * dias_laborados/360

print(f"Señor {nombre} para los {dias_laborados}  dias laborados "
      f"y salario ${salario:,.2f}, su liquidacion se compone asi: ")
print(f"prima: {prima}")
print(f"cesantias: {cesantías}")
print(f"intereses_censantias: {intereses_cesantías}")
print(f"vacaciones: {vacaciones}")
print(f"liquidacion: {liquidacion}")

