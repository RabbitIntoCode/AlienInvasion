class Settings():
    def __init__(self):
        self.screen_width=1500
        self.screen_height=800
        self.bg_color =(162,212,240)
        self.speed_fac =  6
        self.bullet_speed_fac =9
        self.alien_speed_fac = 2
        self.bullet_width =5
        self.bullet_height =15
        self.bullet_color = (134,60,60)
        self.fleet_drop_speed = 5
        self.ship_limit = 3
 # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1