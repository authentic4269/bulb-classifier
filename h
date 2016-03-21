opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt
  -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1200
  -numNeg 64 -w 60 -h 60 -mode ALL -precalcValBufSize 1024
  -precalcIdxBufSize 1024

perl bin/createsamples.pl positives.txt negatives.txt samples 1600\
  "opencv_createsamples -bgcolor 255 -bgthresh 10 -maxxangle 0.5\
  -maxyangle 0.5 maxzangle 0.5 -maxidev 40 -w 60 -h 60"
