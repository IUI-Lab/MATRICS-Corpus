
import os
import pympi.Elan
import pandas as pd


def eaf_to_df( eaf: pympi.Elan.Eaf ) -> pd.DataFrame:
    tier_names = list( eaf.tiers.keys() )

    def timeslotid_to_time( timeslotid: str ) -> float:
        return eaf.timeslots[ timeslotid ] / 1000

    def parse( tier_name: str, tier: dict ) -> pd.DataFrame:
        values = [ (key,) + value for key, value in tier.items() ]
        df = pd.DataFrame( values, columns=[ "id", "start", "end", "transcription", "unknown"] )

        df["start"] = df["start"].apply( timeslotid_to_time )
        df["end"] = df["end"].apply( timeslotid_to_time )
        df["ID"] = df.apply( lambda x: f"{tier_name}-{x.name}", axis=1 )
        df = df.reindex( columns=["ID", "start", "end", "transcription"] )
        
        return df

    dfs = [ parse(tier_name=name, tier=eaf.tiers[name][0]) for name in tier_names ]
    df = pd.concat( dfs )
    df = df.sort_values( "start" )
    df = df.reset_index( drop=True )
    return df


def formatting_transcription( tsc: str ) -> str:
    import re
    if re.match( "^\s+$", tsc ):
        return None
    if any( [ ignore_symbol in tsc for ignore_symbol in [ "(", ")" ] ] ):
        return None
    
    replaced = re.sub( r"\s", " ", tsc )
    replaced = replaced.replace( "{笑}", "{LAUGH}" )
    replaced = replaced.split( "/" )[1] if ("/" in replaced) else replaced
    return replaced



if __name__ == '__main__':
    import util

    # srcs = [ "./BP-S1.eaf" ]
    # dest_dir = "./"
    srcs = util.get_files( r"H:\MATRICS-Corpus\__private\nihei\DialogueActsLabeling\eaf" )
    dest_dir = r"H:\MATRICS-Corpus\utterance"
    

    for src in srcs:
        eaf = pympi.Elan.Eaf( src )
        df = eaf_to_df( eaf )

        df["transcription"] = df["transcription"].apply( formatting_transcription )
        df = df.dropna()
        print( df )

        dest = os.path.join( dest_dir, f"{util.get_filename_without_extension(src)}.txt" )

        df.to_csv( dest, sep="\t", index=False )
