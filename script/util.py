
def get_files( dirPath: str, regex: str="*", recursive=False ):
    import glob
    
    if recursive is True:
        files = glob.glob( f"{dirPath}/**/{regex}", recursive=True )
        return files
    
    files = glob.glob( f"{dirPath}/{regex}" )
    return files


def GetFileName( filePath ):
    import os
    return os.path.basename( filePath )

def get_filename_without_extension( filePath ):
    import os
    return os.path.splitext( os.path.basename( filePath ) )[0]

