import os
import glob
import sys
import subprocess
import shutil
from pathlib import Path
from datetime import datetime

import pandas as pd
import numpy as np

def align_responses():


    # grab path of "data-csv"
    path_csvdata = r"\\path\to\data\3cd\data-csv"
    print(f"\nThis is the INPUT path: \n{path_csvdata}")
    path_csvdata = Path(path_csvdata) # use pathlib

    # define output path
    path_output = Path(r"\\path\to\data\3cd\output")
    print(f"\nThis is the OUTPUT path: \n{path_output}")

    # user input: make sure this has been read
    input("\nPress Enter to continue...\n")

    # iterate through files in folder and take all csv files
    print("\nThese files will be analysed:")
    for csv_file_name in path_csvdata.glob("*.csv"):
        print(csv_file_name.name) # print file name only

    # user input: make sure this has been read
    input("\nPress Enter to continue...\n")
    
    # align responses of csv files
    for csv_file_name in path_csvdata.glob("*.csv"):
        
        # read csv file
        df = pd.read_csv(csv_file_name,
                        names=["time [ms]", f"{csv_file_name.stem}"]) # add column names
        #print(df)

        # select value of 2nd column where time is either -0.5 or -0.4
        flashpoints = [-0.5, -0.4]
        mask = df["time [ms]"].isin(flashpoints)
        df_flash = df[mask]
        print(f"\nJust to inform. This is the row to be shifted to zero of {f'{csv_file_name.stem}'}:\n{df_flash}")
        
        value_shift = df[f"{csv_file_name.stem}"][mask].values[0]
        #print(f"\nThis is the value to be shifted to zero of {f'{csv_file_name.stem}'}:\n{value_shift}")
        
        # substract value_shift from the whole column
        df[f"{csv_file_name.stem}_aligned"] = df[f"{csv_file_name.stem}"].apply(lambda x: x - value_shift)
        #print(df)
        
        # save in output folder
        today = datetime.now() # use datetime
        df.to_csv(f"{path_output}/{csv_file_name.stem}_{today.year}-{today.month:02d}-{today.day:02d}.csv", index=False)





