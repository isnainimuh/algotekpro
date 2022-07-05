from random import choice

def play() :
    user=input("Pilih 1 ('r' batu, 's' gunting, 'p' kertas) : ")
    computer=choice(['r','s','p'])

    if (user==computer):
        print ("Seimbang!")
    elif is_win(user, computer):
        print ("Kamu menang!!")
    else:
        print ("Kamu Kalah!!")


def is_win(player, opponent) :
    #return True if player wins
    #p>r r>s s>p
    if (player=='p' and opponent=='r') or (player=='r' and opponent=='s') or (player=='s' and opponent=='p') :
        return True


play()