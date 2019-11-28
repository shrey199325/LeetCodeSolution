"""
There is a row of seats. Assume that it contains N seats adjacent to each other. There is a group of 
people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.
An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')
Now your target is to make the whole group sit together i.e. next to each other, without having any 
vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.
Return minimum value % MOD where MOD = 10000003

Example
Here is the row having 15 seats represented by the String (0, 1, 2, 3, ......... , 14) -
              . . . . x . . x x . . . x . .

Now to make them sit together one of approaches is -
                  . . . . . . x x x x . . . . .

Following are the steps to achieve this -
1 - Move the person sitting at 4th index to 6th index -
    Number of jumps by him =   (6 - 4) = 2
2 - Bring the person sitting at 12th index to 9th index -
    Number of jumps by him = (12 - 9) = 3
So now the total number of jumps made =
    ( 2 + 3 ) % MOD =
    5 which is the minimum possible jumps to make them seat together.
There are also other ways to make them sit together but the number of jumps will exceed 5 and that 
will not be minimum.
For example bring them all towards the starting of the row i.e. start placing them from index 0.
In that case the total number of jumps will be
    ( 4 + 6 + 6 + 9 )%MOD
    = 25 which is very costly and not an optimized way to do this movement
"""


from random import choice


class Solution:
    def min_jumps(self, arr):
        median = self.median(arr)
        pass

    def median(self, arr):
        """
        Using the Median of median algorithm, finds the median in linear
        time complexity -> O(n)
        """
        pivot_fn = choice
        if len(arr) % 2 != 0:
            self.quickselect(arr, )

    def nlogn_median(self, arr):
        """
        This method first sorts the array and then find the middle element.
        Time complexity of this method is O(n*logn)
        """
        arr = sorted(arr)
        median = 0
        if len(arr) % 2 != 0:
            median = arr[len(arr)//2]
        else:
            median = (arr[(len(arr)//2)-1] + arr[(len(arr)//2)])/2
        return median