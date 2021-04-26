
# to avoid error
import os
os.environ["PATH"] += r";H:\MATRICS-Corpus\__private\__workspace\sox-14.4.2-win32\sox-14.4.2"

import pandas as pd
import opensmile

import util

if __name__ == '__main__':

    # srcs = [ r"H:\MATRICS-Corpus\__private\__workspace\opensmile-3.0-win-x64\example-audio\opensmile.wav" ]
    srcs = util.get_files( r"H:\MATRICS-Corpus\__private\export\Audio" )

    # dest_dir = r"H:\MATRICS-Corpus\speech.prosody"
    dest_dir = r"H:\MATRICS-Corpus\speech.mfcc"
    

    smile = opensmile.Smile(
        # feature_set= r".\OpenSmileConfigs\prosodyShs.conf",
        feature_set= r".\OpenSmileConfigs\MFCC12_0_D_A.conf",
        feature_level='lld',
    )

    # smile = opensmile.Smile(
    #     feature_set=opensmile.FeatureSet.ComParE_2016,
    #     feature_level=opensmile.FeatureLevel.Functionals
    # )

    # smile = opensmile.Smile(
    #     feature_set='my.conf',
    #     feature_level='func'
    # )

    

    for src in srcs:
        dest = os.path.join( dest_dir, f"{util.get_filename_without_extension(src)}.txt" )

        print( f"{src} -> {dest}" )

        df = smile.process_file( src )
        df = df.reset_index().drop( ["file"], axis=1 )

        df.to_csv( dest, sep="\t", index=None )


