pesos = []

for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa (kg): "))
    pesos.append(peso)

print(f"\nO maior peso foi {max(pesos)} kg")
print(f"O menor peso foi {min(pesos)} kg")

