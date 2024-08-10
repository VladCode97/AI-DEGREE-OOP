def magic_number() -> None:
    temp_magic: int = 12345679
    number_user: int = int(input('Inser number beetween 1 and 9: '))
    if number_user < 1 or number_user > 9:
           print("The number must be between 1 and 9.")
           return
    else:
        number_user*=9
        temp_magic*=number_user
        print(temp_magic)

magic_number()
