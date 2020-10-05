#include<iostream> 
#include <list> 
using namespace std; 
class DiGraph 
{ 
    int V;    
    list<int> *adjList;    
public: 
    DiGraph(int V);   
    void addEdge(int v, int w);  
    void BFS(int s);   
}; 
DiGraph::DiGraph(int V) 
{ 
    this->V = V; 
    adjList = new list<int>[V]; 
}
 void DiGraph::addEdge(int v, int w) 
{ 
    adjList[v].push_back(w); 
} 
void DiGraph::BFS(int s) 
{ 
    bool *visited = new bool[V]; 
    for(int i = 0; i < V; i++) 
        visited[i] = false; 
    list<int> queue; 
    visited[s] = true; 
    queue.push_back(s); 
    list<int>::iterator i; 
   
    while(!queue.empty()) 
    { 
        s = queue.front(); 
        cout << s << " "; 
        queue.pop_front(); 
        for (i = adjList[s].begin(); i != adjList[s].end(); ++i) 
        { 
            if (!visited[*i]) 
            { 
                visited[*i] = true; 
                queue.push_back(*i); 
            } 
        } 
    } 
}
int main() 
{ 
    int number;
    cout<<"Enter the number of nodes in the graph:";
    cin>>number;
    DiGraph dg(number);
    int a;
    int con;
    cout<<"Enter the number of connections:";
    cin>>con;
    while(con--) {
        int b;
        cin>>a>>b;
        dg.addEdge(a, b);
    }
    cout << "Breadth First Traversal for given graph: "<<endl;
    cout<<"Enter the starting node value:";
    cin>>a;
    dg.BFS(a); 
   
    return 0; 

}


