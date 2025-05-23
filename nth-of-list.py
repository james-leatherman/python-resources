

def returnLargest(integers: list, n: int):
    if n < 1 or n > len(integers):
        raise ValueError(f"{n} is not a position in the list")
    
    sorted_integers = sorted(integers, reverse=True)
    print(f"The integer at position #{n} is {sorted_integers[n - 1]}")

if __name__ == "__main__":
    nums = input("Enter list of integers: ")
    n = int(input("List the nth largest to find: "))

    nums = [int(x) for x in nums.split()]

    returnLargest(nums, n)