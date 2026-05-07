from abc import ABC, abstractmethod


class Unit(ABC):
    """Базовый класс для всех существ"""
    def __init__(
            self, strength, dexterity, constitution, wisdom,
            intelligence, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    @abstractmethod
    def calculate_max_health(self):
        """Общий метод, возвращающий значение здоровья."""
        pass

    @abstractmethod
    def calculate_damage(self):
        """Общий метод, возвращающий значение урона."""        
        pass

    @abstractmethod
    def calculate_defense(self):
        """Общий метод, возвращающий значение защиты."""        
        pass


class Character(Unit):
    """Класс для характеристик персонажей"""
    def __init__(
            self, strength, dexterity, constitution, wisdom,
            intelligence, charisma):
        super().__init__(
                self, strength, dexterity, constitution, wisdom,
                intelligence, charisma)

    def calculate_max_health(self):
        """Метод, возвращающий максимальное здоровье персонажа."""
        return int((constitution * 10) + strength / 2)

    def calculate_damage(self):
        """Метод, возвращающий получаемый урон от персонажа."""
        return int((strength * 1.5) + dexterity / 4)

    def calculate_defense(self):
        """Метод, возвращающий защиту персонажа."""
        return int((constitution * 1.5) + dexterity / 3)


class Monster(Unit):
    """Класс для характеристик монстров"""    
    def __init__(
            self, strength, dexterity, constitution, wisdom,
            intelligence, charisma):
        super().__init__(
                self, strength, dexterity, constitution, wisdom,
                intelligence, charisma)

    def calculate_max_health(self):
        """Метод, возвращающий максимальное здоровье монстра."""
        return int((constitution * 8) + strength / 3)

    def calculate_damage(self):
        """Метод, возвращающий получаемый урон от монстра."""
        return int((strength * 2) + constitution / 5)

    def calculate_defense(self):
        """Метод, возвращающий защиту монстра."""
        return int((constitution * 1) + (0.2 + (strength / 5)))