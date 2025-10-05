import pandas as pd
data=pd.read_csv(r"C:\Users\User\OneDrive\Desktop\Exo-Trace\gaia_exoplanets_cleaned.csv")

# Example: dropping unwanted columns one by one
data = data.drop('Planet_Letter', axis=1)
data = data.drop('Orbital_Inclination_Deg', axis=1)
data = data.drop('System_Kmag', axis=1)
data = data.drop('Star_Luminosity_Solar', axis=1)
data = data.drop('Insolation_Flux_EarthUnits', axis=1)
data = data.drop('Planet_Equilibrium_Temp_K', axis=1)

print(data.columns)

# Imputation for numerical columns
data['Planet_Radius_Earth'] = data['Planet_Radius_Earth'].median()
data['Planet_Mass_Earth'] = data['Planet_Mass_Earth'].median()
data['Orbital_Period_Days'] = data['Orbital_Period_Days'].median()
data['Orbital_Distance_AU'] = data['Orbital_Distance_AU'].median()
data['Orbital_Eccentricity'] = data['Orbital_Eccentricity'].median()
data['Star_Temperature_K'] = data['Star_Temperature_K'].mean()
data['Star_Radius_Solar'] = data['Star_Radius_Solar'].mean()
data['Star_Mass_Solar'] = data['Star_Mass_Solar'].mean()

# Verify null values are handled
print(data.isnull().sum())

data.to_csv("gaia_exoplanets_cleaned4.csv", index=False)
print("Dataset successfully downloaded and saved as gaia_exoplanets_cleaned4.csv")
