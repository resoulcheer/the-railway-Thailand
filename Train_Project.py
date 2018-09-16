# Node of Doubly Link list consisting of
#   - data as string
#   - Next as Node
#   - Prev as Node
class Node:
    def __init__(self,Prev,data,Next):
        self.data = data
        self.Next = Next
        self.Prev = Prev
# Doubly Link list consisting of
#   - head as Node
#   - tail as Node
class DoublyLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def show(self):
        curP = self.head
        text = ""
        while(curP != None):
            text += "   -" + curP.data + "\n"
            curP = curP.Next 
        print("\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII" + text \
              + "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n")

    def railway(self,start,last):
        curP = self.head
        text = ""
        while(curP.data != start):
            curP = curP.Next
            
        while(curP != None):
            if curP.data == last:
                text += "   -" + curP.data + "\n"
                print("\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII" + text \
              + "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n")
                break
            else:
                text += "   -" + curP.data + "\n"
            curP = curP.Next
        
    def search(self,data):
        curP = self.head
        while(curP != None):
            if(curP.data == data):
                print("*** Available ***\n")
                return True
            curP = curP.Next
        print("XXX Unvailable XXX\n")
        return False
        
    def delete(self,data):
        curP = self.head
        while(curP != None):
            if(curP.data == data):
                if(curP.Prev == None):
                    curP.Next.Prev = None
                    self.head = curP.Next
                    self.head.Prev = None
                elif(curP.Next == None):
                    curP.Prev.Next = None
                    self.tail = curP.Prev
                    self.tail.Next = None
                else:
                    curP.Prev.Next = curP.Next
                    curP.Next.Prev = curP.Prev
                break
            curP = curP.Next
        return
    def append(self,data):
        newNode = Node(None,data,None)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.Prev = self.tail
            self.tail.Next = newNode
            self.tail = newNode
    def Insert(self,data,pos):
        newNode = Node(None,data,None)
        curP = self.head
        for i in range(0,pos):
            if(curP.Next != None):
                curP = curP.Next
            else:
                break
        if(curP.Prev == None):
            newNode.Next = curP
            curP.Prev = newNode
            self.head = newNode
        elif(curP.Next == None):
            newNode.Prev = curP
            curP.Next = newNode
            self.tail = newNode
        else:
            newNode.Next = curP
            newNode.Prev = curP.Prev
            curP.Prev.Next = newNode
            curP.Prev = newNode
            

myLL = DoublyLinkList()

pp = ["CHIANG MAI","LAMPANG","UTARADIT","PHITSANULOK","NAKHON SAWAN","LOPBURI","BANGKOK"]
for i in range(0,len(pp)):
    myLL.append(pp[i])

IsActive = True;
def Choice(input_choice):
    while(IsActive):
        if input_choice == "1":
            print("\n>>>Recent railway<<<")
            myLL.show()
        elif input_choice == "2":
            print(">>>Open station<<<")
            input_data = input("*Enter station name*: ")
            input_pos = int(input("*Enter number of position: "))
            myLL.Insert(input_data.upper(), input_pos - 1)
            myLL.show()
        elif input_choice == "3":
            print(">>>Close station<<<")
            input_del = input("*Enter station*: ")
            myLL.delete(input_del.upper())
            myLL.show()
        elif input_choice == "4":
            print(">>>Check station<<<")
            input_se = input("*Enter station*: ")
            myLL.search(input_se.upper())
        elif input_choice == "5":
            print(">>>Show your railway<<<")
            input_start = input("*Enter start station*: ")
            input_last = input("*Enter last station*: ")
            myLL.railway(input_start.upper(), input_last.upper())
        elif input_choice == "Q" or "q":
            exit()
        else:
            print("/1/ Show railway")
            print("/2/ Open station")
            print("/3/ Close station")
            print("/4/ Check station available")
            print("/5/ Show your railway")
            print("/Q/ Quit \n")
            return Choice(input("(@__@)? Error, Please Enter again: "))
        
        input_choice = input("**Enter your choice**: ")
        
print("#########################################################################\
############################## Welcome to Railway Thailand ##########################\
##################################################################################")
print("/1/ Show railway")
print("/2/ Open station")
print("/3/ Close station")
print("/4/ Check station available")
print("/5/ Show your railway")
print("/Q/ Quit \n")
input_choice = input("**Enter your choice**: ")
print(Choice(input_choice))
