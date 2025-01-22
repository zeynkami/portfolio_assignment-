class EuclideanAlgorithm:
    """
    Class to encapsulate the Euclidean Algorithm for calculating the GCD and LCM.
    """

    @staticmethod
    def calculate_gcd(a, b):
        """
        Calculate the GCD of two numbers using the Euclidean Algorithm.
        :param a: First integer
        :param b: Second integer
        :return: GCD of a and b
        """
        while b != 0:
            remainder = a % b
            a = b
            b = remainder
        return a

    @staticmethod
    def calculate_lcm(a, b):
        """
        Calculate the LCM of two numbers using the relationship between GCD and LCM.
        :param a: First integer
        :param b: Second integer
        :return: LCM of a and b
        """
        gcd = EuclideanAlgorithm.calculate_gcd(a, b)
        return abs(a * b) // gcd


def main():
    """
    Main function to get user input, validate it, and calculate GCD and LCM.
    """
    try:
        # Prompting the user for input
        a = int(input("Enter the first positive integer: "))
        b = int(input("Enter the second positive integer: "))

        # Validate input
        if a <= 0 or b <= 0:
            print("Error: Both numbers must be positive integers.")
            return

        # Calculate GCD and LCM
        gcd = EuclideanAlgorithm.calculate_gcd(a, b)
        lcm = EuclideanAlgorithm.calculate_lcm(a, b)

        # Display results
        print(f"The GCD of {a} and {b} is: {gcd}")
        print(f"The LCM of {a} and {b} is: {lcm}")

    except ValueError:
        print("Error: Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()