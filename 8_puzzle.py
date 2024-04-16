# -*- coding: utf-8 -*-
"""8-puzzle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pue3mALGHFU2ubsp2-qmadPYMsY90g7s

**Name:** Vedant Bhutada

**Batch:** A4

**Roll:** 69

write a program to implement 8-puzzle by using bfs
"""

from collections import deque

class Node:
   def __init__(self, state, parent=None, action="Initial", cost=0):
       self.state = state
       self.parent = parent
       self.action = action
       self.cost = cost

   def incr_cost(self):
       self.cost+=1

   def __str__(self):
       return f"Node({self.state}, {self.parent}, {self.action}, {self.cost})\n"


class Puzzle:
   def __init__(self, initial_state, goal_state):
       self.initial_state = initial_state
       self.goal_state = goal_state

   def get_blank_position(self, state):
       for i in range(len(state)):
           if state[i] == 0:
               return i

   def swap(self, state, i, j):
       state[i], state[j] = state[j], state[i]
       return state

   def get_possible_moves(self, state):
       zero_position = self.get_blank_position(state)
    #    possible_actions = ["UP", "DOWN", "LEFT", "RIGHT"]
       actions = []

       if zero_position > 2:
           actions.append("UP")
       if zero_position < 6:
           actions.append("DOWN")
       if zero_position % 3 != 0:
           actions.append("LEFT")
       if zero_position % 3 != 2:
           actions.append("RIGHT")

       return actions

   def execute_move(self, state, action):
       zero_position = self.get_blank_position(state)
       temp_state = list(state)

       if action == "UP":
           temp_state = self.swap(temp_state, zero_position, zero_position - 3)
       elif action == "DOWN":
           temp_state = self.swap(temp_state, zero_position, zero_position + 3)
       elif action == "LEFT":
           temp_state = self.swap(temp_state, zero_position, zero_position - 1)
       elif action == "RIGHT":
           temp_state = self.swap(temp_state, zero_position, zero_position + 1)

       return temp_state

   def goal_test(self, state):
        return all(a == b for a, b in zip(state, self.goal_state))


   def solve_puzzle(self):
        initial_node = Node(self.initial_state)
        frontier = deque([initial_node])
        explored = []

        while frontier:
            current_node = frontier.popleft()
            explored.append(current_node.state)
            print(self.goal_test(current_node.state), current_node.state, "level: ", current_node.cost)
            if self.goal_test(current_node.state):
                path = []
                while current_node.parent is not None:
                    path.append((current_node.state, current_node.action))
                    current_node = current_node.parent
                path.append((current_node.state, current_node.action))
                return path[::-1]
            for action in self.get_possible_moves(current_node.state):
                child_state = self.execute_move(current_node.state, action)
                if child_state not in explored:
                    child_node = Node(child_state, current_node, action, current_node.cost + 1)
                    frontier.append(child_node)

        # If the frontier becomes empty and the goal is not reached, return None
        return None

def main():
    initial_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    goal_state = [7, 0, 5, 2, 4, 3, 1, 6, 8]
    puzzle = Puzzle(initial_state, goal_state)
    soln = puzzle.solve_puzzle()

    if soln is None:
        print("No solution found.")
    else:
        for ele in soln:
            ctr = 0
            for row in ele[0]:
                print(row, end=" ")
                ctr += 1
                if ctr == 3:
                    print("\n")
                    ctr = 0
            print(f"{ele[1]}\n=================")

if __name__ == '__main__':
    main()



from collections import deque

class Node:
   def __init__(self, state, parent=None, action="Initial", cost=0):
       self.state = state
       self.parent = parent
       self.action = action
       self.cost = cost

   def incr_cost(self):
       self.cost+=1

   def __str__(self):
       return f"Node({self.state}, {self.parent}, {self.action}, {self.cost})\n"


class Puzzle:
   def __init__(self, initial_state, goal_state):
       self.initial_state = initial_state
       self.goal_state = goal_state

   def get_blank_position(self, state):
       for i in range(len(state)):
           if state[i] == 0:
               return i

   def swap(self, state, i, j):
       state[i], state[j] = state[j], state[i]
       return state

   def get_possible_moves(self, state):
       zero_position = self.get_blank_position(state)
    #    possible_actions = ["UP", "DOWN", "LEFT", "RIGHT"]
       actions = []

       if zero_position > 2:
           actions.append("UP")
       if zero_position < 6:
           actions.append("DOWN")
       if zero_position % 3 != 0:
           actions.append("LEFT")
       if zero_position % 3 != 2:
           actions.append("RIGHT")

       return actions

   def execute_move(self, state, action):
       zero_position = self.get_blank_position(state)
       temp_state = list(state)

       if action == "UP":
           temp_state = self.swap(temp_state, zero_position, zero_position - 3)
       elif action == "DOWN":
           temp_state = self.swap(temp_state, zero_position, zero_position + 3)
       elif action == "LEFT":
           temp_state = self.swap(temp_state, zero_position, zero_position - 1)
       elif action == "RIGHT":
           temp_state = self.swap(temp_state, zero_position, zero_position + 1)

       return temp_state

   def goal_test(self, state):
        return all(a == b for a, b in zip(state, self.goal_state))


   def solve_puzzle(self):
        initial_node = Node(self.initial_state)
        frontier = deque([initial_node])
        explored = []

        while frontier:
            current_node = frontier.popleft()
            explored.append(current_node.state)
            print(self.goal_test(current_node.state), current_node.state, "level: ", current_node.cost)
            if self.goal_test(current_node.state):
                path = []
                while current_node.parent is not None:
                    path.append((current_node.state, current_node.action))
                    current_node = current_node.parent
                path.append((current_node.state, current_node.action))
                return path[::-1]
            for action in self.get_possible_moves(current_node.state):
                child_state = self.execute_move(current_node.state, action)
                if child_state not in explored:
                    child_node = Node(child_state, current_node, action, current_node.cost + 1)
                    frontier.append(child_node)

        # If the frontier becomes empty and the goal is not reached, return None
        return None

def main():
    initial_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    goal_state = [1, 2, 3, 4, 5,0, 7, 6, 8]
    puzzle = Puzzle(initial_state, goal_state)
    soln = puzzle.solve_puzzle()

    if soln is None:
        print("No solution found.")
    else:
        for ele in soln:
            ctr = 0
            for row in ele[0]:
                print(row, end=" ")
                ctr += 1
                if ctr == 3:
                    print("\n")
                    ctr = 0
            print(f"{ele[1]}\n=================")

if __name__ == '__main__':
    main()
