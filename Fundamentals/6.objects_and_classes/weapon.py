class Weapon:
    def __init__(self,bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets <= 0:
            return 'no bullets left'
        self.bullets -= 1
        return 'shooting...'

    def __repr__(self):
        return f'Remaining bullets: {self.bullets}'
#You should also override the toString method, \
#so that the following code: print(weapon) should work. To do that define a __repr__ method


weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)