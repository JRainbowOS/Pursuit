# Pursuit
Modelling generic pursuit problems.

## Set up
### 1. Clone (or Fork) Repo locally
### 2. pip install numpy into your environment
### 3. run 'pip install -e .' from inside the root directory

## Overview
Game is an abstract object for modelling behaviour a two-player pursuit. Chase is an example where one object chases the other. 
Pursuer is an abstract object for chasing an abstract Pursued. 
Cat and Mouse are examples of Pursuer and Pursued objects, respectively. Currently, the Mouse blindly walks in circles whilst the cat tries to catch it. There are options to make either of them accelerate or start from different places. 

Run chase.py to see an animation of the first 200 seconds of Cat and Mouse chase. 

## TODO:
### 1. Write Tests
### 2. Modify Pursued behaviour to avoid Pursuer
### 3. Invent other animals (such as random walk mouse)
