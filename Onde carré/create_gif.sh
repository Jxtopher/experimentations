#!/bin/bash

# 
# @file Create gif
# @author Jxtopher
# @brief Create Gif from images
# @version 1
# @date 2020-03
# 
#

NAME_FILE="square-wave-"
DIR_PATH_IMG="images"
# Rename
for j in {1..4}
do
	for i in $(ls $DIR_PATH_IMG | egrep "$NAME_FILE[0-9]{$j}.png")
	do
		mv $DIR_PATH_IMG/$(echo $i) $DIR_PATH_IMG/$(echo $i | sed "s/$NAME_FILE/$(echo $NAME_FILE)0/g")
	done
done


DIR_PATH_WITH_MSG="images_with_ticks"
mkdir -p "images_with_ticks"
# Add ticks in pic
for j in {00000..198}
do
    convert -font helvetica -fill black -pointsize 25 -draw "text 375,21 '$j'" $DIR_PATH_IMG/square-wave-$j.png $DIR_PATH_WITH_MSG/$NAME_FILE$j.png
done


# img to video
mencoder mf://$DIR_PATH_WITH_MSG/*.png -mf w=800:h=600:fps=5:type=png -ovc copy -oac copy -o output.avi

# video to gif
ffmpeg -i output.avi -vf format=gray   out.gif