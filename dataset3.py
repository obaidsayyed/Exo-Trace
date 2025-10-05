import pandas as pd
import requests
from io import StringIO
from time import sleep

url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
query = """
SELECT
    toi, toipfx, tid, ctoi_alias, pl_pnum, tfopwg_disp,
    rastr, ra, decstr, dec, st_pmra, st_pmdec,
    pl_tranmid, pl_orbper, pl_trandurh, pl_trandep
FROM toi
"""
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
    'toi': 'TOI_ID',
    'toipfx': 'TOI_Star_ID',
    'tid': 'TIC_ID',
    'ctoi_alias': 'Community_TOI_Alias',
    'pl_pnum': 'Planet_Candidate_Count',
    'tfopwg_disp': 'TFOPWG_Disposition',
    'rastr': 'RA_Sexagesimal',
    'ra': 'RA_Degrees',
    'decstr': 'Dec_Sexagesimal',
    'dec': 'Dec_Degrees',
    'st_pmra': 'PMRA_mas_per_yr',
    'st_pmdec': 'PMDec_mas_per_yr',
    'pl_tranmid': 'Transit_Midpoint_BJD',
    'pl_orbper': 'Orbital_Period_Days',
    'pl_trandurh': 'Transit_Duration_Hours',
    'pl_trandep': 'Transit_Depth_ppm'
})

# Save cleaned data
data.to_csv("tess_exoplanets_cleaned.csv", index=False)
print("Dataset successfully downloaded and saved as tess_exoplanets_cleaned.csv")
print(data.head())
