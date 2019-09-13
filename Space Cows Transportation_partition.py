# From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cowWeightDict = {}

    with open(filename, 'r') as filetext:
        for line in filetext:
            line = line.strip('\n')
            cowName, cowWeight = line.split(',')
            cowWeightDict[cowName] = int(cowWeight)
    return cowWeightDict

cowWeightDict = load_cows('ps1_cow_data.txt')

a= get_partitions(cowWeightDict.keys())
for i in a:
    print(i)
