import pandas as pd
import os

# This script prepares the Transfermarkt database for further use and creates tables and datasets for 
# data visualization.

START = 2010
END = 2026

# Define subfolder with data in WD
data_dir = "transfermarkt"

# List of the CSV files to import to DF
csv_files = [
    "game_events.csv",
    "game_lineups.csv",
    "games.csv",
    "national_teams.csv",
    "player_valuations.csv",
    "players.csv",
    "transfers.csv",
    "appearances.csv",
    "club_games.csv",
    "clubs.csv",
    "competitions.csv",
    "countries.csv"
]

# Create an empty dictionary to store the DataFrames as values
df_dict = {}

# Loop through the list, read each CSV, and store it in the dictionary
for file in csv_files:
    file_path = os.path.join(data_dir, file)
    
    # Extract the name without the '.csv' extension to use as the dictionary key
    df_name = file.replace(".csv", "")
    
    try:
        df_dict[df_name] = pd.read_csv(file_path)
        
    except FileNotFoundError:
        print(FileNotFoundError)

# Todo