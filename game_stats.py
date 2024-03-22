class Game_stats():
    def __init__(self,sett):
        self.sett = sett
        self.reset_stats()
        self.game_status = True
    def reset_stats(self):
        self.roc_left = self.sett.ship_limit 
