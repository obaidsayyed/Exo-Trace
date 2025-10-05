import pandas as pd

data=pd.read_csv(r"C:\Users\User\OneDrive\Desktop\Exo-Trace\tess_exoplanets_cleaned.csv")
# Drop columns individually using assignment to avoid inplace warnings
data = data.drop('TOI_Star_ID', axis=1)
data = data.drop('Community_TOI_Alias', axis=1)
data = data.drop('Planet_Candidate_Count', axis=1)
data = data.drop('RA_Sexagesimal', axis=1)
data = data.drop('RA_Degrees', axis=1)
data = data.drop('Dec_Sexagesimal', axis=1)
data = data.drop('Dec_Degrees', axis=1)
data = data.drop('PMRA_mas_per_yr', axis=1)
data = data.drop('PMDec_mas_per_yr', axis=1)
data = data.drop('Transit_Midpoint_BJD', axis=1)

print(data.columns)

# Impute the null values in 'Orbital_Period_Days' using median
data['Orbital_Period_Days'] = data['Orbital_Period_Days'].fillna(data['Orbital_Period_Days'].median())

data.to_csv("tess_exoplanets_cleaned3.csv", index=False)
print("Dataset successfully downloaded and saved as tess_exoplanets_cleaned3.csv")
print(data.isnull().sum())
