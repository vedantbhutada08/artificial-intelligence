# -*- coding: utf-8 -*-
"""15-puzzle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15p-IvSFDTec1wDvCmqJe5D8Z3IcUN0aT

**Name:** Vedant Bhutada

**Batch:** A4

**Roll:** 69

write a program to implement 15-puzzle by using bfs

Not Reachable
"""

from collections import deque

class Node:
    def __init__(self, state, parent=None, action="Initial", cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def incr_cost(self):
        self.cost += 1

    def __str__(self):
        return f"Node({self.state}, {self.parent}, {self.action}, {self.cost})\n"


class Puzzle:
    def __init__(self, initial_state, goal_state, puzzle_size):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.puzzle_size = puzzle_size

    def get_blank_position(self, state):
        for i in range(len(state)):
            if state[i] == 0:
                return i

    def swap(self, state, i, j):
        state[i], state[j] = state[j], state[i]
        return state

    def get_possible_moves(self, state):
        zero_position = self.get_blank_position(state)
        actions = []

        if zero_position - self.puzzle_size >= 0:
            actions.append("UP")
        if zero_position + self.puzzle_size < len(state):
            actions.append("DOWN")
        if zero_position % self.puzzle_size != 0:
            actions.append("LEFT")
        if zero_position % self.puzzle_size != self.puzzle_size - 1:
            actions.append("RIGHT")

        return actions

    def execute_move(self, state, action):
        zero_position = self.get_blank_position(state)
        temp_state = list(state)

        if action == "UP":
            temp_state = self.swap(temp_state, zero_position, zero_position - self.puzzle_size)
        elif action == "DOWN":
            temp_state = self.swap(temp_state, zero_position, zero_position + self.puzzle_size)
        elif action == "LEFT":
            temp_state = self.swap(temp_state, zero_position, zero_position - 1)
        elif action == "RIGHT":
            temp_state = self.swap(temp_state, zero_position, zero_position + 1)

        return temp_state

    def goal_test(self, state):
        return state == self.goal_state

    def is_solvable(self):
     def count_inversions(state):
         inversions = 0
         for i in range(len(state)):
             for j in range(i + 1, len(state)):
                 if state[i] > state[j] and state[i] != 0 and state[j] != 0:
                     inversions += 1
         return inversions

     inversion_count = count_inversions(self.initial_state)
     blank_row = self.initial_state.index(0) // self.puzzle_size

     if self.puzzle_size % 2 == 1:  # Odd puzzle size
         return inversion_count % 2 == 0
     else:  # Even puzzle size
         if blank_row % 2 == 0:  # Blank on even row counting from the top
             return inversion_count % 2 == 1
         else:  # Blank on odd row counting from the top
             return inversion_count % 2 == 0


    def solve_puzzle(self):
        if not self.is_solvable():
            return None

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

        return None


def main():
    puzzle_size = 4
    initial_state = [2,1,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    goal_state = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    puzzle = Puzzle(initial_state, goal_state, puzzle_size)
    soln = puzzle.solve_puzzle()
    if soln:
        for ele in soln:
            ctr = 0
            for row in ele[0]:
                print(row, end=" ")
                ctr += 1
                if ctr == puzzle_size:
                    print("\n")
                    ctr = 0
            print(f"{ele[1]}\n=================")
    else:
        print("Goal state is not reachable from the initial state.")


if __name__ == '__main__':
    main()

"""Possible"""

from collections import deque

class Node:
    def __init__(self, state, parent=None, action="Initial", cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def incr_cost(self):
        self.cost += 1

    def __str__(self):
        return f"Node({self.state}, {self.parent}, {self.action}, {self.cost})\n"


class Puzzle:
    def __init__(self, initial_state, goal_state, puzzle_size):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.puzzle_size = puzzle_size

    def get_blank_position(self, state):
        for i in range(len(state)):
            if state[i] == 0:
                return i

    def swap(self, state, i, j):
        state[i], state[j] = state[j], state[i]
        return state

    def get_possible_moves(self, state):
        zero_position = self.get_blank_position(state)
        actions = []

        if zero_position - self.puzzle_size >= 0:
            actions.append("UP")
        if zero_position + self.puzzle_size < len(state):
            actions.append("DOWN")
        if zero_position % self.puzzle_size != 0:
            actions.append("LEFT")
        if zero_position % self.puzzle_size != self.puzzle_size - 1:
            actions.append("RIGHT")

        return actions

    def execute_move(self, state, action):
        zero_position = self.get_blank_position(state)
        temp_state = list(state)

        if action == "UP":
            temp_state = self.swap(temp_state, zero_position, zero_position - self.puzzle_size)
        elif action == "DOWN":
            temp_state = self.swap(temp_state, zero_position, zero_position + self.puzzle_size)
        elif action == "LEFT":
            temp_state = self.swap(temp_state, zero_position, zero_position - 1)
        elif action == "RIGHT":
            temp_state = self.swap(temp_state, zero_position, zero_position + 1)

        return temp_state

    def goal_test(self, state):
        return state == self.goal_state

    def is_solvable(self):
     def count_inversions(state):
         inversions = 0
         for i in range(len(state)):
             for j in range(i + 1, len(state)):
                 if state[i] > state[j] and state[i] != 0 and state[j] != 0:
                     inversions += 1
         return inversions

     inversion_count = count_inversions(self.initial_state)
     blank_row = self.initial_state.index(0) // self.puzzle_size

     if self.puzzle_size % 2 == 1:  # Odd puzzle size
         return inversion_count % 2 == 0
     else:  # Even puzzle size
         if blank_row % 2 == 0:  # Blank on even row counting from the top
             return inversion_count % 2 == 1
         else:  # Blank on odd row counting from the top
             return inversion_count % 2 == 0


    def solve_puzzle(self):
        if not self.is_solvable():
            return None

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

        return None


def main():
    puzzle_size = 4
    initial_state = [2,1,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    goal_state = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    puzzle = Puzzle(initial_state, goal_state, puzzle_size)
    soln = puzzle.solve_puzzle()
    if soln:
        for ele in soln:
            ctr = 0
            for row in ele[0]:
                print(row, end=" ")
                ctr += 1
                if ctr == puzzle_size:
                    print("\n")
                    ctr = 0
            print(f"{ele[1]}\n=================")
    else:
        print("Goal state is not reachable from the initial state.")


if __name__ == '__main__':
    main()



"""reachable but memory out of bound problem"""

from collections import deque

class Node:
    def __init__(self, state, parent=None, action="Initial", cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def incr_cost(self):
        self.cost += 1

    def __str__(self):
        return f"Node({self.state}, {self.parent}, {self.action}, {self.cost})\n"


class Puzzle:
    def __init__(self, initial_state, goal_state, puzzle_size):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.puzzle_size = puzzle_size

    def get_blank_position(self, state):
        for i in range(len(state)):
            if state[i] == 0:
                return i

    def swap(self, state, i, j):
        state[i], state[j] = state[j], state[i]
        return state

    def get_possible_moves(self, state):
        zero_position = self.get_blank_position(state)
        actions = []

        if zero_position - self.puzzle_size >= 0:
            actions.append("UP")
        if zero_position + self.puzzle_size < len(state):
            actions.append("DOWN")
        if zero_position % self.puzzle_size != 0:
            actions.append("LEFT")
        if zero_position % self.puzzle_size != self.puzzle_size - 1:
            actions.append("RIGHT")

        return actions

    def execute_move(self, state, action):
        zero_position = self.get_blank_position(state)
        temp_state = list(state)

        if action == "UP":
            temp_state = self.swap(temp_state, zero_position, zero_position - self.puzzle_size)
        elif action == "DOWN":
            temp_state = self.swap(temp_state, zero_position, zero_position + self.puzzle_size)
        elif action == "LEFT":
            temp_state = self.swap(temp_state, zero_position, zero_position - 1)
        elif action == "RIGHT":
            temp_state = self.swap(temp_state, zero_position, zero_position + 1)

        return temp_state

    def goal_test(self, state):
        return state == self.goal_state

    def is_solvable(self):
     def count_inversions(state):
         inversions = 0
         for i in range(len(state)):
             for j in range(i + 1, len(state)):
                 if state[i] > state[j] and state[i] != 0 and state[j] != 0:
                     inversions += 1
         return inversions

     inversion_count = count_inversions(self.initial_state)
     blank_row = self.initial_state.index(0) // self.puzzle_size

     if self.puzzle_size % 2 == 1:  # Odd puzzle size
         return inversion_count % 2 == 0
     else:  # Even puzzle size
         if blank_row % 2 == 0:  # Blank on even row counting from the top
             return inversion_count % 2 == 1
         else:  # Blank on odd row counting from the top
             return inversion_count % 2 == 0



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

        return None


def main():
    puzzle_size = 4
    initial_state = [2,1,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    goal_state = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    puzzle = Puzzle(initial_state, goal_state, puzzle_size)
    soln = puzzle.solve_puzzle()
    for ele in soln:
        ctr = 0
        for row in ele[0]:
            print(row, end=" ")
            ctr += 1
            if ctr == puzzle_size:
                print("\n")
                ctr = 0
        print(f"{ele[1]}\n=================")


if __name__ == '__main__':
    main()