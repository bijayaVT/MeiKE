README authors: Yao Zhang, Bijaya Adhikari, Steve Jan and B. Aditya Prakash.
Dated: March 2017.

A citation to the following paper will be greatly appreciated:

MeiKe: Influence-based Communities in Networks
Yao Zhang, Bijaya Adhikari, Steve Jan and B. Aditya Prakash
SIAM Conference on Data Mining (SDM 2017), April 2017, Houston

===============================================================

Requirement:
Matlab, Python 2.X, networkX package

===============================================================
Note: You need to change the correct MATLAB_PATH in the "run.sh". You may need to include the directory of unordered_map and unordered_set in the makefile.

Usage:

First do 'make' (to compile sources)
then:
   ./run.sh

The result is in "result" file
==============================================================

To see a Demo:
Again first do 'make'
then
   'make demo'

The result is in "result" file

==============================================================
Input:

edgelist:
node_1 node_2 probability_1_to_2 probability_2_to_1
1 2 0.1 0.2

====================================================================
Output:

The communities:
community_id:
node_1
node_2
...
