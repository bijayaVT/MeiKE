import sys

final_map_file=sys.argv[1]
f=open(final_map_file,'r')
lines=f.readlines()
f.close()
    
f=open(sys.argv[2],'w')
for line in lines:
	[id, temp]=line.split(":")
	id=int(id.strip())
	list=temp.split(",")
	if len(list)==2:
		f.write("%d\n" %id)
f.close()
