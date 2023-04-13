
import PasswordException
import PasswordValidator


def displayErrors(pw):

    print("Invalid Password")
    for e in pw.errors:
        print(f"{e.log['password']} Password must contain {e.log['min_required']} {e.log['error_type']}"
              f"but yours only contained {e.log['count']}")


    