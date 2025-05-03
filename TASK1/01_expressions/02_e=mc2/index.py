C = 299_792_458  

def main():
    mass = float(input("Enter kilos of mass: "))

    energy = mass * (C ** 2)

    print("\ne = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s\n")

    print(f"{energy} joules of energy!")

if __name__ == '__main__':
    main()