class Product:
    def __init__(self, name, code, stock):
        self.name = name
        self.code = code
        self.stock = stock
        self.next = None

class Inventory:
    def __init__(self):
        self.head = None

    def add_product(self, name, code, stock):
        new_product = Product(name, code, stock)
        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_product

    def remove_product(self, code):
        if self.head is None:
            return

        if self.head.code == code:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.code == code:
                current.next = current.next.next
                return
            current = current.next

    def print_inventory(self):
        if self.head is None:
            print("Inventory is empty.")
        else:
            current = self.head
            print("Inventory Items:")
            while current is not None:
                print(f"Name: {current.name}, Code: {current.code}, Stock: {current.stock}")
                current = current.next

inventory = Inventory()

inventory.add_product("komputer", "KB01",15)
inventory.add_product("keyboard", "MS01", 15)
inventory.add_product("mouse", "MN01", 15)
inventory.add_product("speaker", "HP01", 10)

inventory.print_inventory()

print("---")

inventory.remove_product("HP01")

inventory.print_inventory()
