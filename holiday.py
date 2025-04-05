# Displays the total cost of the flight to a city.
def plane_cost(city_flight):
    """
     Calculates the cost of a flight to a given city.

     Args:
    city_flight: The destination city.

    Returns:
    The cost of the flight to the specified city
    Will return if the specified city has not be entered.
    """
    print(city_flight)
    if city_flight == "Nelspruit":
        return 1350
    elif city_flight == "Polokwane":
        return 1500
    elif city_flight == "Pretoria":
        return 1100
    elif city_flight == "Stellenbosch":
        return 2500
    else:
        print("Invalid selection")
        return


# Prompts the user to make a selection between the cities below
print("Make a selection between the cities below ")
city_flight = input("Nelspruit, Polokwane, Pretoria or Stellenbosch: ").capitalize()  
flight_cost = plane_cost(city_flight)


# Calculates the total cost of a hotel cost based on the number of nights.
def hotel_cost(num_nights):
    """
    Calculates the total cost for a hotel stay.

    Parameters:
    num_nights: The number of nights to stay at the hotel.

    Returns:
    The total cost of the nights stayed in hotel.
    """
    fare_per_rate = 2500
    hotel_per_fees = fare_per_rate * num_nights
    return hotel_per_fees


# Prompts user to enter the amount of nights stayed in the hotel
num_nights = int(input("The amount of nights stayed in the hotel: "))
nights_stayed = hotel_cost(num_nights)


# Calculates the final amount of a car rental based on the number days.
def car_rental(rental_days):
    """
        Calculates the total cost of renting a car.

    Parameters:
        rental_days: The number of days the car is rented for.

     Returns:
        The total cost of the car rental(rental_fees).
    """
    cost_day = 1750
    rental_fees = rental_days * cost_day
    return rental_fees


# Prompts user to enter the amount of days the car has been used
rental_days = int(input("The amount of days used to rent the car: "))
rent_rate = car_rental(rental_days)


# Calculates the final amount from the holiday day(flight, rental, hotel stay)
def holiday_cost(city_flight, num_nights, rental_days):
    """
    Calculates the total cost of the whole holiday

    Parameters:
        num_nights: The number of nights for the hotel stay.
        city_flight: The destination city for the flight.
        rental_days: The number of days for the car rental.

    Returns:
        The total cost of the holiday.
    """
    hotel_final = hotel_cost(num_nights)
    plane_final = plane_cost(city_flight)
    car_final = car_rental(rental_days)
    total_holiday_expense = hotel_final + plane_final + car_final
    return total_holiday_expense


# Prints the total amount of each holiday expenditure
total_holiday_cost = holiday_cost(city_flight, num_nights, rental_days)
print(f"The total amount of the flight R{flight_cost}")
print(f"the total amount nights stayed in hotel is R{nights_stayed}")
print(f"The total amount for car rental R{rent_rate}")

# Prints out the total expenditure of the holiday trip
print(f"The total expenditure of the whole trip is R{total_holiday_cost}")
