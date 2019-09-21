class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0

        points = sorted(points, key=(lambda x: x[0]))

        # shoot_begin = points[0][0]
        shoot_end = points[0][1]

        shoot = 1
        for i in range(1, len(points)):
            # shoot_begin = points[i][0]
            if points[i][0] <= shoot_end:
                
                if points[i][1] < shoot_end:
                    shoot_end = points[i][1]
            else:
                shoot_end = points[i][1]
                shoot += 1
        return shoot



if __name__ == '__main__':
    input = [[10,16], [2,8], [1,6], [7,12]]
    sorted(input, key=(lambda x: x[0]))
    print(input)