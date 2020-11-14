def agent(observation, configuration):
    board = Board(observation, configuration)
    current_player = board.current_player
    for ship in current_player.ships:
        ship.next_action = ShipAction.NORTH
    return current_player.next_actions