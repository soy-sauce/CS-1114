import random
class Die:
    def __init__(self, faces=6):
        self.number_of_faces=faces
        self.curr_face_value=random.randint(1,self.number_of_faces)

    def __repr__(self):
        return self.curr_face_value

    def roll(self):
        self.curr_face_value = random.randint(1, self.number_of_faces)
        return self.curr_face_value

class PigGamePlayer:
    def __init__(self,name):
        self.name=name
        self.die=Die()
        self.score=0
        self.total_score=0

    def play_turn(self):
        temp=self.die.roll()
        print("You rolled ",temp)
        if temp==1:
            print("You scored 0 points this turn. Your total score is ", self.total_score)
            self.score=0
        else:
            self.score+=temp
            print("Your score for this turn is: ",self.score)
            again=input("Roll again? (type 'r' for roll, or 'h' for hold: ")
            if again=='r':
                self.play_turn()
            if again=='h':
                self.total_score+=self.score
                print("You score is ",self.score," points this turn. Your total score is ",self.total_score)
                self.score=0


class PigGame:
    def __init__(self,player1_name,player2_name):
        self.player1=PigGamePlayer(player1_name)
        self.player2=PigGamePlayer(player2_name)

    def play(self):
        while self.player1.total_score<100 and self.player2.total_score<100:
            print(self.player1.name, "'s Turn:")
            self.player1.play_turn()
            print("\n")
            print(self.player2.name, "'s Turn: ")
            self.player2.play_turn()
            print("\n")

        if self.player1.total_score>=100:
            print(self.player1.name," won!")
        elif self.player2.total_score>=100:
            print(self.player2.name," won!")


def main():
    name1 = input("Player #1, enter your name: ")
    name2 = input("Player #2, enter your name: ")
    game1 = PigGame(name1, name2)
    game1.play()


main()