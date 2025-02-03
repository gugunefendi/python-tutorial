def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I am a teapot"
        case _: # default case, if no case match, non of the branches is executed
            return "Something is wrong with the internet"
        
error_status = http_error(409)
print(error_status)

# combine case
def check_username(username):
    match username:
        case "Adi" | "Budi" | "Cici":
            return "Username has 'i'"
        case "Nada" | "Wanda":
            return "Username has 'a'"
        case _:
            return "Username has 'e' or 'o'"
        
username = check_username("Nada")
print(username)

# point is an (x, y) tuple
def match_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

match_point((0, 0))  # Output: Origin
match_point((0, 5))  # Output: Y=5
match_point((3, 0))  # Output: X=3
match_point((3, 4))  # Output: X=3, Y=4