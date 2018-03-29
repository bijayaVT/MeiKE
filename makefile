#Make sure you set a correct matlab path
CC = g++
#CFLAGS = -I /usr/include/c++/4.6/
CFLAGS =
SOURCES=src/CoarseNet.cpp src/DisjointSets.cpp src/Edge.cpp src/graph.cpp
EXECUTABLE=src/CoarseNet

EXAMPLE = example/oregon.inf
PERCENT = 50
MATLAB_PATH = /Applications/MATLAB_R2011b.app/bin/matlab #/usr/local/R2011B/bin/matlab


$(EXECUTABLE): $(SOURCES)
	$(CC) $(SOURCES)  -std=c++0x $(CFLAGS) -o $(EXECUTABLE)

demo:
	./run.sh

clean:
	rm -rf $(EXECUTABLE) ./example/*_coarse_* ./example/*_final_map_* ./example/*_scores ./example/*_time ./example/media_nodes ./example/M_degree
