def bubble_sort(arr):
    n = len(arr)
    print("Initial array:", arr)

    for i in range(n - 1):
        swapped = False
        print(f"\n--- Round {i + 1} ---")

        for j in range(n - 1 - i):
            print(f"Compare: {arr[j]} and {arr[j + 1]}", end=" ")

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print("=> swap") 
            else:
                print("=> no swap") 

            print("Current array:", arr)

        if not swapped:
            print("No swaps in this round → array is sorted early") 
            break

    print("\nFinal sorted array:", arr)
    return arr