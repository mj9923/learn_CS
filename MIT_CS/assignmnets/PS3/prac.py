def substitute_hand(hand, letter):
    if hand.has_key(letter):
        alphabet=(VOWELS+CONSONANTS).replace(letter,"")
        x=random.choice(alphabet)
        hand.replace(letter, x)
        replace=True
    else:
        print("That letter is not in your hand.")
        replace=False

def play_game(word_list):
    total_num_hands=int(input("Enter total number of hands:"))
    overall_score=0
    replay =0
    #0.start of the game loop
    while total_num_hands!=0
        #1. setting up initial variables
        total_score=0
        hand = deal_hand(HAND_SIZE)
        #1-1 print current hand
        print("Current hand:", display_hand(hand))

        sub_letter=str(input("Would you like to substitute a letter?"))
        if substitute == "yes":
            while replace==False:
                letter=str(input("Which letter would you like to replace:"))
                hand=hand
                substitute_hand(hand, letter)
        elif substitute == "no":
            continue
        #리플레이를 한 적이 없다면 리플레이를 묻는다
        #리플레이는 한 번 하면 다시 루프를 만들지 않는다.
        if replay==0
            play_hand(hand,word_list)
            #ask for replay
            rep=str(input("Would you like to replay hand?"))
            if rep=="yes":
                replay==1
                play_hand(hand,word_list)
            if rep =="no":
                replay=0
        elif replay==1
            play_hand(hand,word_list)

        overall_score+=total_score
        total_num_hands-=1
    print("Total score over all hands:", overall_score)
    
