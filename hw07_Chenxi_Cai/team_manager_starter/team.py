from player import Player


class Team:
    """A class representing a dodgeball team"""
    # All methods in Python include arguments representing the object
    # itself. In the method definition, this is represented by the
    # `self` parameter.
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    # Another example of self. The method call only passes one argument,
    # the 'name; value. But the method definition must always include the
    # self parameter.
    def set_team_name(self, name):
        # TODO: set the team name
        self.name = name

    # Note again that `self` is the first parameter.
    def add_player(self, player_name, player_number, player_position):
        # TODO: call the Player class constructor with the appropriate
        # values to create a new player object, then add that
        # player object to the team's players list.
        new_player = Player(player_name, player_number, player_position)
        self.players.append(new_player)

    def cut_player(self, player_name):
        # TODO: Remove the player with the name player_name
        # from the players list.
        for i in range(len(self.players)):
            if self.players[i].name == player_name:
                self.players.pop(i)
                return
        else:
            print(player_name, "isn't on the team.")

    def is_position_filled(self, position):
        # TODO: Write the method that checks whether
        # there is currently at least one player on the team
        # occupying the requested position
        for player in self.players:
            if player.pos == position:
                print("Yes, the", position, "position is filled")
                return
        else:
            print("No, the", position, "position is not filled")

    # TODO: Write any necessary methods to support the methods
    # above, and write the method that will display (print to screen)
    # the full team roster in the following format:

    #    The lineup for Seattle Scorpions is:
    #    15       Garcia          catcher
    #    55       Wiggins         corner
    #    99       McCann          sniper
    def show_roster(self):
        if len(self.players) == 0:
            print("The team currently has no players")
        else:
            for player in self.players:
                print("%-10s%-10s%-15s"
                      % (player.num, player.name, player.pos))
