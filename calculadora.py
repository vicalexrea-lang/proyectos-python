# Calculadora de vuelo de dron
distancia = 15.5        # km
precio_por_km = 8.0     # USD
bateria = 100           # porcentaje inicial
consumo_por_km = 4.5    # % de batería por km

costo_total = distancia * precio_por_km
bateria_final = bateria - (distancia * consumo_por_km)

print(f"Distancia del vuelo: {distancia} km")
print(f"Costo total: ${costo_total}")
print(f"Batería restante: {bateria_final}%")
print(f"¿Vuelo completable? {bateria_final > 0}")
