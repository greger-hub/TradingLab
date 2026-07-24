from ranking import Ranking

ranking = Ranking()

ranking.add("Volvo", 88.5)
ranking.add("Investor", 94.0)
ranking.add("Atlas Copco", 96.5)
ranking.add("Lifco", 92.0)

print("=== TOP 4 ===")

for entry in ranking.top():
    print(entry)

print()

print("Investor:", ranking.rank("Investor"))
print("Volvo:", ranking.rank("Volvo"))
print("ABB:", ranking.rank("ABB"))