#!/bin/bash   

matlabpath='/usr/local/R2011B/bin/matlab'
percent='80'
edge='./example/oregon.inf'
directory='./example/'

########################################
#tmp variales

media=$directory"media_nodes"
M_degree=$directory"m_degree"
tmp=$edge"_final_map_"$percent

python src/coarse_net.py $edge $percent $matlabpath
python src/get_media.py $tmp   $media
python src/genzvaluelist.py $edge $media $media > $M_degree
python src/meike.py  $edge  5 500  undirected $media $M_degree  > result

