from datetime import datetime


def generate_id_registro(id_registro, fecha_generacion_registro):
    fecha_obj = convert_to_date(fecha_generacion_registro)
    fecha_str = fecha_obj.strftime('%d%m%y:%H%M')
    return f"MODP-{id_registro}-{fecha_str}"


def convert_to_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return datetime.strptime(date_str, "%Y-%m-%d")
