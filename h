opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt
  -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 4000
  -numNeg 200 -w 30 -h 30 -mode ALL -precalcValBufSize 1024
  -precalcIdxBufSize 1024

perl bin/createsamples.pl positives.txt negatives.txt samples 1500\
  "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle .3\
  -maxyangle .3 maxzangle .3 -maxidev 40 -w 30 -h 30"
