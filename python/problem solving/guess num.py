secret_num=2424
guess=""
guess_count=1
guess_limit=3
out_of_guesses= False
while guess!=secret_num and not(out_of_guesses):
    if guess_count <= guess_limit:
        guess=int(input("guesses num:"))
        break
        if guess_count<guess_limit:
            print("remain guess:", guess_limit - guess_count)
        guess_count += 1
    else:
        out_of_guesses= True

if out_of_guesses:
    print("you r out of guessses")
else:
    print("you win")
