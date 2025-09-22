from pyd4 import D4File
import argparse
import numpy as np
from contextlib import redirect_stdout
from individual_CNV_binned import * #importing all the functions

def create_d4_table(args):
    #file = D4File(snakemake.input[0]) #adding the filename to filepath
    
    file_d4  = D4File(args.fn_file) #reading in the D4 file 

    output = args.output

    test_file = args.fn_file #the filepath name 

    chr17_data = file_d4["chr17"] #only has chromosome 17 data

    #using the functions from individual_CNV_binned.py

    mean_depth_val = mean_depth(file_d4, 17) #calculating the mean depth value. Note: This is not normalized and the outliers are not removed. This simply uses the existing pyd4 functions.

    nf = nf_generator(mean_depth_val) 

    df = read_depth_dict_df(file_d4, 17, nf, 42800001, 46800000, 1000, test_file) #values are for the 17q21.31 locus ONLY

    df.to_csv(output, sep = "\t", index = False)

"""
    #calculating the average CNV over the blocks
    moving_average = window_splitter(chr17_data, 1000) #splitting file into 1000bp
    moving_average_no_outliers = reject_outliers(moving_average) #removing outliers

    nf = nf_generator(moving_average_no_outliers)

    H1 = chr17_data[46095000:46123000].mean()*nf_generator(moving_average_no_outliers)

    H2 = chr17_data[46143000:46238000].mean()*nf_generator(moving_average_no_outliers)

    read_depth_dict = nf_read_depth_dict(chr17_data, nf)

    with open(output, "a") as f:
        print(df, file = f)
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "the specific filename from the .json config file")
    parser.add_argument("--fn_file", '-f', required = True, help = "Path to .d4 file")
    parser.add_argument("--output", '-o', required = True, help = "output .tsv/.json")    
    o = parser.parse_args()
    create_d4_table(o)
