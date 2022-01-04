# Tutorial on HashMap 

We write programs to solve real world problems. Data Structures help us in representing and efficiently manipulating the data associated with these problems. 


# The problem Scenario

In a class students, store heights for each student. 

The problem itself is very simple. We have the data of heights of each student. We want to store it so that next time someone asks for height of a student, we can easily return the value. But how can we store these heights? 


Obviously we can use a database and store these values. But, let's say we don't want to do that for now. We want to use a data structure to store theses values as part of our program. For the sake of simplicity, our problem is limited to storing heights of students. But you can certainly imagine scenrarios where you have to store such key-value pairs and later on when someone gives you a key , you  can efficiently return the corresponding value. 


The class diagram of HashMap would look something like this.


```
class HashMap:
    def __init__(self):
        self.num_entries = 0
    
    def put(self,key,value):
        pass 
    
    def get(self,key):
        pass 
    
    def size(self):
        return self.num_entries
```

## Array 

Can we use arrays to store key-value pairs? 

We can certainly use one array to store the names of the students and use another array to store their corresponding heights at the corresponding indices. 

What will be the time complexity in this scenario?

To obtain height of a student, say Potter, Harry, we will have to traverse the entire array and check if the value at a particular index matches Potter, Harry. Once we find the index in which this value is stored, we can use this index to obtain the height from the second array.

Thus, because of this traveral, complexity for get() operation becomes  𝑂(𝑛) . Even if we maintain a sorted array, the operation will not take less than  𝑂(𝑙𝑜𝑔(𝑛))  complexity.

What happens if a student leaves a class? We will have to delete the entry corresponding to the student from both the arrays.

This would require another traversal to find the index. And then we will have to shift our entire array to fill this gap. Again, the time complexity of operation becomes  𝑂(𝑛)


## Linked List
Is it possible to use linked lists for this problem?

We can certainly modify our LinkedListNode to have two different value attributes - one for name of the student and the other for height.

But we again face the same problem. In the worst case, we will have to traverse the entire linked list to find the height of a particular student. Once again, the cost of operation becomes 𝑂(𝑛).

## Stacks and Queues
Stacks and Queues are LIFO and FIFO data structures respectively. Can you think why they too do not make a good choice for storing key-value pairs?


Can we do better? Can you think of any data structure that allows for fast get() operation?

Let us circle back to arrays.

When we obtain the element present at a particular index using something like arr[3], the operation takes constant i.e. O(1) time.

For review - Does this constant time operation require further explanation?

If we think about array indices as keys and the element present at those indices as values, we can fairly conclude that at least for non-zero integer keys, we can use arrays.

However, like our current problem statement, we may not always have integer keys.

If only we had a function that could give us arrays indices for any key value that we gave it!

# Hash Functions

Simply put, hash functions are these really incredible magic functions which can map data of any size of a fixed data. This fixed sized data is often called hash code or hash digest.



```
def hash_function(string):
    pass
```

For a given string, say abcd, a very simple hash function can be sum of corresponding ASCII values.

Note: you can use ord(character) to determine ASCII value of a particular character e.g. ord('a') will return 97
```
def hash_function(string):
    hash_code = 0
    for character in string:
        hash_code += ord(character)
    return hash_code

    
hash_code_1 = hash_function("abcd")
print(hash_code_1)

```
Looks like our hash function is working fine. But is this really a good hash function?

For starters, it will return the same value for abcd and bcda. Do we want that? We can create 24 different permutations for the string abcd and each will have the same value. We cannot put 24 values to one index.

Obviously, this makes it clear that our hash function must return unique values for unique objects.

When two different inputs produce the same output, then we have something called a collision. An ideal hash function must be immune from producing collisions.

Let's think something else.

Can product help? We will again run in the same problem.

The honest answer is that we have differernt hash functions for different types of keys. The hash function for integers will be different from the hash function for strings, which again, will be different for some object of a class that you created.

However, let's try to continue with our problem and try to come up with a hash function for strings.

# Hash Function for Strings
For a string, say abcde, a very effective function is treating this as number of prime number base p. Let's elaborate this statement.

For a number, say 578, we can represent this number in base 10 number system as
5∗10^2+7∗10^1+8∗10^0
Similarly, we can treat abcde in base p as
𝑎∗𝑝4+𝑏∗𝑝3+𝑐∗𝑝2+𝑑∗𝑝1+𝑒∗𝑝0
Here, we replace each character with its corresponding ASCII value.

A lot of research goes into figuring out good hash functions and this hash function is one of the most popular functions used for strings. We use prime numbers because the provide a good distribution. The most common prime numbers used for this function are 31 and 37.

[Example](./map.py)

# Compress Function 


We now have good hash function which will return unique values for unique string. But let's look at the values. These are huge. We cannot create such large arrays. So we use another function -  compress function to compress these 
values so as to create array of reasonable sizes. 

A very simple, good and effective compression function can be mod len(array). The module operator % returns the remainder of one number when didved by other.

So, if we have an array of size 10, we can be sture that modulo of the number with 10 will be less than 10, allowing to fit into our bucket array. You can visualize the bucket array again as the shown in the figure below in which the bucket_index is generated by the stirng key. 


# Collision Handling 

As discussed earlier, when two different inputs produce the same output, then we have a collision. Our implementation of get_hash_code() function is satisfactory. However, because we are using compression function, we are prone to collisions. Remember, that a key will always be unique. But the bucket_index generated by two different keys can be the same.

Consider the following scenario - We have a bucket array of length 10 and we get two different hash codes for two different inputs, say 355, and 1095. Even though the hash codes are different in this case, the bucket index will be same because of the way we have implemented our compression function. Such scenarios where multiple entries want to go to the same bucket are very common. So, we introduce some logic to handle collisions


There are two popular ways in which we handle collisions.

1. Separate chaining - Separate chaining is a clever technique where we use the same bucket to store multiple objects. THe bucket in this case will store a linked list of key-value pairs.

2. Open Addressing - In open Addressing, we do the following:

    * If, after the bucket index, the bucket is empty, we store the object in that particular bucket.
    * If the bucket is not empty, we find an alternate bucket index by using another function which modifies the current hash code to a give code. This process of finding an alternate bucket index is called probing. A few probing techniques are - linear probing, quadratic probing, or double hashing. 


Separate chaining is a siple and effective technique to handle collisions and that is what we discuss here. Let us visualize the new bucket array one more time. 


