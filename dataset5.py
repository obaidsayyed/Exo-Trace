from astroquery.vizier import Vizier
import pandas as pd
from time import sleep

# Set row limit
Vizier.ROW_LIMIT = 50000  # Adjust if you want more rows

# Retry logic for unstable connections
for attempt in range(5):
    try:
        print(f"Attempt {attempt + 1} to fetch Hipparcos data...")
        # Query Hipparcos Main Catalog (I/239/hip_main)
        result = Vizier.query_constraints(catalog="I/239/hip_main", Vmag="<10")
        break
    except Exception as e:
        print(f"Error: {e}")
        sleep(5)
else:
    raise Exception("Failed to download dataset after 5 attempts")

# Convert to pandas DataFrame
data = result[0].to_pandas()

# Rename columns for clarity (you can adjust more if needed)
data = data.rename(columns={
    'HIP': 'Hipparcos_ID',
    'RA_ICRS': 'RA_Degrees',
    'DE_ICRS': 'Dec_Degrees',
    'Vmag': 'V_Magnitude',
    'Plx': 'Parallax_mas',
    'pmRA': 'PMRA_mas_per_yr',
    'pmDE': 'PMDec_mas_per_yr',
    'SpType': 'Spectral_Type'
})

# Save cleaned data to CSV
data.to_csv("hipparcos_stellar_catalog.csv", index=False)
print("Dataset successfully downloaded and saved as hipparcos_stellar_catalog.csv")
print(data.head())
