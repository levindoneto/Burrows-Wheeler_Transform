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

'''
Return a parallel list of B-ranks. It Also returns a map from character to the
number of times it appears.
@Parameter: String: Last BWM column
@Return: Lists: ranks, Dict: map
'''
def rankBwt(lastColumn):
    tots = dict()
    ranks = []
    for col in lastColumn:
        if not(col in tots):
            tots[col] = 0
        ranks.append(tots[col])
        tots[col] = tots[col] + 1
    return ranks, tots

'''
Return map from character to the range of rows prefixed by the character.
@Parameter: Dict: tots
@Return: Dict: First column with ranks
'''
def firstColumn(tots):
    ''' Return map from character to the range of rows prefixed by
        the character. '''
    firstC = {}
    totc = 0
    for c, counter in sorted(tots.items()):
        firstC[c] = (totc, totc + counter)
        totc += counter
    return firstC
