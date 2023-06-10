class Player:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.next = None

class Tournament:
    def __init__(self):
        self.head = None

    def add_player(self, name, rank):
        new_player = Player(name, rank)
        if self.head is None:
            self.head = new_player
        else:
            current = self.head
            if new_player.rank < current.rank:
                new_player.next = current
                self.head = new_player
            else:
                while current.next is not None and new_player.rank > current.next.rank:
                    current = current.next
                new_player.next = current.next
                current.next = new_player

    def remove_player(self, name):
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

    def print_players(self):
        if self.head is None:
            print("No players registered.")
        else:
            current = self.head
            print("Tournament Players:")
            while current is not None:
                print(f"Name: {current.name}, Rank: {current.rank}")
                current = current.next

tournament = Tournament()

tournament.add_player("wangi", 2000)
tournament.add_player("yuni", 1800)
tournament.add_player("sima", 1400)
tournament.add_player("dina", 1700)

tournament.print_players()

print("---")

tournament.remove_player("sima")

tournament.print_players()
