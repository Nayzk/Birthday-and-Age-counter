# Birthday-and-Age-counter

This Python script calculates the number of days remaining until the next birthday and the current age of a person based on their birthdate. It uses the `datetime` module to handle date manipulations and calculations.

## Features

- **Days Until Next Birthday**: Calculates the number of days left until the user's next birthday.
- **Current Age**: Calculates the user's current age in years.

## Requirements

- Python 3.x

## How to Use

1. **Clone the Repository**: Clone this repository to your local machine using:

   ```
   bash
   Copy code
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to where the script is located:

   ```
   bash
   Copy code
   cd <repository-directory>
   ```

3. **Run the Script**: Execute the script using Python:

   ```
   bash
   Copy code
   python birthday_calculator.py
   ```

4. **Enter Your Birthdate**: When prompted, enter your day, month, and year of birth. For example:

   ```
   yamlCopy codeEnter your day of birth: 15
   Enter your month of birth: 6
   Enter your year of birth: 1990
   ```

5. **View the Results**: The script will display the number of days until your next birthday and your current age.

## Example Output

```
yamlCopy codeEnter your day of birth: 15
Enter your month of birth: 6
Enter your year of birth: 1990
Days until your next birthday: 30
Your age: 33
```

## Code Explanation

### days_until_birthday(birthdate)

This function calculates the number of days until the next birthday.

- **Parameters**: `birthdate` (a `date` object representing the user's birthdate)
- **Returns**: An integer representing the number of days until the next birthday

### calculate_age(birthdate)

This function calculates the user's current age.

- **Parameters**: `birthdate` (a `date` object representing the user's birthdate)
- **Returns**: An integer representing the user's current age

### Input and Output

- The script prompts the user to input their birthdate (day, month, and year).
- It then calculates and prints the number of days until the user's next birthday and their current age.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

If you have suggestions for improvements or find bugs, feel free to open an issue or submit a pull request.