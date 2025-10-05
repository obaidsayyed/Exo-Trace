import pandas as pd
data=pd.read_csv(r"C:\Users\User\OneDrive\Desktop\Exo-Trace\hipparcos_stellar_catalog.csv")

# Drop 'RAhms'
if 'RAhms' in data.columns:
    data.drop(columns='RAhms', inplace=True)
    print("Dropped column: RAhms")

# Drop 'DEdms'
if 'DEdms' in data.columns:
    data.drop(columns='DEdms', inplace=True)
    print("Dropped column: DEdms")

# Drop 'e_Plx'
if 'e_Plx' in data.columns:
    data.drop(columns='e_Plx', inplace=True)
    print("Dropped column: e_Plx")

# Drop 'Notes'
if 'Notes' in data.columns:
    data.drop(columns='Notes', inplace=True)
    print("Dropped column: Notes")

# Drop '_RA.icrs'
if '_RA.icrs' in data.columns:
    data.drop(columns='_RA.icrs', inplace=True)
    print("Dropped column: _RA.icrs")

# Drop '_DE.icrs'
if '_DE.icrs' in data.columns:
    data.drop(columns='_DE.icrs', inplace=True)
    print("Dropped column: _DE.icrs")

# Check remaining columns
print("Remaining columns:")
print(data.columns)

# Drop rows where RA, Dec, or Parallax is missing
data.dropna(subset=['RAICRS', 'DEICRS', 'Parallax_mas'], inplace=True)

# Fill missing proper motion with 0
data['PMRA_mas_per_yr'].fillna(0, inplace=True)
data['PMDec_mas_per_yr'].fillna(0, inplace=True)

# Fill missing B-V with median value
bv_median = data['B-V'].median()
data['B-V'].fillna(bv_median, inplace=True)

# Check again
print(data.isnull().sum())

data.to_csv("hipparcos_stellar_catalog5.csv", index=False)
print("Dataset successfully downloaded and saved as hipparcos_stellar_catalog5.csv")
