def innings(batsman, to_chase):
    print("Enter numbers between 1 and 6. If you both choose the same number then " + batsman + " is out")
    total = 0

    while True:
        pnum = input_num(1, 6)
        cnum = random.randint(1, 6)

        print("User chose", pnum)
        print("Computer chose", cnum)

        if pnum == cnum:
            print(batsman + " is out")
            return total
        else:
            total = total + (pnum if batsman == "User" else cnum)
            print(batsman + " score is", total)
            if to_chase is not None and total > to_chase:
                return total
