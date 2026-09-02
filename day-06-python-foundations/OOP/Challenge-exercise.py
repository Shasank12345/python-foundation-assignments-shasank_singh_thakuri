'''MINI LIBRARY MANAGEMENT SYSTEM'''

from abc import ABC, abstractmethod


class ItemAlreadyCheckedOutError(Exception):
    '''IS RAISED IF USER TRIES TO BORROW ALREADY CHECKEDOUT ITEM'''



class ItemNotBorrowedError(Exception):
    '''exception when member tries too return an item they dont have'''



class LibraryItem(ABC):
    def __init__(self, tittle, item_id):
        self.info = (tittle, item_id)
        self._checked_out: bool = False

    @property
    def info(self):
        return (self._tittle, self._item_id)

    @info.setter
    def info(self, data: tuple[str, str]):
        tittle, item_id = data
        self._tittle = tittle
        self._item_id = item_id

    @property
    def tittle(self):
        return self._tittle

    @property
    def is_checked_out(self):
        return self._checked_out

    @is_checked_out.setter
    def is_checked_out(self, item):
        if self._checked_out is True and item is True:
            raise ItemAlreadyCheckedOutError("Sorry Item is ALready checked out cant procced with the action")
        self._checked_out = item

    @abstractmethod
    def describe(self):
        '''ABSTRACT METHOD'''
        pass


class Book(LibraryItem):
    def __init__(self, tittle, item_id, author):
        super().__init__(tittle, item_id)
        self.author = author

    def describe(self):
        print(f"BOOK : {self._tittle}  BY : {self.author}")


class DVD(LibraryItem):
    def __init__(self, tittle, item_id, duration_mins):
        super().__init__(tittle, item_id)
        self.duration = duration_mins

    def describe(self):
        print(f"DVD: {self._tittle}  Duration : {self.duration} mins")


class Magazine(LibraryItem):
    def __init__(self, tittle, item_id, issue_number):
        super().__init__(tittle, item_id)
        self.issue_number = issue_number

    def describe(self):
        print(f"Magazine :{self._tittle} issue_number :{self.issue_number}")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.__borrowed_items = []

    @property
    def borrowed_items(self) -> tuple:
        return tuple(self.__borrowed_items)

    def borrow(self, item):
        self.__borrowed_items.append(item)

    def return_item(self, item):
        if item not in self.__borrowed_items:
            raise ItemNotBorrowedError("Item isnt Borrowed")
        self.__borrowed_items.remove(item)


class Library:
    def __init__(self):
        self.catlog = []
        self.members = []

    def checkout(self, member, item):
        item.is_checked_out = True
        member.borrow(item)

    def checkin(self, member, item):
        member.return_item(item)
        item.is_checked_out = False

    @classmethod
    def from_catlog(cls, list_of_dict: list):
        library_instance = cls()
        for item_data in list_of_dict:
            item_type = item_data.get("type", "").lower()
            if item_type == "book":
                item = Book(item_data["title"], item_data["id"], item_data["author"])
            elif item_type == "dvd":
                item = DVD(item_data["title"], item_data["id"], item_data["duration"])
            elif item_type == "magazine":
                item = Magazine(item_data["title"], item_data["id"], item_data["issue"])
            else:
                continue
            library_instance.catlog.append(item)
        return library_instance


catalog_data = [

    {"type": "book", "title": "The Pragmatic Programmer", "id": "B001", "author": "Andrew Hunt"},
    {"type": "dvd", "title": "Inception", "id": "D001", "duration": 148},
    {"type": "magazine", "title": "Scientific American", "id": "M001", "issue": 320}
]
lib = Library.from_catlog(catalog_data)
print("--- Library Catalog ---")
for item in lib.catlog:
    item.describe()
mem = Member("Shasank", "M01")
lib.checkout(mem, lib.catlog[0])
print(f"\n{mem.name} borrowed: {[item.tittle for item in mem.borrowed_items]}")

try:
    lib.checkout(mem, lib.catlog[0])
except ItemAlreadyCheckedOutError as e:
    print(f"Exception Caught: {e}")
try:
    lib.checkin(mem, lib.catlog[1])
except ItemNotBorrowedError as e:
    print(f"Exception Caught: {e}")