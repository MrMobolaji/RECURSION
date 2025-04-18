
def generate_permutations(arr):
    """
    Generates all permutations of the input list using recursion.
    
    Parameters:
        arr (list): A list of elements to permute.
        
    Returns:
        list of lists: All possible permutations.
    """
    if len(arr) <= 1:
        return [arr]
    
    perms = []
    for i in range(len(arr)):
        # Remove the element at index i
        current = arr[i]
        remaining = arr[:i] + arr[i+1:]
        
        # Recursively generate permutations of the remaining list
        for p in generate_permutations(remaining):
            perms.append([current] + p)
    
    return perms

# Example usage
if __name__ == "__main__":
    items = [1, 2, 3]
    all_perms = generate_permutations(items)
    print("All permutations of", items, ":")
    for p in all_perms:
        print(p)
