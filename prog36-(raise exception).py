# raise exception

def voter(age):
    if age < 18:
        raise ValueError("Not eligible.")
    return "You are eligible."

try:
    print(voter(17))

except ValueError as error:
    print(error)
