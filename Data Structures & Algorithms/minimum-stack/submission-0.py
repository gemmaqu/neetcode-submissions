class MinStack:

    def __init__(self):

        self.mini = [] # need self to share variables across methods
        self.regular = []

    def push(self, val: int) -> None:
        self.regular.append(val) 
        if len(self.mini) == 0: # b/c wanna check the REAL NUMBER
            self.mini.append(val)
        else:
            currentmin = self.mini[-1]

            if currentmin >= val:
                self.mini.append(val)
            else:
                self.mini.append(currentmin)
        

    def pop(self) -> None:
        self.regular.pop()
        self.mini.pop()
        #no need to check anytthing, since the mini stack will go back to the
        #upper
        

    def top(self) -> int:
        return self.regular[-1]
        # directly get the last element! list index!!! need to return!!!
        

    def getMin(self) -> int:
        return self.mini[-1]
        
