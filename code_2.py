def longest_string_chain(strings):
    # Sort strings by length
    strings.sort(key=len)
    
    # Initialize dictionaries to store chain length and predecessors
    chain_length = {}
    predecessor = {}

    # Initialize max_chain_length and max_chain
    max_chain_length = 0
    max_chain_end = None

    # Iterate through each string
    for s in strings:
        # Initialize chain length for current string
        chain_length[s] = 1
        predecessor[s] = None
        
        # Try removing each character and check if resulting string is in the input list
        for i in range(len(s)):
            prev = s[:i] + s[i+1:]
            if prev in chain_length and chain_length[prev] + 1 > chain_length[s]:
                chain_length[s] = chain_length[prev] + 1
                predecessor[s] = prev
                
        # Update max_chain_length if needed
        if chain_length[s] > max_chain_length:
            max_chain_length = chain_length[s]
            max_chain_end = s
    
    # Reconstruct longest string chain
    longest_chain = []
    while max_chain_end:
        longest_chain.append(max_chain_end)
        max_chain_end = predecessor[max_chain_end]
    
    return longest_chain[::-1] if max_chain_length > 1 else []

# Test the function
strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
print(longest_string_chain(strings))  # Output: ["abcdef", "abcde", "abde", "ade", "ae"]
