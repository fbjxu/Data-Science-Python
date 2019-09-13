###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

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


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    wholeTrip = []
    #sort the cows by their weights
    sortedCows = cows
    sortedName = sorted(cows, key = cows.get, reverse = True) #this thing returns a list
    #iterate through all cows
    while len(sortedName) > 0:
        avail = limit
        singleTrip = []
        for cow in sortedName:
            if sortedCows[cow] <= avail:
                singleTrip.append(cow)
                avail -= sortedCows[cow]
        wholeTrip.append(singleTrip)
        for goneCow in singleTrip:
            if goneCow in sortedName:
                sortedName.remove(goneCow)
    return wholeTrip



# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    def isWholeTripLegal(perm, limit):
        """Assume perm is a list of lists: each individual element is a list of cow names signifying the cows
        transported in one ship
        Returns False if any list's weight exceed the givin limit
        Return True otherwise
        """
        for trip in perm:
            weight = 0
            for cow in trip:
                weight += cowWeightDict[cow]
                if weight > 10:
                    return False
        return True
    limit = 10

    result = {}  # dictionary {trip: number of trips}

    # iterate over all possible permutations of trips
    for tripPermutation in get_partitions(cowWeightDict.keys()):
        # firstly check if any single trip exceeds limit
        if isWholeTripLegal(tripPermutation, limit):
            result[len(tripPermutation)] = tripPermutation
    quickest = result.get(min(result.keys()))
    return quickest


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows('ps1_cow_data.txt')
    # time greedy_cow_transport
    greedy_start = time.time()
    greedy_result = greedy_cow_transport(cows,10)
    greedy_end=time.time()
    greedy_time = greedy_end - greedy_start

    # time brute force
    bf_start = time.time()
    bf_result = brute_force_cow_transport(cows, 10)
    bf_end = time.time()
    bf_time = bf_end - bf_start

    print('Time for Greedy:', greedy_time, 'Trip Length:',len(greedy_result), 'Trip Detail:', greedy_result, '\n')
    print('Time for Brute Force:', bf_time, 'Trip Length:', len(bf_result), 'Trip Detail:', bf_result, '\n')

import time
compare_cow_transport_algorithms()

