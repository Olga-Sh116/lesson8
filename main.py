from abc import ABC, abstractmethod

# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"

# Шаг 3: Модифицируйте класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon is None:
            return f"{self.name} не имеет оружия."
        return f"{self.name} {self.weapon.attack()}"

# Шаг 4: Реализация боя
class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        return f"Монстр {self.name} побежден!"

# Основная логика игры
if __name__ == "__main__":
    # Создание бойца и монстра
    fighter = Fighter("Боец")
    monster = Monster("Дракон")

    # Боец выбирает меч
    sword = Sword()
    fighter.changeWeapon(sword)
    print(fighter.attack())
    print(monster.defeat())

    # Боец выбирает лук
    bow = Bow()
    fighter.changeWeapon(bow)
    print(fighter.attack())
    print(monster.defeat())
