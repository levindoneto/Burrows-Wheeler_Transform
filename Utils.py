'''
Return list of rotations of inputS string
@Parameter: String: inputS
@Return: List: All rotations given the string input
'''
def rotations(inputS):
    rotation = inputS * 2
    return [rotation[i:i+len(inputS)] for i in range(0, len(inputS))]
