Stark= ["Eddard", "Tony", "Ayra", "Bryan"]

for d in range(len(Stark)):
    print(d + 2, Stark[d])

students = {"Godwin": "Abia",
            "Chima": "Anambra",
            "Golden": "Imo",
            "Maria": "Benue"}

for student in students:
    print(student, students[student], sep=", ")


royals = [
    {"name": "George", "house": "Pendragon", "sygil": "Dragon", "estate": "Camelot"},
    {"name": "Lancelot", "house": "Arvane", "sygil": "Swan", "estate": "Dicathen"},
    {"name": "Aegon", "house": "Targaryean", "sygil": "Hydra", "estate": "Dragon"},
    {"name": "Jamie", "house": "Lannister", "sygil": "Lion", "estate": "Casterly Rock"}

]
for royal in royals:
    print(royal ["name"], royal ["sygil"],sep=", ")


def main():
    print_alpha(4)


def print_alpha(height):
    for _alpha in range(height):
        print("#"* height)

main()

def major():
    print_beta(4)

def print_beta(width):
    print("?" * width)

major()