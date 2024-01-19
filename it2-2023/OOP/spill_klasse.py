class Character:
    def __init__(self, name, lvl=1, hp=100, mp=1200) -> None:
        self.name = name
        self.lvl = lvl
        self.MAX_HP = hp
        self.MAX_MP = mp
        self.init_hp = hp
        self.init_mp = mp
        self.hp = hp
        self.mp = mp
        self.is_alive = True if self.hp > 0 else False
        self.has_mp = True if self.mp > 0 else False

    def set_hp(self, delta):
        if self.hp + delta >= self.MAX_HP:
            self.hp = self.MAX_HP
        elif self.hp + delta <= 0:
            self.is_alive = False
        else:
            self.hp += delta

    def set_mp(self, delta):
        if self.mp + delta <= self.MAX_MP:
            self.mp = self.MAX_MP
        elif self.mp + delta <= 0:
            self.has_mp = False
        else:
            self.mp += delta

    def set_lvl(self, delta, has_died=False):
        if has_died:
            self.lvl = 1
            self.MAX_HP = self.init_hp
            self.MAX_MP = self.init_mp
        else:
            self.lvl += delta
            self.MAX_HP += 25 * self.lvl**2 if self.MAX_HP > 300 else 300
            self.MAX_HP += 100 * self.lvl**2 if self.MAX_MP > 2400 else 2400


Jacob = Character("Tjukken", "1", "200", "1400")
