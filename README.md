# Introduction
This repository contains all the homework coding projects from the Udacity class *Artificial Intelligence for Robotics -- Programming a Robotic Car*. Instructor for this class is Sebastian Thrun, a pioneer of autonomous driving and the previous leader of Google self-driving program. Sebastian gives a broad overview of the core subjects related to Robotics, including **Localization, Tracking, Motion planning, PID control and SLAM**. 

I finished all the coding assignments for the 6 units of this class. Sebastian's instruction is very clear so it is not difficult to finish the projects after understanding his lecture. All of my codes passed the online grader. I also made improvements to some of the algorithms. For example, the motion planning is related to a generic subject about search and planning. I have tried to write the code into a more standardized structure and used some more efficient algorithms, e.g. Dijkstra minimum path for the deterministic dynamic programming (Yes, I know Dijkstra is greedy not DP.). 

I learned a lot about Robotics from Sebastian's class, especially about some key theories. And it also won't take long to finish this class, if you are really focused. It took me one week but I haven't finished the final project of "chasing the escaping car" yet. (Definitely on my TODO list....)

Below is a summary of the codes in this repository, which are all the coding assignments for the class. Codes are all written in Python 3. (The original class codes are in Python 2)

1. file name note
2. PID figure
3. Search result
4. SLAM result

# Localization and tracking, Unit 1, 2, 3
> Unit 1, 2, 3 are all about the Robot localization and tracking, using different filters, including **Histogram filter, Kalman filter and Particle filter**


## Unit 1, Histogram filter

Histogram filter is also called Discrete filter. 
``` Python
## simple 1D localization using Histogram filter
DiscreteFilter_1D.py
## simple 2D localization using Histogram filter
DiscreteFilter_2D.py
```

## Unit 2, Kalman filter
```Python
## simple 1D localization using Kalman filter
KalmanFilter_locOnly.py
```

```python
KalmanFilter_tracking_1D.py
KalmanFilter_tracking_2D.py
```

## Unit 3, Particle filter
```Python
Particle_dumRobot.py
Particle_carRobot.py
```

# Search and Planning, Unit 4

For BFS, DFS, Uniform cost search, A* search, there is standard structure (pseudo code):
```
Explored = empty
frontier = container
frontier.push(root)

while frontier is not empty:
    Node=frontier.pop()
    if Node not in Explored:
        visit(Node)
        If Node is goal: 
            Success!
        Explored.add(Node)

        for child_node in child(Node):
            if child_node not in Explored:
            frontier.push(child_node)
Failed! 
```
The only difference is that BFS use Queue, DFS use Stack, Uniform cost and A* search use PriorityQueue as the container. 

```Python
Maze_BFS.py
Maze_Expand.py
Maze_BFS_printPath.py
Maze_Astar.py
```

```python
DynamicProgramming_value.py
DynamicProgramming_policy.py
DynamicProgramming_policy_method2.py
DynamicProgramming_stochastic.py
```

```python
Car_leftTurn_DP.py
Car_leftTurn_Astar.py
```


# PID Control, Unit 5
```python
Path_smoothing.py
Path_cyclicSmoothing.py
Path_fixedSmoothing.py
```

```python
PID_control.py
PID_twiddle_parameter.py
PID_Racetrack.py
```

# SLAM, Unit 6
```python
RoboticCar.py
```

```pythons
simple_SLAM.py
Robot_SLAM.py
Online_SLAM.py
```

# Final Project, Chase the escaping robot
Not done yet...