# maze_with_depth-first_search_algorithm
maze-solving algorithm using depth-first search
## **depth-first search** is a search algorithm that always expands the deepest node in the frontier.
### frontier :- implemented using a stack data structure, **stack** is a last-in first-out data type.
### depth-first search algorithm steps:-
• Start with a frontier that contains the initial state. 
• Start with an empty explored set. 
• Repeat: 
• If the frontier is empty, then no solution. 
• Remove a node from the frontier. 
• If node contains goal state, return the solution. 
• Add the node to the explored set. 
• Expand node, add resulting nodes to the frontier if they 
aren't already in the frontier or the explored set.

### Depth-first search algorithm Pseudocode:-
DepthFirstSearch(start, goal):
    Create an empty stack frontier
    Push the start node onto the frontier
    
    Create an empty set explored
    
    while frontier is not empty:
        node = Pop the top node from the frontier
        
        if node is the goal:
            return node  // Solution found
        
        Add node to explored set
        
        for each neighbor in neighbors of node:
            if neighbor is not in explored and not in frontier:
                Push neighbor onto the frontier
                
    return None  // No solution found
