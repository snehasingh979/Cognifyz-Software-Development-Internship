print("=" * 40)
print("🌡️ TEMPERATURE CONVERTER 🌡️")
print("=" * 40)

while True:
    print("\nChoose Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        celsius = float(input("Enter Temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")

    elif choice == "2":
        fahrenheit = float(input("Enter Temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius:.2f}°C")

    elif choice == "3":
        celsius = float(input("Enter Temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C = {kelvin:.2f} K")

    elif choice == "4":
        kelvin = float(input("Enter Temperature in Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin} K = {celsius:.2f}°C")

    elif choice == "5":
        print("\nThank you for using Temperature Converter!")
        break

    else:
        print("Invalid choice! Please try again.")
