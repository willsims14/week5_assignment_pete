
names = ["Eric", "Matt", "Mitch", "Jack"]
# names = ["Eric",]

def calculation(name: str):
    d = { 'name': name }
    discussion_grade = float(input("\nWhat was " + name + "'s discussion grade?\t"))
    d['grade'] = discussion_grade
    return d


highest_grade = 0
for name in names:
    info = calculation(name)
    if info['grade'] >= highest_grade:
        highest_grade = info['grade']
        highest_name = info['name']

print(f"{highest_name} got the highest score of {highest_grade}")
