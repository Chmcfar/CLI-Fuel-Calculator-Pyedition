def get_price_per_mile(current_gas_price: float, fuel_efficiency: float): 
    if fuel_efficiency == 0:
        return "fuel_efficiency cannot be 0"
    return current_gas_price / fuel_efficiency

if __name__ == "__main__":
    current_gas_price = 3 # Currency/Volume 
    fuel_efficiency = 20 # Volume/Distance
    print(f"For a gas price of ${current_gas_price:.2f} per gallon \nand a vehicle with a fuel efficiency of {fuel_efficiency} gallons per mile,\nevery mile driven will cost you ${get_price_per_mile(current_gas_price, fuel_efficiency):.2f}")
    trip_distance = 17
    if trip_distance != 0:
        price_of_trip = get_price_per_mile(current_gas_price, fuel_efficiency) * trip_distance
        print(f"A trip of {trip_distance}mi will cost ${price_of_trip:.2f} for fuel")
