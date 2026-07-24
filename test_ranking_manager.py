from ranking_manager import RankingManager

manager = RankingManager()

manager.add_score("quality", "Investor", 95)
manager.add_score("quality", "Atlas Copco", 97)
manager.add_score("quality", "Volvo", 88)

manager.add_score("value", "Volvo", 94)
manager.add_score("value", "Investor", 86)

print("Rankings:")
print(manager.names())

print()

print("QUALITY")

for company in manager.get("quality").top():
    print(company)

print()

print("VALUE")

for company in manager.get("value").top():
    print(company)