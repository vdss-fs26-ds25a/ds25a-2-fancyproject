import pandas as pd
import io
from tmquery import TMQuery
print("asdl23")
# 1. Chain the methods to search for the competition and fetch its clubs
# Note: Transfermarkt often formats seasons as "YYYY-YY" or just the starting year "YYYY"
query = TMQuery().search_competition("premier league").get_clubs(season="2010")
print("asdl23")
# 2. Extract the data as a CSV string
csv_data = query.csv()
print("asdl23")
# 3. Read the CSV string directly into a Pandas DataFrame
df = pd.read_csv(io.StringIO(csv_data))

# Display the first few rows to verify
print("asdl23")