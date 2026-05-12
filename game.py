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
    """Класс для персонажа с выбором игрового класса."""

    CLASSES = {'warrior', 'mage', 'hunter'}

    def __init__(
            self, strength, dexterity, constitution, wisdom,
            intelligence, charisma, character_class):
        super().__init__(
            strength, dexterity, constitution, wisdom,
            intelligence, charisma)

        if character_class == 'warrior' 
        or character_class == 'mage' 
        or character_class == 'hunter':
            self.character_class = character_class
        else:
            raise ValueError(
                f"Некорректный класс персонажа.
                 Допустимые значения: warrior, mage, hunter")

        self.character_class = character_class

        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self):
        """
        Формула для персонажа: телосложение * 10 + сила / 2
        Округление в меньшую сторону.
        """
        return int((self.constitution * 10) + self.strength / 2)

    def calculate_damage(self):
        """
        Расчёт урона в зависимости от класса персонажа.
        Воин: сила * 2.2 + телосложение / 3
        Маг: интеллект * 2.5 + мудрость / 2
        Охотник: ловкость * 1.9 + сила / 3
        Округление в меньшую сторону.
        """
        if self.character_class == 'warrior':
            return int((self.strength * 2.2) + self.constitution / 3)
        elif self.character_class == 'mage':
            return int((self.intelligence * 2.5) + self.wisdom / 2)
        elif self.character_class == 'hunter':
            return int((self.dexterity * 1.9) + self.strength / 3)
        else:
            return 0

    def calculate_defense(self):
        """
        Расчёт защиты в зависимости от класса персонажа.
        Воин: телосложение * 1.8 + сила / 4
        Маг: мудрость * 1.3 + интеллект / 6
        Охотник: ловкость * 1.6 + телосложение / 5
        Округление в меньшую сторону.
        """
        if self.character_class == 'warrior':
            return int((self.constitution * 1.8) + self.strength / 4)
        elif self.character_class == 'mage':
            return int((self.wisdom * 1.3) + self.intelligence / 6)
        elif self.character_class == 'hunter':
            return int((self.dexterity * 1.6) + self.constitution / 5)
        else:
            return 0


class Monster(Unit):
    """Класс для характеристик монстров"""

    def __init__(
            self, strength, dexterity, constitution, wisdom,
            intelligence, charisma):
        super().__init__(
            strength, dexterity, constitution, wisdom,
            intelligence, charisma)

    def calculate_max_health(self):
        """Метод, возвращающий максимальное здоровье монстра."""
        return int((self.constitution * 8) + self.strength / 3)

    def calculate_damage(self):
        """Метод, возвращающий получаемый урон от монстра."""
        return int((self.strength * 2) + self.constitution / 5)

    def calculate_defense(self):
        """Метод, возвращающий защиту монстра."""
        return int((self.constitution * 1.2) + self.strength / 5)