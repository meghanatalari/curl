import requests
import json

url = "https://michaelgathara.com/api/python-challenge"

response = requests.get(url)

challenges = response.json()
print(challenges)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    problems = response.json()

    # Solve and print each problem
    for problem in problems:
        problem_id = problem["id"]
        expression = problem["problem"]

        # Remove the question mark from the expression
        expression = expression.rstrip("?")

        try:
            # Evaluate the expression
            result = eval(expression)

            # Print the problem ID, expression, and its solution
            print(f"Problem ID: {problem_id}")
            print(f"Expression: {expression}")
            print(f"Solution: {result}")
            print()
        except SyntaxError:
            print(f"Invalid expression: {expression}")
        except Exception as e:
            print(f"An error occurred while solving the problem: {expression}")
            print(f"Error details: {str(e)}")
else:
    print(f"Error accessing the URL. Status Code: {response.status_code}")