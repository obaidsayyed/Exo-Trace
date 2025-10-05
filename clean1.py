import pandas as pd

data_cleaned=pd.read_csv(r"C:\Users\User\OneDrive\Desktop\Exo-Trace\exoplanets_cleaned.csv")

data_cleaned['Planet_Radius_Earth'] = data_cleaned['Planet_Radius_Earth'].fillna(data_cleaned['Planet_Radius_Earth'].median())
data_cleaned['Planet_Mass_Earth'] = data_cleaned['Planet_Mass_Earth'].fillna(data_cleaned['Planet_Mass_Earth'].median())
data_cleaned['Orbital_Period_Days'] = data_cleaned['Orbital_Period_Days'].fillna(data_cleaned['Orbital_Period_Days'].median())
data_cleaned['Orbital_Distance_AU'] = data_cleaned['Orbital_Distance_AU'].fillna(data_cleaned['Orbital_Distance_AU'].median())
data_cleaned['Orbital_Eccentricity'] = data_cleaned['Orbital_Eccentricity'].fillna(data_cleaned['Orbital_Eccentricity'].median())
data_cleaned['Orbital_Inclination_Deg'] = data_cleaned['Orbital_Inclination_Deg'].fillna(data_cleaned['Orbital_Inclination_Deg'].median())
data_cleaned['Star_Temperature_K'] = data_cleaned['Star_Temperature_K'].fillna(data_cleaned['Star_Temperature_K'].mean())
data_cleaned['Star_Radius_Solar'] = data_cleaned['Star_Radius_Solar'].fillna(data_cleaned['Star_Radius_Solar'].mean())
data_cleaned['Star_Mass_Solar'] = data_cleaned['Star_Mass_Solar'].fillna(data_cleaned['Star_Mass_Solar'].mean())
data_cleaned['System_Kmag'] = data_cleaned['System_Kmag'].fillna(data_cleaned['System_Kmag'].mean())
data_cleaned['Star_Luminosity_Solar'] = data_cleaned['Star_Luminosity_Solar'].fillna(data_cleaned['Star_Luminosity_Solar'].median())
data_cleaned['Insolation_Flux_EarthUnits'] = data_cleaned['Insolation_Flux_EarthUnits'].fillna(data_cleaned['Insolation_Flux_EarthUnits'].median())
data_cleaned['Planet_Equilibrium_Temp_K'] = data_cleaned['Planet_Equilibrium_Temp_K'].fillna(data_cleaned['Planet_Equilibrium_Temp_K'].median())


# Verify that nulls are handled
print(data_cleaned.isnull().sum())

data_cleaned.to_csv("exoplanets_cleaned1.csv", index=False)
print("Dataset successfully downloaded and saved as exoplanets_cleaned1.csv")

