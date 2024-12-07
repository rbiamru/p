# Confusing Dictionary to be practiced (Very Counter-intuitive)
from typing import List
from collections import Counter
def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    # Using mp
    # Create a map or frequency table
    mp = Counter(v)
    #Retrieve value with Max value
    max_frequentValue = max(mp.values())
    min_frequentValue = min(mp.values())
    #Find the largest key with the max frequency
    # key_max_value = max(mp, key = mp.get) # max_frequentValue.Key()
    # key_min_value = min(mp, key = mp.get)

     # Find the smallest key with the max frequency
    key_max_value = min([key for key, freq in mp.items() if freq == max_frequentValue])
    
    # Find the smallest key with the min frequency
    key_min_value = min([key for key, freq in mp.items() if freq == min_frequentValue]) #Frequency === value (frequency means value)

    return [key_max_value, key_min_value]
