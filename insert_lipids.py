import sqlite3
import pandas as pd

# Connect to the initialized database where data will be entered
cxn = sqlite3.connect("ox_pdt.db") 
df = pd.read_csv("PLPC_TEST.csv")  # Insert path to CSV file containing data
df.to_sql(name="ox_pdt_1", con=cxn, if_exists="append", index=False)

cxn.commit()
cxn.close()