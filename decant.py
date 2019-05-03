import search #interface
import sys
sys.setrecursionlimit(50)
class DECANT(search.Nodes):
    #return the starting state vessels
    def start(self):
        return [7,0,0]
    #if node is == to goal node, returns true
    def goal(self,node): 
        return node == [2,2,3]
    #successors
    def succ(self,node):
            # set capacities for vessels
            cap = [7,4,3];
            for i in range(len(node)):
                for j in range(len(node)): 
                    #create a safety copy as proffessor said
                    new_n = node[:]
                    #vessel i to vessel j                
                    if (new_n[i]>0 and new_n[j]<cap[j]):
                            #calculate the second vessel difference and compaire with first vessel choose min of them
                            differ = min(new_n[i],cap[j]-new_n[j])
                            new_n[i]= new_n[i]-differ
                            new_n[j]= new_n[j]+differ
                            yield new_n
