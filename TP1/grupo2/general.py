#for clearing the console
import os

#for checking if a value is a function
import types

#for type hinting
from typing import Callable
from typing import Dict
from typing import List
from typing import Self

#clears the screen, hopefully does so in linx too
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#checks if value is a lambda
def isALambda(v):
    LAMBDA = lambda:0
    return isinstance(v, type(LAMBDA)) and v.__name__ == LAMBDA.__name__

#checks if value is a function
def isAFunction(v):
    return isinstance(open, types.FunctionType)

#wait for key press
def waitForKeyPress():
    try:
        input("Press enter to continue...")

    except SyntaxError:
        pass

#Option
class Option:
    def __init__(self):
        self.name: str = ""
        self.label: str = ""
        self.childrens: Dict[str, Option] = {}
        self.action: Callable[[dict], dict] = None
        self.function: Callable[[dict], dict] = None
        self.isMenu: bool = False
    
    def __str__(self):
        return self.name + self.label
    
    #the idea behind the fields "action" and "function" in a Option object is that "actions" 
    #are supposed to be code that should be excecuted when a "option" that is a submenu is selected, 
    #and "function" is supposed to do something when a option that is a "function" is selected 
    def excecute(self, data):
        if self.action is not None:
            data = self.action(data)

        if self.function is not None:
            data = self.function(data)

        return data
    
    def setLabel(self, label: str):
        self.label = label

    def setAction(self, action: types.FunctionType):
        self.action = action

    def setAsMenu(self):
        self.isMenu = True

    def setName(self, name: types.FunctionType):
        self.name = name
        
    def setFunction(self, function: types.FunctionType):
        self.function = function
    
    def getChildrens(self) -> Dict[str, Self]:
        return self.childrens
    
    def setChildren(self, children: Dict[str, Self]):
        self.childrens = children

class Options:
    def __init__(self, baseTree: Dict):
        self.root: Option = Options.optionFactory(baseTree)
        self.dir: List[str] = []
        self.menu: Option = self.root.getChildrens()

        self.ocurrences: Dict[str, int] = {}
        self.history: List[str] = []
    
    #get menu based on the current dir 
    def getOptions(self) -> Dict[str, Option]:
        if len(self.dir) == 0:
            self.menu = self.root.getChildrens()
            
        else:
            tmp = self.root
            for step in self.dir:
                tmp = tmp.getChildrens()[step]

            self.menu =  tmp.getChildrens()

        return self.menu

    def getSelected(self, selection: str) -> Option:
        selected = self.menu[selection]
        if selected.isMenu:    
            self.dir.append(selection)

            path = ' -> '.join(self.dir)

            self.history.append(path)

            if path in self.ocurrences:
                self.ocurrences[path] += 1

            else:
                self.ocurrences[path] = 1

        return selected
    
    def setBack(self):
        self.dir = self.dir[:-1]

    def lastSelections(self) -> List[str]:
        return self.history[-3:]
    
    #factory to create objects of the class Option
    @staticmethod
    def optionFactory(tree: dict, name: str = "") -> Option:
        option = Option()   
        option.setName(name)

        if "action" in tree.keys():
            option.setAction(tree.pop("action"))    
        
        if "label" in tree.keys():
            option.setLabel(tree.pop("label"))

        if "function" in tree.keys():
            option.setFunction(tree.pop("function"))

        else:
            childrens = {}
            for key in tree.keys():
                childrens[key] = Options.optionFactory(tree[key], key)
 
            option.setChildren(childrens)
            option.setAsMenu()
        return option

#State
class Order:
    def __init__(self, id):
        self.id: int = id
        self.items: List[str] = []
        self.itemsCost: Dict[str, float] = {}
        self.cost: float = 0

    def __str__(self):
        string = "ID: " + str(self.id)
        string += "\nItems: "
        for item in self.items:
            string += "\n" + item + ", Costo: " + str(self.itemsCost[item])

        string += "\nTotal: " + str(self.cost)
        return string

    def isOrderEmpty(self) -> bool:
        return len(self.items) == 0

    def addItemToOrder(self, item: str, cost: float):
        self.itemsCost[item] = cost
        self.items.append(item)
        self.cost += cost

class Orders:
    def __init__(self):
        self.orders: List[Order] = []

        self.itemsOcurrences: Dict[str, int] = {}
        self.itemsTotalCost: float = 0
        self.itemsCost: Dict[str, int] = {}

    def __str__(self):
        string = "Ordenes: \n"

        for order in self.orders:
            string += "\n\n" + str(order)

        return string
         
    def addOrder(self, order: Order):
        for item in order.items:
            if item in self.itemsOcurrences:
                self.itemsOcurrences[item] += 1

            else:
                self.itemsOcurrences[item] = 1

        for item in order.itemsCost:
            self.itemsCost[item] = order.itemsCost[item]

        self.itemsTotalCost += order.cost


        self.orders.append(order)
    
    def getNewOrder(self):
        return Order(len(self.orders))
    
class MenuData:
    def __init__(self, baseTree: Dict):
        self.keepExcecuting: bool = True

        self.orders: Orders = Orders()
        self.order: Order = self.orders.getNewOrder()

        self.options: Options = Options(baseTree)

    def setKeepExcecuting(self, keepExcecuting: bool):
        self.keepExcecuting = keepExcecuting

    def doWeKeepExcecuting(self) -> bool:
        return self.keepExcecuting

    def confirmOrder(self):
        self.orders.addOrder(self.order)
        self.order = self.orders.getNewOrder()