round_count = 1 
def quick_sort(arr):
    global round_count
    if len(arr) <= 1:
        return arr
    if all(x == arr[0] for x in arr):
        print(f"\n=== Round {round_count} ===")
        print(f"All elements equal → {arr}, stop recursion.")
        return arr

    pivot = arr[-1]
    left = []
    right = []

    print(f"\n=== Round : {round_count} ===")
    print(f"Pivot selected: {pivot}")

    for i in arr[:-1] :
        if i <= pivot :
            left.append(i)
        else :
            right.append(i)
    round_count += 1
    print(f"Left partition: {left}")
    print(f"Right partition: {right}")

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    return sorted_left + [pivot] + sorted_right

input_numbers = list(map(int, input("Enter list of number: ").split()))

print(input_numbers)
print("Running Quick Sort Algorithm...")
result = quick_sort(input_numbers)
print("\nFinal Result:", result)
