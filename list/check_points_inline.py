'''
Coordinates is an list(list())) eg [[1,2],[2,3]]
'''

def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if((coordinates[1][0] - coordinates[0][0])==0):
            compare = coordinates[0][0]
            for coordinate in coordinates:
                if coordinate[0] != compare:
                    return False
        if (coordinates[1][1] - coordinates[0][1]) ==0 :
            compare = coordinates[0][1]
            for coordinate in coordinates:
                if coordinate[1] != compare:
                    return False
        slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        constant = coordinates[0][1] - slope*coordinates[0][0]
        
        for coordinate in coordinates:
            if coordinate[1] != slope*coordinate[0] + constant:
                return False
        
        return True

