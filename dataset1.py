import pandas as pd
import requests
from io import StringIO
from time import sleep

url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
query = "SELECT pl_name, pl_letter, pl_rade, pl_bmasse, pl_orbper, pl_orbsmax, pl_orbeccen, pl_orbincl, hostname, st_teff, st_rad, st_mass, sy_kmag, st_lum, pl_insol, pl_eqt FROM ps"
params = {"query": query, "format": "csv"}

# Retry logic for unstable connections
for attempt in range(5):
    try:
        print(f"Attempt {attempt + 1} to fetch data...")
        response = requests.get(url, params=params, timeout=120)
        response.raise_for_status()
        break
    except Exception as e:
        print(f"Error: {e}")
        sleep(5)
else:
    raise Exception("Failed to download dataset after 5 attempts")

# Load CSV into pandas DataFrame
data = pd.read_csv(StringIO(response.text), low_memory=False)

# Rename columns
data = data.rename(columns={
    'pl_name': 'Planet_Name',
    'pl_letter': 'Planet_Letter',
    'pl_rade': 'Planet_Radius_Earth',
    'pl_bmasse': 'Planet_Mass_Earth',
    'pl_orbper': 'Orbital_Period_Days',
    'pl_orbsmax': 'Orbital_Distance_AU',
    'pl_orbeccen': 'Orbital_Eccentricity',
    'pl_orbincl': 'Orbital_Inclination_Deg',
    'hostname': 'Host_Star_Name',
    'st_teff': 'Star_Temperature_K',
    'st_rad': 'Star_Radius_Solar',
    'st_mass': 'Star_Mass_Solar',
    'sy_kmag': 'System_Kmag',
    'st_lum': 'Star_Luminosity_Solar',
    'pl_insol': 'Insolation_Flux_EarthUnits',
    'pl_eqt': 'Planet_Equilibrium_Temp_K'
})

# Save cleaned data
data.to_csv("exoplanets_cleaned.csv", index=False)
print("Dataset successfully downloaded and saved as exoplanets_cleaned.csv")
print(data.head())
