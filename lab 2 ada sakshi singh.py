

1 # Merge Sort using Divide and Conquer

def merge(arr, left, mid, right):
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)


# Input
arr = list(map(int, input("Enter numbers: ").split()))

merge_sort(arr, 0, len(arr)-1)

print("Sorted array:", arr)








2  # Activity Selection using Greedy Algorithm

def activity_selection(start, finish):
    n = len(start)
    activities = list(zip(start, finish))
    
    # Sort by finish time
    activities.sort(key=lambda x: x[1])

    selected = [activities[0]]

    last_finish = activities[0][1]

    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]

    return selected


# Input
n = int(input("Enter number of activities: "))

start = list(map(int, input("Enter start times: ").split()))
finish = list(map(int, input("Enter finish times: ").split()))

result = activity_selection(start, finish)

print("Selected activities (start, finish):")
for act in result:
    print(act)









3 # 0/1 Knapsack using Dynamic Programming

def knapsack(W, wt, val, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]


# Input
n = int(input("Enter number of items: "))

val = list(map(int, input("Enter values: ").split()))
wt = list(map(int, input("Enter weights: ").split()))

W = int(input("Enter capacity: "))

print("Maximum Profit:", knapsack(W, wt, val, n))