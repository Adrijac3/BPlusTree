## B+ TREE IMPLEMENTATION-


### About the assignment-
In this assignment the B+ tree data structure has been implemented from scratch. Here, we have 3 classes, namely bPlusTree, nonLeafNode and LeafNode. The leafNode inherits from nonLeafNode with an extra atribute acting as a block pointer for the right sibling. The nonLeafNode doesn't store record pointers while only the leaf nodes store them.
The implementation has been done using OOPS concepts and below attached is the class diagram for the same:
#### Class diagram-
![ds3](https://user-images.githubusercontent.com/30933610/108587654-ea5b7a00-737a-11eb-9b54-a1fb6b453362.jpg)
### Features implemented-
* Insert values- `INSERT X`
* Find values `FIND X`
* Count values `COUNT X`
* Range query `RANGE X Y`
* Error handling for invalid queries
### Constraints-
* -10^9 <= X <= 10^9, -10^9 <= Y <= 10^9
* The number of queries will be less than 10^6.
#### Dependency to run the code
* Machine should be able to run .py source file

#### How to execute the program-
* Make an input file containing queries with syntax mentioned above.
* Open a terminal with root of the application folder as the present working directory
* run the driver file by passing inputfile name as command line argument: `python3 drive.py <queryFileName>`

### Output-
* The result of FIND, COUNT and RANGE will be displayed in terminal as well as stored in an output file named as `output1.txt`

### Deliverables-
* Driver code in `drive.py`
* B+ Tree class handling insert, count, find and range in `bPlusTree.py`
* Two classes nonLeafNode and LeafNode in `node.py`
#### Language used-
Python

