file = open("6-1.in", "r")
# file = open("6-1.in.sample", "r")

nums = []
for line in file:
    nums = [int(x) for x in line.strip().split(" ")]

seen = set()
iterations = 0
key = ",".join(str(x) for x in nums)
while key not in seen:
    seen.add(key)
    next_index = nums.index(max(nums))
    blocks = nums[next_index]
    nums[next_index] = 0
    while blocks > 0:
        next_index = (next_index + 1) % len(nums)
        nums[next_index] += 1
        blocks -= 1
    key = ",".join(str(x) for x in nums)
    iterations += 1

print(iterations)

seen = set()
iterations = 0
key = ",".join(str(x) for x in nums)
while key not in seen:
    seen.add(key)
    next_index = nums.index(max(nums))
    blocks = nums[next_index]
    nums[next_index] = 0
    while blocks > 0:
        next_index = (next_index + 1) % len(nums)
        nums[next_index] += 1
        blocks -= 1
    key = ",".join(str(x) for x in nums)
    iterations += 1

print(iterations)
