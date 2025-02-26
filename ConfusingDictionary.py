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

Visual Analogy
Think of the dictionary as a table of fruits and their prices:

Fruit	Price
Apple	10
Banana	20
Cherry	15
When we say max(mp, key=mp.get), it’s like asking:

"Which fruit has the highest price?"
The function goes through each fruit, checks its price, and tells us 'banana'.

# Confusing Sorted 
###def lexico_compare(str1, str2):
    min_length = min(len(str1), len(str2))
    for i in range(min_length):
        if str1[i] < str2[i]:
            return -1
        elif str1[i] > str2[i]:
            return 1
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    return 0

def lexico_sort(strings):
    return sorted(strings, key=functools.cmp_to_key(###lexico_compare))

# Example usage
import functools

strings = ["amruthan", "amruthana", "amurusha", "amrut", "amruta"]
sorted_strings = lexico_sort(strings)
print("Lexicographically sorted:", sorted_strings)

