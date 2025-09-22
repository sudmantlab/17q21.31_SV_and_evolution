import os 
import argparse
import json
import numpy as np

"""
Generate a .json config file with the names of all the samples in the .d4 file folder for 1KG samples
"""

__author__="Samvardhini Sridharan"

cwd = os.getcwd() 

def make_json():

    j_out = {} #initializing an empty dictionary

    #j_out['d4_path'] = args.d4_path
    j_out['samples'] = {} 

    #updated as of 2023-05-25 to only reflect q0 files; "you want q0" - Peter
    sample_directory = "/global/scratch/p2p3/pl1_sudmant/human_diversity/d4_files/1KG/q0/"

    for sample in os.listdir(sample_directory):
        sample_name = sample[:-3]
        j_out["samples"][sample_name] = sample_directory+sample_name
    
    return j_out

FOUT = open(("{cwd}/"+ "d4_1KG.json").format(cwd=cwd),'w') 
FOUT.write(json.dumps(make_json(), indent=4, separators=(",", ": ")))
FOUT.close()
