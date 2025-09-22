import os
import pandas as pd

folder_path = "/global/scratch/users/sridharan/scripts/process_d4/HGDP/outputs/nfs/"

merged_df = pd.DataFrame()

header_added = False

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        print("merging this file:", file_path)
        df = pd.read_csv(file_path, sep = "\t")
        merged_df = merged_df.append(df, ignore_index = True)
    
    if not header_added:
        merged_df = merged_df.append(df, ignore_index = True)
        header_added = True

    else:
        merged_df = merged_df.append(df.iloc[1:], ignore_index = True)

merged_df.to_csv("/global/scratch/users/sridharan/scripts/process_d4/HGDP/outputs/HGDP_readdepth.txt", sep = "\t", index = False)
