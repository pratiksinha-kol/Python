def joules(mass):
    c = 300000000
    energy = mass * c**2
    return energy

def main():
    mass = int(input("Enter mass in kilograms: "))
    energy = joules(mass)
    # print(f"The energy equivalent of {mass} kg is {energy} joules.")
    print(energy)

main()