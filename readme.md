Using Random 8 Characters:
--------------------------

In this approach we generate a random 8 characters using random package using python. 
with this we will be able to generate 62**8 possibilities. 

Our charset includes small letters (a-z), big letters (A-Z) and 0-9 
To check the duplication is there we need to have a db aswell with replicas for read. 


Disadvantages:

1. Possibility of duplication is high when we move towards higher numbers. (run test.py file to see). 
2. high traffic will be occuring in the db side due to duplication.


Using Twitter Snowflake and Base62 Convertion:
----------------------------------------------

In this approach we generate twitter snowflake id and coverting to base62 representation ([a-zA-Z0-9]).

Disadvantages:

1. It has a length of 10 chars. 

For usage consideration:
1000 request in one second for 20 yrs

1000 * 365 * 24 * 60 * 60 * 20 = 630720000000

One insertion takes 10bytes, 630720000000 * 10 = 6307200000000 bytes
so for 20yrs it takes - 5.736364983 TB 