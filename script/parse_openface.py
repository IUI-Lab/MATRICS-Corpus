

import pandas as pd
import numpy as np

import os
from util import *

if __name__ == '__main__':
    
    src_files = get_files( r"H:\MATRICS-Corpus\OpenFace.csv" )

    dest = r"H:\MATRICS-Corpus\script\dest"


    for src in src_files:

        import time
        start = time.time()

        table = pd.read_table( src, delimiter=", ", engine="python" )
        print( src )

        print( f"load: {time.time() - start}" )
        start = time.time()



        

        frame, face_id, timestamp, confidence, success = np.identity( 714, dtype=bool )[:5]
        gaze = table.columns.str.startswith( "gaze_" )
        eye_landmarks_2d = table.columns.str.match( "eye_lmk_[x|y]_\d+" )
        eye_landmarks_3d = table.columns.str.match( "eye_lmk_[X|Y|Z]_\d+" )
        pose = table.columns.str.startswith( "pose_" )
        position_2d = table.columns.str.match( "[x|y]_\d+" )
        position_3d = table.columns.str.match( "[X|Y|Z]_\d+" )
        pdm = table.columns.str.startswith( "p_" )
        au_r = table.columns.str.match( "AU\d+_r" )
        au_c = table.columns.str.match( "AU\d+_c" )

        print( f"idx: {time.time() - start}" )

        
        # extract...
        selections = [
            frame, face_id, timestamp, confidence, success,
            # gaze, eye_landmarks_2d, eye_landmarks_3d,
            # pose,
            # position_2d, position_3d,
            # pdm,
            au_r, au_c
        ]

        selections = np.sum( np.array(selections), axis=0 ).astype( np.bool )
        extraction = table.loc[:, selections]


        # with header
        extraction.to_csv(
            os.path.join( dest, f"{get_filename_without_extension(src)}.txt" ),
            sep="\t", index=False, float_format="%.5f"
        )
