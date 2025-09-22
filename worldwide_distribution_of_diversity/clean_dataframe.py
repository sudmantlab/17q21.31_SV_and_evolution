import pandas as pd
import numpy as np

df = pd.read_csv("/global/home/users/sridharan/sridharan/scripts/process_d4/1000G/outputs/1000G_readdepth.txt", delimiter = "\t")

df['sample'] = df['sample_name'].str.extract(r'\/([^\/]*)\.')
df['sample'] = df['sample'].apply(lambda x: x.split(".", 1)[0])

df.drop("sample_name", axis = 1, inplace = True)

columns = df.columns.tolist()
columns = ["sample"] + columns[:-1]
df = df[columns]

print(df.head(10))

df.to_csv("/global/scratch/users/sridharan/scripts/process_d4/1000G/outputs/1000G_readdepth_CLEAN.txt", sep = "\t", index = False)
