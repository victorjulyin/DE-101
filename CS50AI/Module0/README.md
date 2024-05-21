## Definitions
    - Agent - something or someone who perform the actions (AI or a car for example)
    - Initial state - the condition that we have in the start of the work
    - State - just some condition
    - Action - choices that we have in a state. Just a function that returns set of actions that can be executed
    - Transition model - result (new state) of performing some action in some state. Like a function "some_new_state = f(state, action)". It describes how states and actions related to each other
    - State space - set of all the possible states that can be reached from the current states with any amount of actions. IMAGINE GRAPH WITH ARROWS HERE. Points = states, arrows = actions.
    - Goal test - way to determine that the given state is a goal state
    - Path cost - numerical cost of associated path. Like the goal should be reached in a rational way. Generally every certain action has some cost
    - Node - data structure to store the info about a certain state. Data from the initial state to the current state. It contains:
        - a state
        - a parent (node that generated this node)
        - an action (action applied to the parent to get node)
        - a path cost (from initial state to node)
    - Frontier - data structure that contains all the possible next steps that we can explore next

### Approach of solving the search problem
    - Starting with a frontier that contains only the initial state
    - Start with an empty explored set
    - Repeat by loop:
        - if the frontier is empty then there is no solution
        - remove a node from the frontier (like check this certain node)
        - if node contains the solution (goal test) then return the result
        - if not:
            - Add the node to the explored set (nodes that we've already checked)
            - Expand node by adding resulting nodes to the frontier (trying to explore next steps) if they are not in the frontier already AND not in the explored set

## How to choose the node? (point 3.2 - remove a node from the frontier)

### Depth first search (DFS)
    In this approach we're using stack Stack.
    - Stack - last-in = first-out data type (like a stack of plates). Which means that firstly we explore the node that got to a frontier as the last one.
    - Depth first search (DFS) - search algorithm that always expands the deepest node in the frontier. When it hits a dead-end it returns to the last action and tries the new node etc

### Breadth first search (BFS)
    In this approach we're using stack Queue.
    - Queue - first-in = first-out data type

## Uninformed and Informed search
    Let's look at the maze below.

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module0/maze_informed_uninformed.jpg" width=70% height=70%></p>

    At this point the program has a choice - go left or go right. And in case we're using BFS, it will just check the whole graph. In case we're using DFS it may check the whole graph too.

    If human tries to solve this problem, he will try to go right, because he sees that he's getting closer to the goal. And if the computer could see the coordinates of the point A and point B it could calculate that it is bettern to turn right to reach the goal.

    - Uninformed search - search strategy that uses no problem-specific knowledge. Like it doesn't care what the size of the maze is or anything. It just tries to find a solution step by step
    - Informed search - search strategy that uses problem-specific knowledge to find solutions more eficiently. So it has some data that helps to reach the goals better. Problem-specific knowledge in case of this maze - "better to be in a square that geographically closer to the point B".

    Informed search has several subtypes

### Greedy best-first search

    For instance, we have the maze below. Which of the squares is better for the goal - C or D? A human will just answer - D. Because it is closer geographically to the final goal.

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module0/readme_pics/maze_coordinates1.jpg" width=70% height=70%></p>

    But how can we exlain it to the machine? We need to create a heuristic function that is gonna count the estimated path length. And in this case it can be retty simple - just count how many steps we need to perform to get to the goal just by the X and Y axises (omitting the walls).

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module0/readme_pics/maze_coordinates2.jpg" width=70% height=70%></p>

    So generally every square has its own "price" of how many steps it is far from the goal. And machine can rely on this data.

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module0/readme_pics/maze_coordinates3.jpg" width=70% height=70%></p>

    But it is not always an optimal way to do it. For exanple, we could have a "snake"-shape maze and in this case it would be better to choose the other path. 

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module0/readme_pics/maze_coordinates4.jpg" width=70% height=70%></p>

    And that's where we get to the A * Search

### A * Search
    - A * Search - search algorithm that expands node with lowest value of g(n) + h(n), where:
        - g(n) is cost to reach the node (how many steps we had to perform to get to this certain node)
        - h(n) is estimated cost to goal (the amount of steps until the goal)

    So it's gonna look like this:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module0/readme_pics/maze_coordinates5.jpg" width=70% height=70%></p>

    We're summing the number of steps to reach this certain state and the estimated cost to goal.
    And this is the point where we need to make a decision:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module0/readme_pics/maze_coordinates6.jpg" width=70% height=70%></p>

    And the more rational option is to go up. Because of the SUM of the metrics. But at the state below we see that it may be rational to try out the other path:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module0/readme_pics/maze_coordinates7.jpg" width=70% height=70%></p>

    And it will be the optimal path:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module0/readme_pics/maze_coordinates8.jpg" width=70% height=70%></p>

    So the A * Search is an optimal solution if:
        - h(n) is admissable (never overestimates the true cost). It never tells us that we are further from the goal than we actually are.
        - h(n) is consistent (for every node "n" and successor (next state for example) "n`" with step cost "c", h(n) <= h(n`) + c). For instance, we are in some state. And we have some "price" of getting to the goal. And when we move to the next state, the price must be less for the cost of one step that we performed. So all the states are the same and the cost of the step is always the same.

## Adversarial search
    It is a type of search problem when the agent is trying to make an intellegent decision and there is an opponent who is fighting against to him.
    For example, a game - Tic-Tac-Toe (zeros-crosses)

### Minimax
    In this algorithm we have two opponents. And we set everything up like this: when "player1" wins it is "1", when "player2" wins it is "-1" and when noone wins it is 0. In this case "player1"'s goal is to maximize the score of the game. And opposite for the "player2".
    And then the program should try to check all the possible options of the game and choose the move that have more chances to win the game.
    What we need to run this game:
        - S - initial state (empty field)
        Functions:
            - Player(s) - returns which player should move in state S
            - Actions(s) - returns which actions are available in state S
            - Result(s, a) - returns state after action A applied to state S
            - Terminal(s) - checks if state S is a terminal state (if someone won the game or it is impossible to continue)
            - Utility(s) - final numerical value for the terminal state S (-1, 0 or 1)

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module0/readme_pics/minimax1.jpg" width=70% height=70%></p>

    Now let's look at the picture above. This is a strategy of how the agent needs to choose the move.
    It is some simple game that has only three choices for player1 and after that 3 choices for player2.
    For example the agent (our computer, AI, we are) is the MAX player (green). It checks out all the options he has.
    In the bottom we can see the Terminal States. So every triangle reflects the final score of the game.
    In the middle level we see the minimal value of score for every bottom nodes. Why minimal? Because if the opponent (MIN player) makes intelligent desicions, it will choose the option with the minimal score. So when we can say that choice in the middle == minimal score in the bottom.

### Optimizations - Alpha-Beta pruning

    We've figured out how to use the minimax algorithm to find the solution in a game. But what if we want to optimize it and find it more efficient?
    Let's look at the picture below.

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module0/readme_pics/minimax2.jpg" width=70% height=70%></p>

    For example we've checked the first node (in the left). We found out that it has a score "4". When we check the next node and we find that one of the Terminal States in the bottom is 3 which is less than the minimal score of the first node (3 < 4), we don't need to check all the rest states on this node. Because we already know that this choice is not optimal, better to choose the left node. The same with the right node. When we see that it's score is 2 it doesn't make sense to check other bottom states.
    With this technique we are reducing the number of the nodes to explore to find the optimal solution.

### Optimizations - Depth-Limited minimax

    Tic-Tac-Toe is a pretty simple game. And I was shocked when I knew that there are 268k of the possible nodes in this game.
    But what about the more complex games like chess? It has 10^29000 of the possible options of the game. Computer can't explore all the possible options to find the optimal solution.
    And in this case we can use Depth-Limited minimax. Standard minimax is unlimited, so it tries to go deep as much as possible until the end of the game to find a solution. But in a Depth-Limited minimax we set the maximal depth of the node to explore. So there are gonna be much less options to explore.
    But in this case we also need an Evaluation funcition - the function that estimates the expected utility of the game from a given state. 
    And as better this function predicts the utility than better the AI works
