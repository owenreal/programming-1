colors = ["red", "green", "blue"]
print(colors)
print(colors[1])

fruits = ["apple", "banana", "orange", "kiwi", "mango"]

for item in fruits:
	print(item)
print()

for index in range(len(fruits)):
	print(fruits[index])
print()

# lastfruit = fruits[len(fruits)-1]
lastfruit = fruits[-1]
print(lastfruit)
input()