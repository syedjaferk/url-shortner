In this approach we generate a random 8 characters using random package using python. 
with this we will be able to generate 62**8 possibilities. 

Our charset includes small letters (a-z), big letters (A-Z) and 0-9 
To check the duplication is there we need to have a db aswell with replicas for read. 


Disadvantages:

1. Possibility of duplication is high when we move towards higher numbers. (run test.py file to see). 
2. high traffic will be occuring in the db side due to duplication. 
3. 