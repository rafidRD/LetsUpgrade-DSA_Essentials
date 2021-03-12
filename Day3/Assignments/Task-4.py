# Question #
# Perform Delete operation at the end to remove the oldest movie from the movies list

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
    def ByeOldMan(self):
        if self.head == None:
            return None
        if next == None: 
            self = None
            return None
        old_man = self.head 
        while(old_man.next.next): 
            old_man = old_man.next
        old_man.next = None
        return self

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
movie_list.addMovie("Avengers", '29 March 2013')
movie_list.addMovie("Hacker", '09 February 2015')
movie_list.addMovie("KGF", '17 June 2019')

# removes the last/old movie
movie_list.ByeOldMan()

# Displays All The Movies
movie_list.displayMovies()