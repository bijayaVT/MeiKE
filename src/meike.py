import networkx as nx
import sys
import random
import math
import time
from sets import Set

zdict={}
M=[]
def readfile(mediafile,zlistfile):
    f=open(mediafile,'r')
    lines=f.readlines()
    for line in lines:
        M.append(int(line))
    f.close()
    f=open(zlistfile,'r')
    lines=f.readlines()
    for line in lines:
        a= line.split('\t')
        zdict[ int(a[0]) ] = int(a[1])


    f.close()




def weba(g, k, iteration):

    #community: a list of Sets [(1,2,3), (5,3,2)] Set
    community_list=[]
    #print "start greedy"
    candidates=greedy(g, k, iteration)
    #print "finsh greedy"
    candi_size=len(candidates)
    graph_size=len(g)

    #l: number of communities
    nonzerozlist = []

    for i in zdict.keys():
        if zdict[i] > 0 :
            nonzerozlist.append( i )

    l=len(candidates)

    for i in range(l):
        #weights w
        w={}

        origS_index=random.sample(range(candi_size), 1)
        origS_index=origS_index[0]
        S=candidates[origS_index]

        for node in g.nodes():
            w[node]=0.0
        #S is greedy generate
        for node in list(S):
            w[node]=1.0

        #nw
        nw={}
        ## all weight initial is 0
        for node in g.nodes():
            nw[node]=0.0

        for u in g.nodes():

            for v in g.neighbors(u):

                if v in zdict:
                    nw[u]=nw[u]+zdict[v]*w[v]

#        print 'finish nw'
        count = 0
        #initialize pairwised delta: delta[v][u]
        delta={}



        ttt=0
        #print "i=%d" %i
        while True: ### define a iteration to make it stop
            #print 'fff'
            ttt+=1

            #print ttt
            if ttt == iteration:
                break
            max_delta=-1.0
            judge_delta=-1.0
            max_u=-1
            max_v=-1
            count = 0

            for u in (set(g.nodes()) - set(M)):
                if w[u] == 1:
                    continue

                for v in (set(g.nodes()) - set(M)):
                    if u == v:
                        continue
                    if w[v]==0:
                        continue
                    if not (g.has_edge(u,v)):
                        temp=min( 1.0-w[u], w[v] )




                    else:
                        if (u in zdict) and (v in zdict):
                            if zdict[u] > 0 and zdict[v] > 0:
                                temp=min( 1.0-w[u], w[v],  ( zdict[u]* nw[u]-zdict[v]*nw[v])/(2.0*zdict[u]*zdict[v]            ))
                            else:
                                temp = min( 1-w[u],w[v])
                        else:
                            temp = min( 1-w[u],w[v])





                    if temp>max_delta:
                        max_delta=temp
                        max_u=u
                        max_v=v
                    if temp>judge_delta:
                        temp=judge_delta
                        max_u=u
                        max_v=v


            if judge_delta<=1e-6:
                break



            w[max_u]=w[max_u]+max_delta
            w[max_v]=w[max_v]-max_delta
            for nei in g.neighbors(max_u):
                nw[nei]=nw[nei]+max_delta
            for nei in g.neighbors(max_v):
                nw[nei]=nw[nei]-max_delta

        #get kernel community
        C=[]
        for v in w.keys():
            if math.fabs(w[v]-1.0)<1e-5:
                C.append(v)
        C=Set(C)
        if C not in community_list:
            community_list.append(C)

    #l: number of communities
    l=int(((graph_size*1.0)/k))

    return community_list

def greedy(g, k, iteration):
    #community: a list of Sets [(1,2,3), (5,3,2)] Set
    comm_list=[]
    graph_size=len(g)
    nonzerozlist = []

    for i in zdict.keys():
        if zdict[i] > 0 :
            nonzerozlist.append( i )


    #l: number of communities

    l=int((( len(nonzerozlist)   *1.0)/k))

    l=iteration
    for i in range(l):
        #print i,l
        degree={}
        score={}
        G=g.copy()
        for node in G.nodes():
            degree[node]=0
        v=random.sample(nonzerozlist, 1)
        S=Set(v)
        v=v[0]
        degree[v]=-1
        for i in M:
            G.remove_node(i)
        for node in G.neighbors(v):
            degree[node]=degree[node]+1
        for i in degree.keys():
            if i in zdict:
                score[i] = degree[i] * zdict[i]
            else:
                score[i] = degree[i]
        G.remove_node(v)

        removel=[]
        for i in range((k-1)):
            #select k-1 nodes in S
            selected_node=max(score.iterkeys(),key=lambda k:score[k])
            if score[ selected_node] == 0 :
                selected_node=random.sample(G.nodes(), 1)[0]
            S.add(selected_node)
            degree[selected_node]=-10000000000 #make selected_node do not be chose again
            score[selected_node] = -100000
            for node in G.neighbors(selected_node):
                degree[node]=degree[node]+1
            for i in degree.keys():
                if i in zdict:
                    score[i] = degree[i] * zdict[i]
                else:
                    score[i] = degree[i]

            removel.append(selected_node)
            G.remove_node(selected_node)

        if S not in comm_list:
            comm_list.append(S)
   # print comm_list
    return comm_list

def create_directed_graph(filename):
    g=nx.DiGraph()
    f=open(filename,'r')
    lines=f.readlines()
    for line in lines:
        temp=line.split()
        #[node1, node2, weight]=line.split()
        index1=int(temp[0].strip())
        index2=int(temp[1].strip())
        #weight=eval(weight)
        #g.add_edge(index1,index2,weight=weight)
        g.add_edge(index1,index2)

    f.close()
    return g

def create_undirected_graph(filename):
    g=nx.Graph()
    f=open(filename,'r')
    lines=f.readlines()
    for line in lines:
        temp=line.split()
        #[node1, node2, weight]=line.split()
        index1=int(temp[0].strip())
        index2=int(temp[1].strip())
        #weight=eval(weight)
        #g.add_edge(index1,index2,weight=weight)
        g.add_edge(index1,index2)

    f.close()
    return g

def main():
    #edgelist
    if len(sys.argv)<4:
        print "Usage: python weba.py edgelist kernel_size iteration directed/undirected\nExample: python weba.py karate 5 1 undirected"
        exit(0)
    start_time = time.time()
    filename=sys.argv[1]
    #kernelsize
    k=int(sys.argv[2])
    iteration=int(sys.argv[3])
    mediafile=sys.argv[5]
    zlistfile=sys.argv[6]
    readfile(mediafile,zlistfile)


    tag=sys.argv[4]
    if tag not in ["directed", "undirected"]:
        print "tag parameter must be directed/undirected"
        exit(0)
    if tag=="directed":
        g=create_directed_graph(filename)
    if tag=="undirected":
        g=create_undirected_graph(filename)

    #community: a list of Sets [(1,2,3), (5,3,2)] Set
    #greedy algorithm
    #community_list=greedy(g, k, iteration)
    #weba
    community_list=weba(g, k, iteration)
    count = 1
    for i in   community_list:
        print count,':'
        for j in i:
            print j
        count = count +1
    #print("--- %s seconds ---" % (time.time() - start_time))


if __name__=='__main__':
    main()
