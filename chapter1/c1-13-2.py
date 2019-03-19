# 1.13.2: Inheritance: Logic Gates and Circuits
# Come back to this tonight

class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None


    def getLabel(self):
        return self.label


    def getOutput(self):
        # we are writing a method for a class that doesn't exist yet.
        # this actually works.
        self.output = self.performGateLogic()  
        return self.output


# putting LogicGate in parentheses means that BinaryGate is a subclass of LogicGate
class BinaryGate(LogicGate):

    def __init__(self, n):
        # the first thing we want to do is initialize any data items inherited through LogicGate
        LogicGate.__init__(self, n)
        
        # input pins of the gate
        self.pinA = None
        self.pinB = None
    

    def getPinA(self):
        if self.pinA == None:
            return(int(input("Enter Pin A input for gate " + self.getLabel() + "-->")))
        else:
            return self.pinA.getFrom().getOutput()


    def getPinB(self):
        if self.pinB == None:
            return(int(input("Enter Pin B input for gate " + self.getLabel() + "-->")))
        else:
            return self.pinB.getFrom().getOutput()


    # This method sets pins when we are using 
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError('Error: There are 0 free pins!')


class UnaryGate(LogicGate):
    
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None


    def getPin(self):
        return(int(input("Enter Pin input for gate " + self.getLabel() + "-->")))


    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError('Error: There are 0 free pins!')



class AndGate(BinaryGate):

    def __init__(self, n):
        ### 'super' looks at the superclass of the first object, 
        ### passes in the class and instance, 
        ### and then the parameter in the init
        # this is just a different syntax than earlier that will be useful later. 
        # get used to this syntax
        super(AndGate, self).__init__(n)


    def performGateLogic(self):  #don't forget to use self in *every* method declaration's parameters
        a = self.getPinA()
        b = self.getPinB()

        return(a == 1 and b == 1)


class OrGate(BinaryGate):

    def __init__(self, n):
        super(OrGate, self).__init__(n)

    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        return( a == 1 or b == 1)


class NotGate(UnaryGate):

    def __init__(self, n):
        super(NotGate, self).__init__(n)


    def performGateLogic(self):
        return not self.getPin()



# now let's start building circuits
# Start with a Connector class to connect the circuits
class Connector():

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)


    def getFrom(self):
        return self.fromgate


    def getTo(self):
        return self.togate


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())

main()


