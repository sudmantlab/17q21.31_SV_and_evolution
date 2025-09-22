from pyd4 import D4File  
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
test_folder = "/global/scratch/p2p3/pl1_sudmant/human_diversity/d4_files/1KG/q0/"
test_file = "HG02699.ERR3243019.PJL.d4"

file = D4File(test_folder + test_file)

#an array with the read depth at each individual base pair
chr17_data = file["chr17"]
"""

#overall block in hg38: [46000000,46310000]
#H1 block: [46095000,46123000]
#H2 block: [46143000,46238000]

"""
#normalization
def window_splitter(chromosome, window):
    smaller_arrays = [chromosome[i:i+window] for i in range(0, len(chromosome),window)]
    means = [sum(arr)/len(arr) for arr in smaller_arrays]
    return means

#removes outliers from the dataset in order to calculate the normalizing factor
def reject_outliers(data, m = 2):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0
    return data[s<m]
"""

def mean_depth(data, chrom_num):
    return data.mean("chr" + str(chrom_num))

def nf_generator(mean_depth):
    return 2/np.mean(mean_depth)

def read_depth_dict_df(data, chrom, nf, chrom_start, chrom_end, window_size, test_file):
    df_dict = {"sample_name":[], "chromosome":[], "normalizing_factor":[],  "window_start":[], "window_end": [], "read_depth": []}
    for i in range(chrom_start, chrom_end + window_size, window_size):
        df_dict["sample_name"].append(test_file)
        df_dict["chromosome"].append(chrom)
        df_dict["normalizing_factor"].append(nf)
        df_dict["window_start"].append(i)
        df_dict["window_end"].append(i + window_size)
        df_dict["read_depth"].append(data.mean("chr" + str(chrom) + ":" + str(i) + "-" + str(i + window_size))*nf)
    return pd.DataFrame.from_dict(df_dict)

"""
test_dict = read_depth_dict_df(file, 17, 0.04578, 42800001, 46800000, 100000)      
print(test_dict)

#test the function:
#moving_average = window_splitter(chr17_data, 1000) #windows are a 1000bp
#moving_average = np.array(moving_average) #convert to an NumPy array
#print(moving_average)

#moving_average_no_outliers = reject_outliers(moving_average, m = 2) #removing outliers

mean_depth_val = mean_depth(file, 17)
print("mean_depth_val", mean_depth_val)

normalizing_factor= 2/np.mean(mean_depth_val) #nf for this indiv
print("nf_normalized", normalizing_factor)

#copy_number_scaled = moving_average * nf_generator(moving_average_no_outliers) #scaling by the nf
#print(copy_number_scaled)

#plt.hist(copy_number_scaled) #output of the histogram
#plt.savefig("copynumber.png")

#post-normalization
print("average read depth over overall block:", chr17_data[46000000:46310000].mean()*normalizing_factor)
print("average read depth over the H1 block:", chr17_data[46095000:46123000].mean()*normalizing_factor)
print("average read depth over the H2 block:", chr17_data[46143000:46238000].mean()*normalizing_factor)
#print(create_nf_read_depth_dict(chr17_data, normalizing_factor))
#print(nf_read_depth_dict(chr17_data, normalizing_factor))

print(mean_depth(file, 17))
"""
