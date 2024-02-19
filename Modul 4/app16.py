def check_pasward():
    requires_chars = ['!', '@', '%']
    passward = input('introduceti o parola: ')
    print(passward)
    if len(passward) < 7:
        print("parola cu lungime gresita")
        check_pasward()
    else:
        for character in requires_chars:
            if character in passward:
                break

        else:
            print("parola trebuie sa contina : ! @ %")
            check_pasward()

check_pasward()
