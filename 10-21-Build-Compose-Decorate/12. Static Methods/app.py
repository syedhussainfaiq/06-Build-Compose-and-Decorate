class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
      return (c * 9/5 ) + 32
    

# Example usage
if __name__ == "__main__":
   celsius = 25
   fahrenhit = TemperatureConverter.celsius_to_fahrenheit(celsius)
   print(f"{celsius} C is equal to {fahrenhit} F")
        