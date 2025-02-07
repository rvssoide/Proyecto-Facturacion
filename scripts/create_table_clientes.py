import pandas as pd
from google.colab import drive, files

# Load the uploaded CSV file to examine its structure
drive.mount('/content/drive')

data = pd.read_csv("/content/drive/", delimiter=',')

# Display the first few rows of the dataset to understand its structure
data.head(10)

unique_clients_count = data['CUIT/CUIL'].nunique()
print(f"Cantidad de clientes únicos en la tabla original: {unique_clients_count}")

import random

# Define fictitious data for additional columns
continents = ['América', 'Europa', 'Asia']
countries = {
    'América': ['Argentina', 'Brasil', 'Estados Unidos'],
    'Europa': ['España'],
    'Asia': ['China']


}
states_cities = {
    'Argentina': {'Buenos Aires': ['Buenos Aires'], 'Córdoba': ['Córdoba'], 'Santa Fe': ['Rosario']},
    'Brasil': {'São Paulo': ['São Paulo'], 'Rio de Janeiro': ['Rio de Janeiro']},
    'Estados Unidos': {'California': ['Los Ángeles', 'San Francisco'], 'Texas': ['Houston', 'Dallas']},
    'España': {'Madrid': ['Madrid'], 'Cataluña': ['Barcelona']},
    'China': {'Pekín': ['Pekín'], 'Shanghái': ['Shanghái']}
}

# Determine 'Tipo de Cliente' based on 'Condicion'
def determine_tipo_cliente(condicion):
    if condicion in ['Responsable Inscripto', 'Régimen Simplificado']:
        return 'Persona Física'
    elif condicion in ['IVA Sujeto Exento']:
        return 'Persona Jurídica'
    return 'Desconocido'

# Filter unique clients from the original data
clientes_unicos = data[['Razon_Social', 'CUIT/CUIL', 'Condicion']].drop_duplicates().head(6001)

# Generate the new table
dim_tabla_clientes = clientes_unicos.copy()
dim_tabla_clientes['Domicilio'] = [f'Calle {random.randint(1, 999)} N°{random.randint(1, 5000)}' for _ in range(len(dim_tabla_clientes))]
dim_tabla_clientes['Región'] = [random.choice(continents) for _ in range(len(dim_tabla_clientes))]
dim_tabla_clientes['País'] = dim_tabla_clientes['Región'].apply(lambda x: random.choice(countries[x]))
dim_tabla_clientes['Estado/Provincia'] = dim_tabla_clientes['País'].apply(lambda x: random.choice(list(states_cities.get(x, {}).keys())))
dim_tabla_clientes['Ciudad'] = dim_tabla_clientes.apply(
    lambda row: random.choice(states_cities.get(row['País'], {}).get(row['Estado/Provincia'], ['Ciudad Desconocida'])),
    axis=1
)
dim_tabla_clientes['Tipo de Cliente'] = data['Condicion'].apply(determine_tipo_cliente)

# Display the first few rows of the new table
dim_tabla_clientes.head()

# Export the generated table to a CSV file
output_path = '/content/drive/'
dim_tabla_clientes.to_csv(output_path, index=False)

output_path