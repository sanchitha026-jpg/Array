

scores = []

n = int(input("Enter number of scores: "))

for i in range(n):
    score = float(input("Enter score: "))
    scores.append(score)

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("\nScores:", scores)
print("Sum of scores:", total)
print("Average of scores:", average)
print("Maximum score:", maximum)
print("Minimum score:", minimum)
