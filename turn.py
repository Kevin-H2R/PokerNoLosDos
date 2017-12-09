class Turn:
    def __init__(self, players, board, smallBlind, bigBlind):
        self.players = players
        self.board = board
        self.smallBlind = smallBlind
        self.bigBlind = bigBlind
        self.lastBet = bigBlind
        self.lastBettingPlayer = players[1]

    def run(self):
        self.players[0].bet(self.smallBlind)
        self.players[1].bet(self.bigBlind)
        playerIndex = 2
        decision = None
        while self.players[playerIndex] is not self.lastBettingPlayer:
            currentPlayer = self.players[playerIndex]
            decision = currentPlayer.decide(self.board, self.lastBet)
            playerIndex = (playerIndex + 1) % len(self.players)
            if (decision == -1):
                # flop
                # TODO: Remove player from loop
                continue
            if (decision > self.lastBet):
                self.lastBet = decision
                self.lastBettingPlayer = currentPlayer
            currentPlayer.bet(self.lastBet)
        if (len(self.players) > 1):
            potSum = 0
            for player in self.players:
                potSum += player.pot
            return potSum
        else:
            return -1
