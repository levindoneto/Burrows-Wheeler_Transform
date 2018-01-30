'''
Return list of rotations of inputS string
@Parameter: String: inputS
@Return: List: All rotations given the string input
'''
def rotations(inputS):
    rotation = inputS * 2
    return [rotation[i:i+len(inputS)] for i in range(0, len(inputS))]

'''
Return sorted list of inputS’s rotations in a lexicographical way
@Parameter: String: inputS
@Return: List: All rotations sorted given the string input
'''
def bwm(inputS):
    return sorted(rotations(inputS))

'''
Return sorted list of inputS’s rotations in a lexicographical way
@Parameter: List: BWM list
@Return: String: Formatted matrix of rotations
'''
def showRotations(bwmList):
    return '\n'.join(bwmList)

'''
Return the last column of the matrix of rotations
@Parameter: String: inputS
@Return: String: Last column
'''
def getLastColumn(inputS):
    # Given T, returns BWT(T) by way of the BWM
    return ''.join(map(lambda rot: rot[-1], bwm(inputS)))
