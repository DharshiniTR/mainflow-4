# ---- User Input ----
arr = list(map(int, input("Enter array elements: ").split()))
SSS = int(input("Enter target sum: "))

start = 0
curr_sum = 0
result = -1

for end in range(len(arr)):
    curr_sum += arr[end]   # expand window

    # shrink window if sum > SSS
    while curr_sum > SSS and start <= end:
        curr_sum -= arr[start]
        start += 1

    # check if found
    if curr_sum == SSS:
        result = (start, end)
        break

print("Result:", result)
