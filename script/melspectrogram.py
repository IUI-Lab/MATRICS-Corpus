
import numpy as np
import librosa

import os
from util import *


def create_melspectrogram( src, dest ):
    y, sr = librosa.load( src, sr=sampling_rate )

    S = librosa.feature.melspectrogram( y=y, sr=sr, n_fft=window_length, hop_length=hop_length, n_mels=n_mels )
    S_dB = librosa.power_to_db(S, ref=np.min) / 100.0 # データ中の最小値を基準にしたdbへの変換．
                                                      # その後0-1に収めるため100.0で割った．
                                                      # ここではデータの最大値が100を超えることがないと想定しているが，超える場合は100.0を調整すること．
    return S_dB.transpose()


if __name__ == '__main__':

    # src_files = [
    #     r"H:\MATRICS-Corpus\__private\export\Audio\BP-S1-A.wav",
    #     r"H:\MATRICS-Corpus\__private\export\Audio\BP-S1-D.wav"
    # ]
    src_files = get_files( r"H:\MATRICS-Corpus\__private\export\Audio" )

    dest_dir = r"H:\MATRICS-Corpus\speech.melspectrogram"

    # --- hyper parameters -----
    sampling_rate = 44100
    window_length= 2048
    ideal_fps = 50
    n_mels = 64

    hop_length, mod = divmod( sampling_rate, ideal_fps ) 

    if mod is not 0:
        raise Exception( "srを割り切れる数をideal_fpsにして！" )


    for src in src_files:
        file_name = get_filename_without_extension( src )
        dest = os.path.join( dest_dir,  f"{file_name}.txt" )

        print( f"{src} -> {dest}" )
        melspectrogram = create_melspectrogram( src=src, dest=dest )
        np.savetxt( dest, melspectrogram, fmt="%.5f", delimiter="\t" )




    
