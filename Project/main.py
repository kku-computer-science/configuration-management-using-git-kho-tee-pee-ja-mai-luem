from sorting.bubble_sort import bubble_sort
from sorting.quick_sort import quick_sort

def get_integer_list():
    """รับลิสต์ตัวเลขจำนวนเต็มจากผู้ใช้ พร้อมตรวจสอบความถูกต้อง"""
    while True:
        user_input = input("Enter integers separated by spaces (or X to cancel): ")

        if user_input.lower() == 'x':
            print("Process canceled.")
            return None

        parts = user_input.split()
        numbers = []

        valid = True
        for p in parts:
            if not p.lstrip('-').isdigit():
                print(f"Invalid input: '{p}' is not an integer. Try again.")
                valid = False
                break
            numbers.append(int(p))

        if valid:
            return numbers


def show_menu():
    print("\n=== Sorting Menu ===")
    print("1. Bubble Sort")
    print("2. Quick Sort")
    print("3. Exit")
    return input("Choose an option: ")


def main():
    print("=== Sorting Program ===")

    # Step 1: รับลิสต์ตัวเลข
    data = get_integer_list()
    if data is None:
        return  # ผู้ใช้ยกเลิก

    # Step 2: เข้าสู่เมนูเลือก algorithm
    while True:
        choice = show_menu()

        if choice == '1':
            print("\nRunning Bubble Sort...")
            result = bubble_sort(data.copy())
            print("Sorted result:", result)

        elif choice == '2':
            print("\nRunning Quick Sort...")
            result = quick_sort(data.copy())
            print("Sorted result:", result)

        elif choice == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
