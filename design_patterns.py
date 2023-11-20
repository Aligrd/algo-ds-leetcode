from abc import ABC, abstractmethod


class Burger:
    def __init__(self, ing: list) -> None:
        self.ingredient = ing

    def print(self):
        print(self.ingredient)


class BurgerFactory:
    def createSimpleBurger(self):
        ingredient = ["cheese", "burger-pad", "bread"]
        return Burger(ingredient)

    def createCVeganBurger(self):
        ingredient = ["tomato", "grass", "bread"]
        return Burger(ingredient)

    def createChickenBurger(self):
        ingredient = ["cheese", "chicken-pad", "bread"]
        return Burger(ingredient)


class BurgerBuilder:
    def __init__(self) -> None:
        self.ingredinet = []

    def addBread(self, type: str):
        self.ingredinet.append(type)

    def addPad(self, type: str):
        self.ingredinet.append(type)

    def addSuace(self, type: str):
        self.ingredinet.append(type)

    def build(self):
        return Burger(self.ingredinet)


#! buidler design pattern
# burgerbulder = BurgerBuilder()
# burgerbulder.addBread("mac-bread")
# burgerbulder.addSuace("tomato-suace")
# burgerbulder.addPad("chicken")
# burgerbulder.build().print()

#! buidler design pattern
# burger_factory = BurgerFactory()
# burger_factory.createChickenBurger().print()
# burger_factory.createCVeganBurger().print()
# burger_factory.createSimpleBurger().print()


#! singleton design pattern
# class ApplicationState:
#     instance = None

#     def __init__(self) -> None:
#         self.isLoggedIn = False

#     @staticmethod
#     def getAppState():
#         if not ApplicationState.instance:
#             ApplicationState.instance = ApplicationState()
#         return ApplicationState.instance


# appState = ApplicationState.getAppState()

# print("first state", appState.isLoggedIn)  # false

# appState2 = ApplicationState.getAppState()

# appState.isLoggedIn = True

# print("first state after change ", appState.isLoggedIn)
# print("seccond state after change", appState.isLoggedIn)


# abstraction for youtube Users (interface for youtuber User)

# class Event:
#     def __init__(self,) -> None:

#     @staticmethod
#     def newVideo():
#         return "hey new Video Added"
#     @staticmethod
#     def Liked():
#         return "hey new Video Added"

#! observer Pattern
# class YoutubeSubscriber(ABC):
#     @abstractmethod
#     def sendNotification(self, event: str):
#         pass


# class YoutubeUser(YoutubeSubscriber):
#     def __init__(self, name) -> None:
#         self.name = name

#     def sendNotification(self, channel, event: str):
#         print(f"User {self.name} recived a notification from {channel} : {event}")


# class YoutubeChannel:
#     def __init__(self, name) -> None:
#         self.subscribers: list[YoutubeUser] = []
#         self.name = name

#     def subscribe(self, newSub: YoutubeUser):
#         self.subscribers.append(newSub)

#     def notify(self, event):
#         for subscriber in self.subscribers:
#             subscriber.sendNotification(self.name, event)


# myChannel = YoutubeChannel("self improvment as always! :)")

# user1 = YoutubeUser("fatguys")
# user2 = YoutubeUser("hornyguy")
# user3 = YoutubeUser("smartguy")

# myChannel.subscribe(user1)
# myChannel.subscribe(user2)
# myChannel.subscribe(user3)


# myChannel.notify("if you want six pack and get rich fast click this video")


# class ListNode:
#     def __init__(self, value) -> None:
#         self.val = value
#         self.next = None


# class LinkedList:
#     def __init__(self, firstNode: ListNode) -> None:
#         self.head = firstNode  # first index
#         self.cur: ListNode = None  # current pointer

#     def __iter__(self):
#         self.cur = self.head
#         return self

#     def __next__(self):
#         if self.cur:
#             val = self.cur.val
#             self.cur = self.cur.next
#             return val
#         else:
#             raise StopIteration


# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# myList = LinkedList(head)

# # iterate through LinkedList
# for n in myList:
#     print(n)


#! behavioral pattern - Strategy
# class FilterStrategy(ABC):
#     @abstractmethod
#     def filterValues():
#         pass


# class FilterNegativeValues(FilterStrategy):
#     def filterValues(self, value):
#         return value < 0


# class FilterOddValue(FilterStrategy):
#     def filterValues(self, value):
#         return abs(value) % 2


# class Values:
#     def __init__(self, val) -> None:
#         self.vals = val

#     def filter(self, strategy: FilterStrategy):
#         res = []
#         for n in self.vals:
#             if not strategy.filterValues(n):
#                 res.append(n)
#         return res


# values = Values([-2 - 1, 0, 3, 5, 6])

# data = values.filter(FilterOddValue())
# print(data)

#! structural pattern

#!adaptor pattern

# class USBCable:
#     def __init__(self) -> None:
#         self.isPlugged = False

#     def plugIn(self):
#         self.isPlugged = True


# class MicroUSBCable:
#     def __init__(self) -> None:
#         self.isPlugged = False

#     def PlugMicro(self):
#         self.isPlugged = True


# class USBPort:
#     def __init__(self) -> None:
#         self.portAvailable = True

#     def plug(self, usb: USBCable):
#         usb.plugIn()
#         self.portAvailable = False


# class MicroToUSBAdaptor(USBCable):
#     def __init__(self, microUsbCable: MicroUSBCable) -> None:
#         self.microUsbCable = microUsbCable
#         self.microUsbCable.PlugMicro()


# # usb cable can plug into usb port
# usbCable = USBCable()
# usbPort = USBPort()
# microusbcable = MicroUSBCable()

# mtua = MicroToUSBAdaptor(microusbcable)

# # usbPort.plug(usbCable)
# usbPort.plug(mtua)
# print(usbPort.portAvailable)


