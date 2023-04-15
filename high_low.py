class High_Low:
    def __init__(self):
        pass

    def find_high_low(self, numbers):
        """
        This function takes a list of integers as input and returns the highest
        and lowest numbers in the list.
        """
        if not numbers:
            return None, None  # Return None for both high and low if the list is empty

        high = numbers[0]  # Initialize high and low with the first number in the list
        low = numbers[0]

        for num in numbers:
            if num > high:
                high = num  # Update high if num is greater
            elif num < low:
                low = num  # Update low if num is smaller

        return high, low


