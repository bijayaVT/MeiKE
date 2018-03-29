import subprocess
import time
import sys

# Usage: python score_and_coarsen.py graph_name percent_of_vertices_to_merge matlab_path
""" Input: graph_name and percentage of vertices to merge
Assumes: The graph (in tab separated .inf format) is present in (#../data/original/) ~/memetracker/connected/intnetworks. 
Assumes graph is strongly connected as in paper.
Process: 
1. Runs matlab code to score edges
2. Merges specified number of edges (i.e. vertices)
"""

print len(sys.argv)
if len(sys.argv)!=4:
    print 'Check usage'

graph = sys.argv[1]
percent = sys.argv[2]
matlab_path=sys.argv[3]
t1=time.time()

score_file = graph+'_scores'
input_graph = graph

print 'Scoring started'
matlab_function="getEigenScore('"+input_graph+"', '"+score_file+"')"
subprocess.call([matlab_path,"-nosplash","-nojvm","-r", matlab_function])
print 'Finished Scoring'


coarse_graph =graph+'_coarse_'+percent
map_file = graph+'_final_map_'+percent
temp = graph+'_time'

print 'Coarsening started'
subprocess.call(["src/CoarseNet", input_graph, score_file, percent, '0', coarse_graph, map_file, temp])

print 'Finished Coarsening'
t2=time.time()
cost_time=t2-t1

time_file= graph+'_coarse_'+percent+'_cost_time'
f=open(time_file,'w')
f.write("%f \n" % cost_time)
f.close()
