#El PC Builder (Configurador de Hardware)
cpus = [
    {"modelo": "Ryzen 5 5600X", "socket": "AM4", "consumo": 65, "precio": 200},
    {"modelo": "Core i9-12900K", "socket": "LGA1700", "consumo": 240, "precio": 600}
]
motherboards = [
    {"modelo": "B550 Aorus", "socket": "AM4", "precio": 150},
    {"modelo": "Z690 Prime", "socket": "LGA1700", "precio": 220}
]
psus = [
    {"modelo": "Corsair 650W", "watts": 650, "precio": 80},
    {"modelo": "Evga 500W", "watts": 500, "precio": 50}
]

def seleccionar_componente(componentes, tipo):
    print(f"\nSeleccione una {tipo}:")
    for i, comp in enumerate(componentes):
        print(f"{i + 1}. {comp['modelo']} - Precio: ${comp['precio']}")
    eleccion = int(input(f"Ingrese el número de la {tipo} deseada: ")) - 1
    return componentes[eleccion]

def validacion_compatibilidad(cpu, motherboard):
    return cpu["socket"] == motherboard["socket"]

def calculo_energia(cpu, psu):
    return psu["watts"] >= cpu["consumo"] * 1.5  # Recomendación de 1.5x consumo

def calculo_precio_total(cpu, motherboard, psu):
    return cpu["precio"] + motherboard["precio"] + psu["precio"]

def main():
    print("--- Configurador de PC ---")
    cpu_seleccionada = seleccionar_componente(cpus, "CPU")
    motherboard_seleccionada = seleccionar_componente(motherboards, "Motherboard")

    if not validacion_compatibilidad(cpu_seleccionada, motherboard_seleccionada):
        print("Error: La CPU y la Motherboard no son compatibles.")
        return

    psu_seleccionada = seleccionar_componente(psus, "PSU")

    if not calculo_energia(cpu_seleccionada, psu_seleccionada):
        print("Error: La PSU seleccionada no proporciona suficiente energía para la CPU.")
        return

    precio_total = calculo_precio_total(cpu_seleccionada, motherboard_seleccionada, psu_seleccionada)
    print(f"\nConfiguración válida. Precio total: ${precio_total}")

if __name__ == "__main__":
    main()