import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import os

combined_metadata_LMI = pd.DataFrame()
combined_metadata_vel = pd.DataFrame()

# Set your directory
os.chdir(r'C:\Users\lucas\OneDrive - Johns Hopkins\Ramesh Lab - Research\Code\HELIX-Shot-Query')
folder_name = r'C:\Users\lucas\Downloads\Updated velocity shots'

# For all Excel files in directory
for filename in os.listdir(folder_name):
    filepath = os.path.join(folder_name,filename)
    if filepath.endswith('.xlsx') and "LMI" in filepath:
        exp_run_metadata = pd.read_excel(filepath)
        # Concatenate, ignore index so you just stack rows
        combined_metadata_LMI = pd.concat([combined_metadata_LMI, exp_run_metadata], ignore_index=True, sort=True)
    if filepath.endswith('.xlsx') and "velocity" in filepath:
        exp_run_metadata = pd.read_excel(filepath)
        # Concatenate, ignore index so you just stack rows
        combined_metadata_vel = pd.concat([combined_metadata_vel, exp_run_metadata], ignore_index=True, sort=True)


combined_metadata_vel[['Beam_Profile_FileName', 'PDV_FileName']] = combined_metadata_vel[['Beam_Profile_FileName', 'PDV_FileName']].replace(0, '')

# Save combined dataframe
combined_metadata_LMI.to_excel('combined_metadata_LMI.xlsx', index=False)
combined_metadata_vel.to_excel('combined_metadata_vel.xlsx', index=False)
# display(combined_metadata_LMI)

df = pd.DataFrame(combined_metadata_vel)

# Clean the string columns (optional: ensures no non-string types)
for col in ['Beam_Profile_FileName', 'PDV_FileName']:
    df[col] = df[col].replace(0, '').astype(str)

# Streamlit UI
st.title("Metadata Viewer")

st.write("This is your metadata table:")
st.dataframe(df)  # <-- This displays the interactive dataframe in the browser

# Simple plot for demo
st.write("Histogram of Energy")
st.bar_chart(df['Energy'])