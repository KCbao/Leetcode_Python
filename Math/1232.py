class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        first, sec = coordinates[0], coordinates[1]
        if first[0] == sec[0]:
            slope = first[0]
            flag = True
        else:
            slope = (sec[1]-first[1])/(sec[0]-first[0])
            flag = False
        for item in coordinates[2:]:
            if flag == True:
                if item[0] != slope:
                    return False       
            else:    
                if (item[0]-first[0] == 0):
                    return False
                elif slope != (item[1]-first[1])/(item[0]-first[0]) :
                    return False
                
        return True