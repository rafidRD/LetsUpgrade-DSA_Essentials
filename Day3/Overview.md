# <center>Overview</center>

## Functions
    def fun(a):
      print('Hello coder', a)
      return

    fun("Rafid")

Output: Hello coder Rafid
<br>

    def fun(a, b):
      return a + b
    print(fun(100, 350))

Output: 450
<br><br>
## Methods & Data Members

*Adding class block it has become a method*

    class Test:
        def show(self):
            print("Method")
    ob = Test()
    ob.show() #Test.show(ob)

Output: Method

**Adding Data Member:**

    class Test:
      def __init__(self): #Constractor
        self.a = 10 
      
      def show(self):
        print("Method", self.a)
        
    ob = Test()
    ob.show()    #Test.show(ob)

    OUTPUT: Method 10
    ============================================================
    class TestX:
      def __init__(self, data):  #Constructor
        self.x = data
      def look(self):
        print("Method", self.x)

    ob = TestX(20)
    ob.look()    #TestX.look(ob)

    OUTPUT: Method 20
    ============================================================
    class Testing:
    def __init__(self, K): #constructor
        self.s = K
    def wow(self, y):
        print("Method", self.s, y)

    ob = Testing(27)
    ob.wow(73)        #Testing.wow(ob)

    OUTPUT: Method 27 73


## Netflix Movie List Backend
<br>

    class MovieNode:
        def __init__(self, movieName, relDate):
            self.movieName = movieName
            self.relDate = relDate
            self.next = None
            return
        
    class MovieList:
        def __init__(self):
            self.head = None
        def addMovie(self, movieName, relDate):
            new = MovieNode(movieName, relDate)
            if self.head == None:
                self.head = new
                return
            new.next = self.head
            self.head = new
            return
        def displayMovies(self):
            if self.head == None:
                print("No movies for you right now.")
                return
            temp = self.head
            
            while(temp != None):
                print(temp.movieName, temp.relDate, "->", end =" ")
                temp = temp.next
            print("None")
            return
                
    movie_list = MovieList()
    movie_list.addMovie("The Red Xone", '18 January 2002')
    movie_list.addMovie("Iron Man", '24 August 2008')
    movie_list.addMovie("Avengers", '24 November 2013')

    movie_list.displayMovies()

<br>

------------------------------------------------------------------
# <center>Provided Summary</center>

### TIMESTAMP for EACH TOPIC:  


[00:24](https://www.youtube.com/watch?v=e404YCilMH0&t=24s) - 04:22 - Introduction and day 2 recap 

[04:23](https://www.youtube.com/watch?v=e404YCilMH0&t=263s) - 08:46 - functions

[08:47](https://www.youtube.com/watch?v=e404YCilMH0&t=527s) - 13:29 - classes and methods

[13:30](https://www.youtube.com/watch?v=e404YCilMH0&t=810s) - 20:12 - __init__ (constructor)

[20:13](https://www.youtube.com/watch?v=e404YCilMH0&t=1213s) - 23:02 - Doubt Solving 

[23:03](https://www.youtube.com/watch?v=e404YCilMH0&t=1383s) - -25:30 -  Linked List  

[25:31](https://www.youtube.com/watch?v=e404YCilMH0&t=1531s) - 28:15 - MovieNode class definition

[28:16](https://www.youtube.com/watch?v=e404YCilMH0&t=1696s) - 34:28 - NetflixMovieList class definition

[34:29](https://www.youtube.com/watch?v=e404YCilMH0&t=2069s) - 39:02 - Add Node at the beginning of the list 

[39:03](https://www.youtube.com/watch?v=e404YCilMH0&t=2343s) - 44:41 - Doubt Solving

[44:42](https://www.youtube.com/watch?v=e404YCilMH0&t=2682s) - 52:07 - Display method

[52:08](https://www.youtube.com/watch?v=e404YCilMH0&t=3128s) - 56:58 - Execution of the Movie linked list program

[56:59](https://www.youtube.com/watch?v=e404YCilMH0&t=3419s) - 59:10 - Assignment 

[59:11](https://www.youtube.com/watch?v=e404YCilMH0&t=3551s) - 1:00:45 - Conclusion

----------------------------------------------------------------------------------------

### **Function**

   * A function in Python is an aggregation of related statements designed to perform a computational, logical, or evaluative task.
   * A function is defined by using the def keyword.
<br>
    def my_function():
      print("Hello LetsUpgrader’s")

### **Classes and Methods**

   * A class is like a blueprint for creating objects.
   * A class has attributes as well as methods for objects.
   * A class is defined by the keyword class.
   * An object is created using the constructor of the class.

###  **\_\_init\_\_() function**

   * It is a built-in function present in every class and it gets called when a class is being initiated.
   * Various initial properties of the object can be defined by the use of this function.
<br>

    class Person:
      def __init__(self, name):
        self.name = name
      def myfunc(self):
        print("Hello my name is " + self.name)
    p1 = Person("Letsupgrade")
    p1.myfunc()


### **Linked list**


  * Collection of nodes in which each node stores a data and has a link or reference to the next node.

*Example of a node:-*

    class Node:
        def __init__(self, dataval=None):
            self.dataval = dataval
            self.nextval = None

------------------------------------------------------------------