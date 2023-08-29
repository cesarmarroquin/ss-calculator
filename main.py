from math import gcd


class SustainabilityScoreCalculator:
    def __init__(self):
        pass

    @staticmethod
    def calculate(driver: str, destination: str):
        """
        This method will take a driver's name and the destination address, and will calculate the sustainability score
        for the given combination.
        :param driver: The driver's name
        :param destination: The destination address
        :return:
        """
        # Calculate number of vowels and consonants
        driver = driver.lower()
        vowels = 'aeiou'
        num_vowels = 0
        for char in driver:
            if char in vowels:
                num_vowels += 1
        num_consonants = len(driver) - num_vowels

        # Calculate SS based on even or odd
        if len(destination) % 2 == 0:
            ss = num_vowels * 1.5
        else:
            ss = num_consonants * 1

        # Update SS if common factors found besides 1
        if gcd(len(destination), len(driver)) > 1:
            ss *= 1.5
        return ss


def read_file(file_path: str):
    """
    Helper function which is used by the main program to read the destination and driver files.
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def main():
    """
    The main executable program, which will calculate the total SS score from a list of destinations and drivers.
    :return:
    """
    # Initialize data and variables
    destination_file = input("Enter the path to the shipment destinations file: ")
    driver_file = input("Enter the path to the drivers file: ")
    destinations = read_file(destination_file)
    drivers = read_file(driver_file)
    total_ss = 0
    driver_matches = {}

    # Assign shipment destinations to drivers
    for destination in destinations:
        best_match = None
        best_ss = 0
        for driver in drivers:
            ss = SustainabilityScoreCalculator.calculate(driver, destination)
            if ss > best_ss:
                best_match = driver
                best_ss = ss
        total_ss += best_ss
        driver_matches[destination] = best_match
        drivers.remove(best_match)

    # Print final shipment/driver combinations and total SS
    for destination, driver in driver_matches.items():
        print(f"Destination: {destination}, Driver: {driver}")
    print(f"Total Sustainability Score: {total_ss}")


if __name__ == "__main__":
    main()
