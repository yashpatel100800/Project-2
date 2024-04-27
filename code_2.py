def longest_string_chain(strings):
    # Sort strings by length
    strings.sort(key=len)
    
    # Initialize dictionaries to store chain length and predecessors
    chain_len = {}
    pred = {}

    # Initialize max_chain_length and max_chain
    max_chain_len = 0
    max_chain_end = None

    # Iterate through each string
    for s in strings:
        # Initialize chain length for current string
        chain_len[s] = 1
        pred[s] = None
        
        # Try removing each character and check if resulting string is in the input list
        for i in range(len(s)):
            prev = s[:i] + s[i+1:]
            if prev in chain_len and chain_len[prev] + 1 > chain_len[s]:
                chain_len[s] = chain_len[prev] + 1
                pred[s] = prev
                
        # Update max_chain_length if needed
        if chain_len[s] > max_chain_len:
            max_chain_len = chain_len[s]
            max_chain_end = s
    
    # Reconstruct longest string chain
    longest_chain = []
    while max_chain_end:
        longest_chain.append(max_chain_end)
        max_chain_end = pred[max_chain_end]
    
    return longest_chain[::-1] if max_chain_len > 1 else []

# Test the function
strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
print(longest_string_chain(strings))  # Output: ["abcdef", "abcde", "abde", "ade", "ae"]
