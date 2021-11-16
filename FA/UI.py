from FA import FiniteAutomata

class Console:

    def __readFA(self):
        self.fa = FiniteAutomata.readFromFile('fa.in')

    def __displayAll(self):
        print(self.fa)

    def __displayStates(self):
        print(self.fa.Q)

    def __displayAlphabet(self):
        print(self.fa.E)

    def __displayTransitions(self):
        print(self.fa.S)

    def __displayFinalStates(self):
        print(self.fa.F)

    def __checkDFA(self):
        print(self.fa.isDfa())

    def __checkAccepted(self):
        seq = input()
        print(self.fa.isAccepted(seq))

    def __displayMenu(self):
        print("1.Read FA")
        print("2.Display FA")
        print("3.Display States")
        print("4.Display Alphabet")
        print("5.Display transitions")
        print("6.Display final states")
        print("7.Check is DFA")
        print("8.Check accepted sequence")
        print("9.Exit")

    def run(self):
        while(1):
            self.__displayMenu()
            cmd=int(input())
            if cmd == 1:
                self.__readFA()
            if cmd == 2:
                self.__displayAll()
            if cmd == 3:
                self.__displayStates()
            if cmd ==  4:
                self. __displayAlphabet()
            if cmd == 5:
                self.__displayTransitions()
            if cmd == 6:
                self.__displayFinalStates()
            if cmd == 7:
                self.__checkDFA()
            if cmd == 8:
                self.__checkAccepted()
            if cmd == 9:
                break