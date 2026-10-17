
class SocialNetwork:
    def __init__(self, users):
        self.users = users
        self.matrix = [[0] * len(users) for _ in users]

    def add_friendship(self, user1, user2):
        i = self.users.index(user1)
        j = self.users.index(user2)
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1

    def display(self):
        print("  ", *self.users)
        for i in range(len(self.users)):
            print(self.users[i], self.matrix[i])

    def show_friends(self, user):
        i = self.users.index(user)
        print("Friends of", user, ":")
        for j in range(len(self.users)):
            if self.matrix[i][j] == 1:
                print(self.users[j])


users = ["Alice", "Bob", "Charlie", "David"]
network = SocialNetwork(users)

network.add_friendship("Alice", "Bob")
network.add_friendship("Alice", "Charlie")
network.add_friendship("Bob", "David")
network.add_friendship("Charlie", "David")

network.display()
network.show_friends("Alice")

