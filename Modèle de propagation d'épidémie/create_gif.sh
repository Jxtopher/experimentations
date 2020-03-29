#!/bin/bash

# 
# @file Create gif
# @author Jxtopher
# @brief Create Gif from images
# @version 1
# @date 2020-03
# 
#

# Rename
for j in {1..4}
do
	for i in $(ls | egrep "word-[0-9]{$j}.jpg")
	do
		mv $(echo $i) $(echo $i | sed 's/word-/word-0/g')
	done
done


## Add ticks in pic
for j in {00000..108}
do
    convert -font helvetica -fill white -pointsize 20 -draw "text 15,50 '$j'" word-$j.jpg aWord-$j.png
done


# img to video
mencoder mf://*.png -mf w=800:h=600:fps=5:type=png -ovc copy -oac copy -o output.avi

# video to gif
ffmpeg -i output.avi -pix_fmt rgb24  out.gif