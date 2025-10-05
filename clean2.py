import pandas as pd 

data=pd.read_csv(r"C:\Users\User\OneDrive\Desktop\Exo-Trace\exoplanets_pscomppars_cleaned.csv")

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

# Check the renamed columns
print(data.columns)
# Planet properties
data['Planet_Radius_Earth'] = data['Planet_Radius_Earth'].fillna(data['Planet_Radius_Earth'].median())
data['Planet_Mass_Earth'] = data['Planet_Mass_Earth'].fillna(data['Planet_Mass_Earth'].median())
data['Orbital_Period_Days'] = data['Orbital_Period_Days'].fillna(data['Orbital_Period_Days'].median())
data['Orbital_Distance_AU'] = data['Orbital_Distance_AU'].fillna(data['Orbital_Distance_AU'].median())
data['Orbital_Eccentricity'] = data['Orbital_Eccentricity'].fillna(data['Orbital_Eccentricity'].median())
data['Orbital_Inclination_Deg'] = data['Orbital_Inclination_Deg'].fillna(data['Orbital_Inclination_Deg'].median())

# Host star properties
data['Star_Temperature_K'] = data['Star_Temperature_K'].fillna(data['Star_Temperature_K'].mean())
data['Star_Radius_Solar'] = data['Star_Radius_Solar'].fillna(data['Star_Radius_Solar'].mean())
data['Star_Mass_Solar'] = data['Star_Mass_Solar'].fillna(data['Star_Mass_Solar'].mean())
data['System_Kmag'] = data['System_Kmag'].fillna(data['System_Kmag'].mean())
data['Star_Luminosity_Solar'] = data['Star_Luminosity_Solar'].fillna(data['Star_Luminosity_Solar'].median())

# Planet irradiation & temperature
data['Insolation_Flux_EarthUnits'] = data['Insolation_Flux_EarthUnits'].fillna(data['Insolation_Flux_EarthUnits'].median())
data['Planet_Equilibrium_Temp_K'] = data['Planet_Equilibrium_Temp_K'].fillna(data['Planet_Equilibrium_Temp_K'].median())

# Optional: check that no nulls remain

data.to_csv("exoplanets_pscomppars_cleaned2.csv", index=False)
print("Dataset successfully downloaded and saved as exoplanets_pscomppars_cleaned2.csv")
print(data.isnull().sum())

