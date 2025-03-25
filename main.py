from functions import *

if __name__ == "__main__":    
    
    arr = [3, 1, 8, 2, 5, 7, 4, 6]
    min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
    print(f"Menor elemento: {min_val}, Maior elemento: {max_val}")