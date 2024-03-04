import random;


def guess_number_computer(x):

    print("=======================");
    print("  Welcome to the Game!  ");
    print("=======================");

    print(f"Select a number between 1 and {x} in order for the computer to guess it ");

    inferior_limit = 1;
    superior_limit = x;

    answer = "";

    while answer != "c":
        if inferior_limit != superior_limit:
            prediction = random.randint(inferior_limit, superior_limit);
        else:
            prediction = inferior_limit;

        answer = input(f"My prediction is {prediction}. If it is superior, enter (A). If it is inferior, enter (B). If it is correct, enter (C) ").lower();

        if answer == "a":
            superior_limit = prediction - 1;
        elif answer == "b":
            inferior_limit = prediction + 1;

    print(f"Yessss! The computer guessed the number correctly {prediction} ");


guess_number_computer(10);

