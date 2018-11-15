

class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        # TODO: Initialize the bench object with whatever
        # attributes and values it will need
        self.player = []

    def send_to_bench(self, player_name):
        # TODO: Put the player "onto the bench"
        self.player.insert(0, player_name)

    def get_from_bench(self):
        # TODO: Return the name of the player who has
        # been on the bench longest.
        return(self.player.pop())

    # TODO: Write the function that will display the
    # current list of players on the bench
    def show_bench(self):
        if len(self.player) == 0:
            print("Empty bench.")
        else:
            for name in self.player:
                print(name)

    # TODO: Write any other methods that might be used
    # by the methods above.
