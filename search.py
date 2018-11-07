# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import sys
from time import sleep

from game import Directions

n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def generalGraphSearch(problem, structure):
    """
    algoritme asli baraye piade sazie tamamie masaeel
    problem: soal
    structure: methode hale soal-> stack , list , ...
    """


    structure.push([(problem.getStartState(), "Stop", 0)])

    closed = []

    while not structure.isEmpty():


        path = structure.pop()

        curr_state = path[-1][0]
        if problem.isGoalState(curr_state):

            return [x[1] for x in path][1:]

            #agar hanooz visited nashode bashad

        if curr_state not in closed:
            closed.append(curr_state)

            for childs in problem.getSuccessors(curr_state):

                print(childs)
                if childs[0] not in closed:
                    successorPath = path[:]
                    successorPath.append(childs)
                    structure.push(successorPath)

    return False



def depthFirstSearch(problem):
#hal ba estefade az stack
    stack = util.Stack()

    return generalGraphSearch(problem, stack)

def breadthFirstSearch(problem):
    # hal ba estefasde az queue
    queue = util.Queue()

    return generalGraphSearch(problem, queue)

def uniformCostSearch(problem):
        #hal ba liste olaviat dar
    cost = lambda path: problem.getCostOfActions([x[1] for x in path][1:])

    # liste olaviat dar
    priorityQueue = util.PriorityQueueWithFunction(cost)

    return generalGraphSearch(problem, priorityQueue)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    cost = lambda path: problem.getCostOfActions([x[1] for x in path][1:]) + heuristic(path[-1][0], problem)

    # liste olaviat dar
    #olaviate ha bar asase cost ha
    priorityQueue = util.PriorityQueueWithFunction(cost)

    return generalGraphSearch(problem, priorityQueue)



bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch