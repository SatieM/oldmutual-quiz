import time

def bubble_sort(arr):
    n = len(arr)
    Pass = 0
    comparisons = 0
    swaps = 0
    print("\n Sorting Process:")
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps +=1
            Pass += 1
            print(f"Pass {Pass}: {arr}")
    return arr, comparisons,swaps

def get_user_input():
    try:
        nums = input("Enter numbers separated by spaces: ")
        return [int(num) for num in nums.strip().split()]
    except ValueError:
        print("Invalid input. Please enter only integers.")
        return get_user_input()

def main():
    print("===== BUBBLE SORT ALGORITHM ===== ")
    user_numbers = get_user_input()

    if len(user_numbers) < 2:
        print("You need at least two numbers to sort.")
        return

    # Copy the list for comparison
    bubble_input = user_numbers.copy()
    builtin_input = user_numbers.copy()

    # Bubble Sort with timing
    start = time.time()
    sorted_bubble, comparisons , swaps = bubble_sort(bubble_input)
    end = time.time()
    bubble_time = time.time() - start

# Built-in Sort
    start = time.time()
    builtin_input.sort()
    builtin_time = time.time() - start

    # Calculate speed comparison
    speed_ratio = bubble_time / builtin_time if builtin_time > 0 else float('inf')

    # Print Final Output
    print("\n Final sorted array:", sorted_bubble)
    print("\n Performance Analysis:")
    print(f"• Array size: {len(user_numbers)}")
    print(f"• Total comparisons: {comparisons}")
    print(f"• Total swaps: {swaps}")
    print(f"• Time taken (bubble sort): {bubble_time:.4f} seconds")

    print("\nComparison with Python's sort():")
    print(f"• Built-in sort time: {builtin_time:.4f} seconds")
    if speed_ratio == float('inf'):
        print("• Built-in sort was too fast to compare.")
    else:
        print(f"• Bubble sort is {speed_ratio:.0f}x slower than built-in sort")

if __name__ == "__main__":
    main()
