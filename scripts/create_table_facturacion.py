import pandas as pd
import random
from datetime import datetime, timedelta

# Cargar el archivo proporcionado
file_path = '/mnt/data/Tabla_Facturas - Hoja 1.csv'
columns = pd.read_csv(file_path).columns

# Configurar los valores posibles para algunos campos
tipo_comprobante = ["Factura A", "Factura B", "Factura C", "Factura Electrónica A"]
estado = ["Pagado", "Pendiente de pago", "Vencido"]
condicion = ["Régimen Simplificado", "Responsable Inscripto", "IVA Sujeto Exento"]

# Generar fechas aleatorias
def random_date(start, end):
    """Genera una fecha aleatoria entre start y end."""
    return start + timedelta(days=random.randint(0, (end - start).days))

# Configurar rangos de fechas
start_date = datetime(2014, 1, 1)
end_date = datetime.now()

# Generar datos con los campos ajustados
records = []
for _ in range(6000):
    # Generar fechas relacionadas
    fecha_emision = random_date(start_date, end_date)
    fecha_vencimiento = fecha_emision + timedelta(days=random.randint(1, 60))
    fecha_pago = fecha_emision + timedelta(days=random.randint(0, 60))
    
    # Generar razón social aleatoria (puede ser física o jurídica)
    razon_social = (
        f"Persona {random.randint(1, 3000)}"
        if random.random() < 0.5
        else f"Empresa {random.randint(1, 3000)} {random.choice(['S.A.', 'SRL', 'SAS'])}"
    )
    
    # Generar registro
    records.append({
        "Punto_De_Venta": f"{random.randint(10000, 99999)}",
        "Tipo_De_Comprobante": random.choice(tipo_comprobante),
        "Numero_De_Comprobante": f"{random.randint(10000000, 99999999)}",
        "ID_Factura": "",
        "Fecha_Emision": fecha_emision.strftime("%d/%m/%Y"),
        "Fecha_Vencimiento": fecha_vencimiento.strftime("%d/%m/%Y"),
        "Fecha_Pago": fecha_pago.strftime("%d/%m/%Y") if fecha_pago > fecha_emision else "",
        "Estado": random.choice(estado),
        "CUIT/CUIL": f"{random.randint(10, 99)}-{random.randint(10000000, 99999999)}-{random.randint(0, 9)}",
        "Razon_Social": razon_social,
        "Condicion": random.choice(condicion),
        "SubTotal": round(random.uniform(1000, 50000), 2),
        "IVA": "",
        "Total": ""
    })

# Crear un DataFrame con los datos generados
df = pd.DataFrame(records, columns=[
    "Punto_De_Venta", "Tipo_De_Comprobante", "Numero_De_Comprobante", "ID_Factura",
    "Fecha_Emision", "Fecha_Vencimiento", "Fecha_Pago", "Estado", "CUIT/CUIL",
    "Razon_Social", "Condicion", "SubTotal", "IVA", "Total"
])

# Guardar en un archivo para entregar al usuario
output_file_path = '/mnt/data/Tabla_Facturas_Generada.csv'
df.to_csv(output_file_path, index=False)
output_file_path



# Definir una lista de clientes únicos (Punto_De_Venta, CUIT/CUIL, Razon_Social, Condicion)
num_clientes_unicos = 500  # Número aproximado de clientes únicos
clientes = [
    {
        "Punto_De_Venta": f"{random.randint(10000, 99999)}",
        "CUIT/CUIL": f"{random.randint(10, 99)}-{random.randint(10000000, 99999999)}-{random.randint(0, 9)}",
        "Razon_Social": (
            f"Persona {random.randint(1, 3000)}"
            if random.random() < 0.5
            else f"Empresa {random.randint(1, 3000)} {random.choice(['S.A.', 'SRL', 'SAS'])}"
        ),
        "Condicion": random.choice(condicion),
    }
    for _ in range(num_clientes_unicos)
]

# Generar registros asociados a los clientes
records = []
for _ in range(6000):
    # Seleccionar un cliente al azar
    cliente = random.choice(clientes)
    
    # Generar fechas relacionadas
    fecha_emision = random_date(start_date, end_date)
    fecha_vencimiento = fecha_emision + timedelta(days=random.randint(1, 60))
    fecha_pago = fecha_emision + timedelta(days=random.randint(0, 60))
    
    # Generar registro
    records.append({
        "Punto_De_Venta": cliente["Punto_De_Venta"],
        "Tipo_De_Comprobante": random.choice(tipo_comprobante),
        "Numero_De_Comprobante": f"{random.randint(10000000, 99999999)}",
        "ID_Factura": "",
        "Fecha_Emision": fecha_emision.strftime("%d/%m/%Y"),
        "Fecha_Vencimiento": fecha_vencimiento.strftime("%d/%m/%Y"),
        "Fecha_Pago": fecha_pago.strftime("%d/%m/%Y") if fecha_pago > fecha_emision else "",
        "Estado": random.choice(estado),
        "CUIT/CUIL": cliente["CUIT/CUIL"],
        "Razon_Social": cliente["Razon_Social"],
        "Condicion": cliente["Condicion"],
        "SubTotal": round(random.uniform(1000, 50000), 2),
        "IVA": "",
        "Total": ""
    })

# Crear un DataFrame con los datos generados
df = pd.DataFrame(records, columns=[
    "Punto_De_Venta", "Tipo_De_Comprobante", "Numero_De_Comprobante", "ID_Factura",
    "Fecha_Emision", "Fecha_Vencimiento", "Fecha_Pago", "Estado", "CUIT/CUIL",
    "Razon_Social", "Condicion", "SubTotal", "IVA", "Total"
])

# Guardar en un archivo para entregar al usuario
output_file_path = '/mnt/data/Tabla_Facturas_Clientes_Repetidos.csv'
df.to_csv(output_file_path, index=False)
output_file_path
