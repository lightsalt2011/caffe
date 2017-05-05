# /usr/bin/env sh
DATA=examples/images
echo "Create train.txt..."
rm -rf $DATA/train.txt
find $DATA -name *cat.jpg | cut -d '/' -f3 | sed "s/$/ 1/">>$DATA/train.txt
find $DATA -name *bike.jpg | cut -d '/' -f3 | sed "s/$/ 2/">>$DATA/tmp.txt
cat $DATA/tmp.txt>>$DATA/train.txt
rm -rf $DATA/tmp.txt
echo "Done.."
