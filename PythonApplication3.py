from bangtal import *
import random

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene1 = Scene("장면1", "Images/주사위 배경.png")

com_dice1 = Object("Images/1주사위.png")
com_dice1.setScale(0.4)
com_dice1.locate(scene1, 50, 450)
com_dice1.hide()

com_dice2 = Object("Images/2주사위.png")
com_dice2.setScale(0.4)
com_dice2.locate(scene1, 200, 450)
com_dice2.hide()

com_dice3 = Object("Images/3주사위.png")
com_dice3.setScale(0.4)
com_dice3.locate(scene1, 350, 450)
com_dice3.hide()

com_dice4 = Object("Images/4주사위.png")
com_dice4.setScale(0.4)
com_dice4.locate(scene1, 50, 300)
com_dice4.hide()

com_dice5 = Object("Images/5주사위.png")
com_dice5.setScale(0.4)
com_dice5.locate(scene1, 200, 300)
com_dice5.hide()

com_dice6 = Object("Images/6주사위.png")
com_dice6.setScale(0.4)
com_dice6.locate(scene1, 350, 300)
com_dice6.hide()

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ#

your_dice1 = Object("Images/노랑주사위1.png")
your_dice1.setScale(0.4)
your_dice1.locate(scene1, 700, 450)

your_dice2 = Object("Images/노랑주사위2.png")
your_dice2.setScale(0.4)
your_dice2.locate(scene1, 850, 450)

your_dice3 = Object("Images/노랑주사위3.png")
your_dice3.setScale(0.4)
your_dice3.locate(scene1, 1000, 450)

your_dice4 = Object("Images/노랑주사위4.png")
your_dice4.setScale(0.4)
your_dice4.locate(scene1, 700, 300)

your_dice5 = Object("Images/노랑주사위5.png")
your_dice5.setScale(0.4)
your_dice5.locate(scene1, 850, 300)

your_dice6 = Object("Images/노랑주사위6.png")
your_dice6.setScale(0.4)
your_dice6.locate(scene1, 1000, 300)


start = Object("Images/시작버튼.png")
start.setScale(2.5)
start.locate(scene1, 500, 150)
start.show()

end = Object("Images/종료버튼.png")
end.setScale(0.1)
end.locate(scene1, 1100, 600)
end.show()


computer = 0


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ#

def start_onMouseAction(x, y, action):   # 시작버튼
    start.hide()
    global computer
    
    com_dice1.hide()
    com_dice2.hide()
    com_dice3.hide()
    com_dice4.hide()
    com_dice5.hide()
    com_dice6.hide()

    your_dice1.show()
    your_dice2.show()
    your_dice3.show()
    your_dice4.show()
    your_dice5.show()
    your_dice6.show()
    showMessage("1-6까지의 주사위 중 하나를 선택해주세요")

    computer = random.randint(1,6)
start.onMouseAction = start_onMouseAction


# 당신이 1 선택시 함수 
def one_onMouseAction(x, y, action): 
    global computer
   
    your_dice2.hide()
    your_dice3.hide()
    your_dice4.hide()
    your_dice5.hide()
    your_dice6.hide()

    if computer == 1:
        com_dice1.show()
        showMessage("비겼습니다!")
    elif computer == 2:
        com_dice2.show()
        showMessage("컴퓨터가 이겼습니다")
    elif computer == 3:
        com_dice3.show()
        showMessage("컴퓨터가 이겼습니다")
    elif computer == 4:
        com_dice4.show()
        showMessage("컴퓨터가 이겼습니다")
    elif computer == 5:
        com_dice5.show()
        showMessage("컴퓨터가 이겼습니다")
    else:
        com_dice6.show()
        showMessage("컴퓨터가 이겼습니다")

    start.locate(scene1, 1000, 100 )
    start.show()
your_dice1.onMouseAction = one_onMouseAction

# 당신이 2 선택 시 함수

def two_onMouseAction(x, y, action):  
    global computer

    your_dice1.hide()
    your_dice3.hide()
    your_dice4.hide()
    your_dice5.hide()
    your_dice6.hide()

    if computer == 1:
        com_dice1.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 2:
        com_dice2.show()
        showMessage("비겼습니다")
    elif computer == 3:
        com_dice3.show()
        showMessage("컴퓨터가 이겼습니다")
    elif computer == 4:
        com_dice4.show()
        showMessage("컴퓨터가 이겼습니다")
    elif computer == 5:
        com_dice5.show()
        showMessage("컴퓨터가 이겼습니다")
    else:
        com_dice6.show()
        showMessage("컴퓨터가 이겼습니다")

    start.locate(scene1, 1000, 100 )
    start.show()
your_dice2.onMouseAction = two_onMouseAction


# 당신이 3 선택시 함수 
def three_onMouseAction(x, y, action): 
    global computer
    your_dice1.hide()
    your_dice2.hide()
    your_dice4.hide()
    your_dice5.hide()
    your_dice6.hide()

    if computer == 1:
        com_dice1.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 2:
        com_dice2.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 3:
        com_dice3.show()
        showMessage("비겼습니다!")
    elif computer == 4:
        com_dice4.show()
        showMessage("컴퓨터가 이겼습니다")
    elif computer == 5:
        com_dice5.show()
        showMessage("컴퓨터가 이겼습니다")
    else:
        com_dice6.show()
        showMessage("컴퓨터가 이겼습니다")

    start.locate(scene1, 1000, 100 )
    start.show()
your_dice3.onMouseAction = three_onMouseAction

        
# 당신이 4 선택시 함수 
def four_onMouseAction(x, y, action): 
    global computer
    your_dice1.hide()
    your_dice2.hide()
    your_dice3.hide()
    your_dice5.hide()
    your_dice6.hide()

    if computer == 1:
        com_dice1.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 2:
        com_dice2.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 3:
        com_dice3.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 4:
        com_dice4.show()
        showMessage("비겼습니다")
    elif computer == 5:
        com_dice5.show()
        showMessage("컴퓨터가 이겼습니다")
    else:
        com_dice6.show()
        showMessage("컴퓨터가 이겼습니다")

    start.locate(scene1, 1000, 100 )
    start.show()
your_dice4.onMouseAction = four_onMouseAction     

# 당신이 5 선택시 함수 
def five_onMouseAction(x, y, action): 
    global computer
    your_dice1.hide()
    your_dice2.hide()
    your_dice3.hide()
    your_dice4.hide()
    your_dice6.hide()

    if computer == 1:
        com_dice1.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 2:
        com_dice2.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 3:
        com_dice3.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 4:
        com_dice4.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 5:
        com_dice5.show()
        showMessage("비겼습니다")
    else:
        com_dice6.show()
        showMessage("컴퓨터가 이겼습니다")

    start.locate(scene1, 1000, 100 )
    start.show()
your_dice5.onMouseAction = five_onMouseAction 

# 당신이 6 선택시 함수 
def six_onMouseAction(x, y, action): 
    global computer
    your_dice1.hide()
    your_dice2.hide()
    your_dice3.hide()
    your_dice4.hide()
    your_dice5.hide()

    if computer == 1:
        com_dice1.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 2:
        com_dice2.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 3:
        com_dice3.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 4:
        com_dice4.show()
        showMessage("당신이 이겼습니다!")
    elif computer == 5:
        com_dice5.show()
        showMessage("당신이 이겼습니다!")
    else:
        com_dice6.show()
        showMessage("비겼습니다")

    start.locate(scene1, 1000, 100 )
    start.show()
your_dice6.onMouseAction = six_onMouseAction 


def end_onMouseAction(x, y, action):
    endGame()
end.onMouseAction = end_onMouseAction

startGame(scene1)

