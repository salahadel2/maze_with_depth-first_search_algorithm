#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


# In[4]:


class StackFrontier():
    def __init__(self):
        self.frontier = []
        
    def add(self, node):
        self.frontier.append(node)
        
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node                            # return self.frontier.pop(-1)
            


# In[5]:


class Maze:
    # Constants for symbols
    wall_symbol = "#"
    path_symbol = " "
    
    def __init__(self, maze):
        self.height, self.width = self.maze_size(maze)
        self.start, self.goal = self.find_start_goal(maze)
        self.walls = self.track_walls(maze)
        self.solution = None
        
    def maze_size(self, maze):
        height = len(maze)
        width = max(len(row) for row in maze_data)  # len(maze[0, 0:])
        return height, width
    
    def find_start_goal(self, maze):
        initial_state = None
        goal_state = None
        for i, row in enumerate(maze):
            for j, col in enumerate(row):
                if maze[i][j] == "A":
                    inital_state = (i,j)
                if maze[i][j] == "B":
                    goal_state = (i,j)

        if inital_state is None or goal_state is None:
            raise ValueError("Maze must have exactly one start and one goal point")
        return inital_state, goal_state
    

# Track the walls in the maze.
    def track_walls(self, maze):
        walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if maze[i][j] == "A":
                        row.append(False)
                    elif maze[i][j] == "B":
                        row.append(False)
                    elif maze[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            walls.append(row)

        return walls
    
     # Expand node
    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result
    
    # depth-first search algorithm 
    def solve(self):         
            # Keep track of the number of states explored
        self.num_explored = 0
            # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)
            # Initialize an empty explored set
        self.explored = set()
            # Keep looping until a solution is found
        while True:
            # 1-check If the frontier is empty, then no solution.
            if frontier.empty():
                raise Exception("no solution")
            # 2-Remove a node from the frontier. 
            node = frontier.remove()
            self.num_explored += 1

            # 3-check If node contains goal state, return the solution.
            if node.state == self.goal:
                action = []
                cells = []
                while node.parent is not None:
                    action.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                # lists are reversed to ensure they are in the correct order, representing the solution path from start to goal.
                action.reverse()
                cells.reverse()
                self.solution = (action,cells)
                return
            # 4-Mark the node as explored
            self.explored.add(node.state)

            # 5-Add neighbors to the frontier (Expand node)
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state= state, parent= node, action= action)
                    frontier.add(child)

    
    # Print a visual representation of the maze.
    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()


# In[6]:


# main
maze_data = [
    ['#', '#', '#', ' ', ' ', 'B', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#'],
    [' ', ' ', ' ', ' ', ' ', '#', '#'],
    ['A', ' ', '#', '#', '#', '#', '#']]
maze = Maze(maze_data)
maze.print()
maze.solve()
maze.print()

