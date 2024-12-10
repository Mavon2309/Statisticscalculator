def calculate_sample_statistics():
    """
    Calculate the sample variance and sample standard deviation for user-provided data.
    """
    # Ask the user to input a list of numbers
    try:
        data = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
        return

    if len(data) < 2:
        print("At least two data points are required to calculate sample statistics.")
        return

    # Calculate the mean of the data
    mean = sum(data) / len(data)

    # Initialize the sum of squared deviations
    sum_squared_deviations = 0

    # Calculate the sum of squared deviations from the mean
    for x in data:
        sum_squared_deviations += (x - mean) ** 2

    # Calculate the sample variance
    sample_variance = sum_squared_deviations / (len(data) - 1)

    # Calculate the sample standard deviation
    sample_deviation = sample_variance ** 0.5

    # Print the results
    print("Mean:", mean)
    print("Sample Variance:", sample_variance)
    print("Sample Standard Deviation:", sample_deviation)


# Example usage
if __name__ == "__main__":
    calculate_sample_statistics()
