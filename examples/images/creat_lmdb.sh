#!/usr/bin/env sh
DATA=examples/images
rm -rf $DATA/img_train_lmdb
build/tools/convert_imageset --shuffle \
	--resize_height=256 --resize_width=256 \
	/home/lvfeng/trunk/caffe-refs/caffe/examples/images/ $DATA/train.txt  $DATA/img_train_lmdb
