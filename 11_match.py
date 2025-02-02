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
    