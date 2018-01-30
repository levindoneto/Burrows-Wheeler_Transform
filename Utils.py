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
