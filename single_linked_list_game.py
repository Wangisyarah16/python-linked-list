class Item:
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance
        self.next = None

class Backpack:
    def __init__(self):
        self.head = None

    def add_item(self, name, importance):
        new_item = Item(name, importance)
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            if new_item.importance > current.importance:
                new_item.next = current
                self.head = new_item
            else:
                while current.next is not None and new_item.importance < current.next.importance:
                    current = current.next
                new_item.next = current.next
                current.next = new_item

    def remove_item(self, name):
        if self.head is None:
            return

        if self.head.name == name:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                return
            current = current.next

    def print_items(self):
        if self.head is None:
            print("Backpack is empty.")
        else:
            current = self.head
            print("Backpack Items:")
            while current is not None:
                print(f"Name: {current.name}, Importance: {current.importance}")
                current = current.next

backpack = Backpack()

backpack.add_item("pedang", 5)
backpack.add_item("ramuan", 3)
backpack.add_item("koin emas", 20)
backpack.add_item("Map", 2)

backpack.print_items()

print("---")

backpack.remove_item("ramuan")

backpack.print_items()
