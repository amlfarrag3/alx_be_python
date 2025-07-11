# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
   temperature_converted_to_Celsius =(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
   return (temperature_converted_to_Celsius)

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    temperature_converted_to_Fahrenheit =(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return (temperature_converted_to_Fahrenheit)
def main():
    print("Temperature Conversion Tool")
    while True:
        try:
            temp = float(input("Enter the temperature to convert: "))
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        while unit not in ["C", "F"]:
            unit = input("Invalid unit. Please enter C for Celsius or F for Fahrenheit: ").strip().upper()

        if unit == "C":
            fahrenheit = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {fahrenheit}°F")
        elif unit == "F":
            celsius = convert_to_celsius(temp)
            print(f"{temp}°F is {celsius}°C")
            break

if __name__ == "__main__":
    main()
