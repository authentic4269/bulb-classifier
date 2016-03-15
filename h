opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt
  -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 800
  -numNeg 58 -w 80 -h 80 -mode ALL -precalcValBufSize 1024
  -precalcIdxBufSize 1024
