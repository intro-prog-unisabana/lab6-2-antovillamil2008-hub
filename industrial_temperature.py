def trigger_alarm(temperatures, threshold=80):
    sensores_en_alerta = []
    for nombre_sensor, lectura_actual in temperatures.items():
        # Verificamos si la lectura supera estrictamente el límite
        if lectura_actual > threshold:
            sensores_en_alerta.append(nombre_sensor)
    return sensores_en_alerta
