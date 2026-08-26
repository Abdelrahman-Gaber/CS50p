def main():
    mass = int(input("Enter mass in Kg.: "))
    print(f"{energy(mass):,}")

def energy(mass):
    """Calculate the energy equivalent of a given mass using E=mc^2."""
    c = 300000000   # Speed of light in meters per second
    return mass * c ** 2

main()