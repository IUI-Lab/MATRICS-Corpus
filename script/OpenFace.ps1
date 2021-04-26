
# $openface = "./FeatureExtraction.exe"
$openface = "H:\MATRICS-Corpus\__private\__workspace\openface\OpenFace_2.2.0_win_x64\FeatureExtraction.exe"

# $targets = (Get-ChildItem -Path "H:\MATRICS-Corpus\__private\export\FaceFrontalVideo" )
$targets = @(
    "H:\MATRICS-Corpus\__private\export\FaceFrontalVideo\BP-S3-D.mp4"
    "H:\MATRICS-Corpus\__private\export\FaceFrontalVideo\BP-S11-D.mp4"
) | ForEach-Object { New-Object System.IO.FileInfo $_ }

$dest = "./dest"



New-Item -ItemType Directory $dest

Write-Host "targets are...: " $targets
Write-Host "total of target is: " $targets.Length

# Pause

foreach ($target in $targets) {

    $outDir = Join-Path dest $target.Name.replace( ".mp4", "" )

    Write-Host $target.FullName -> $outDir

    

    & $openface -f $target.FullName -out_dir $outDir

    # & $openface -f $target.FullName -out_dir $outDir `
    #     -2Dfp -3Dfp -pdmparams -pose -aus -gaze -hogalign -tracked `
    #     -format_aligned jpg -g
    
}

