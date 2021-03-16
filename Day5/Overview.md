# Provoded Summary


TIMESTAMP for EACH TOPIC:  

-----------

[00:10](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=10s) - 06:24 - Introduction and day 4 recap

[06:25](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=385s) - 13:04 - What is Greedy ATM?

[13:05](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=785s) - 16:57 - What is the greedy approach?

[16:58](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=1018s) - 33:17 - Implementation of greedy algorithm code 

[33:18](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=1998s) - 34:34 - Execution of Greedy ATM code

[34:35](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=2075s) - 37:10 - Doubt Solving

[37:11](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=2231s) - 44:57 - Drawback of the Greedy algorithm approach 

[44:58](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=2698s) - 48:01 - Doubt Solving

[48:02](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=2882s) - 52:04 - What is Array Rotation?

[52:05](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=3125s) - 54:26 - Time Complexity for k rotations

[54:27](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=3267s) - 1:01:32 - How to rotate array with O(n) time complexity?

[1:01:33](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=3693s) - 1:05:04 - Doubt Solving 

[1:05:05](https://www.youtube.com/watch?v=aFXzq1p_Rm8&t=3905s) - 1:10:34 - Conclusion

-------------
## Greedy Algorithm

* Greedy algorithms always make the choice that seems to be the best at that moment.
* This means that it makes a locally optimal choice in the hope that this choice will lead to a globally optimal solution.
* Generally, greedy algorithms do not provide globally optimized solutions.

Example:-

    If we are provided coins of Rs 1, 7, 10.
    Counting coins for value 18 will be absolutely optimum i.e 3coins (1+7+10=18).
    But for value 15, it may use more coins as the greedy approach will use 10 + 1 + 1 + 1 + 1 + 1, total 6 coins. Whereas the same problem could be solved by using only 3 coins (7 + 7 + 1)

![](https://t-images.imgix.net/https%3A%2F%2Flh4.googleusercontent.com%2Fa7TkePfvdHQXqZuGGgl-vd-nOBXp0C6b4TX_Qli80XFPhlYNtDxIZXDCiVlqpIEnwWUYDcfs-cxwArueuBUWGoQ4sg0PhSz8vFrGXeZU83NMxu7wZrTr7aQ2XCJcVtJXpTr7XCC5?width=1240&w=1240&auto=format%2Ccompress&ixlib=js-2.3.1&s=7526e180ab29244ca887046acf2db78a)

## Array Rotation

* The time complexity for the k times left rotation of an array of size n is k*n .
* To reduce this quadratic time complexity O(n^2) to linear time complexity O(n) we need to find out the effective no of rotations.
* Effective rotations, k=k%n.

### Code to print the array with k rotations:-

    li=[9,6,5,0,8,2]
    k=int(input(“Enter no of rotations : ”))
    k= k % len(li)
    print(li[k : ] + li[0 : k ])

![](https://t-images.imgix.net/https%3A%2F%2Flh4.googleusercontent.com%2F3DjKdgXCzGbAj-UE27xojVbIMcIHH5lcuJ50p9bW4cPqWCDYLaVMsLiy1Lol23dobuL-2g0D7e0d3LHEOcd4zkECNwVTnz_KnN_WqoCjMpREjYuw59O_RKIizcwBirKVh2OJpxwV?width=1240&w=1240&auto=format%2Ccompress&ixlib=js-2.3.1&s=d59b794aa52deef129eb8b79a5112ae5)

------------------

🚀  Materials for the day have been uploaded in the drive. 

[👩‍🏫 Classroom](https://letsupgrade.in/my-programs) 

(Make sure you have registered on our website for the course. If not registered yet, register yourself!!!. You can find the Course/classroom under the "My Program" section on the website.)

[📰 Day 5 Materials](https://drive.google.com/drive/folders/1JjcrtCL3FkwKovoUZFuwSbv6ScH11iyj?usp=sharing)

[Video](https://youtu.be/aFXzq1p_Rm8)