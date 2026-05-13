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
        self.spells = []
        self.mana = 0

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

    @abstractmethod
    def calculate_max_mana(self):
        """Общий метод, возвращающий максимальное количество маны."""
        pass

    def add_spell(self, spell):
        """Добавляет заклинание в список."""
        self.spells.append(spell)

    def cast_spell(self, index):
        """
        Применяет заклинание по индексу.
        Проверяет, достаточно ли маны.
        """
        if index < 0 or index >= len(self.spells):
            raise IndexError("Некорректный индекс заклинания")

        spell = self.spells[index]

        if self.mana < spell.mana_cost:
            raise ValueError(
                f"Недостаточно маны. Требуется: {spell.mana_cost}, "
                f"доступно: {self.mana}"
            )

        self.mana -= spell.mana_cost
        return spell.cast()


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
        self.mana = self.calculate_max_mana()

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

    def calculate_max_mana(self):
        """
        Расчёт максимальной маны в зависимости от класса персонажа.
        Воин: интеллект + сила / 2
        Маг: интеллект * 3 + мудрость
        Охотник: ловкость * 1.5 + мудрость / 2
        Округление в меньшую сторону.
        """
        if self.character_class == 'warrior':
            return int(self.intelligence + self.strength / 2)
        elif self.character_class == 'mage':
            return int((self.intelligence * 3) + self.wisdom)
        elif self.character_class == 'hunter':
            return int((self.dexterity * 1.5) + self.wisdom / 2)
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

    def calculate_max_mana(self):
        """Монстры не используют ману."""
        return 0


class Spell(ABC):
    """Абстрактный класс для заклинаний"""

    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self):
        """Возвращает урон от заклинания."""
        pass


class Fireball(Spell):
    """Заклинание Огненный шар"""

    def __init__(self):
        super().__init__("Огненный шар", 35, 15)

    def cast(self):
        """Возвращает урон огненного шара."""
        return self.damage


class IceLance(Spell):
    """Заклинание Ледяное копьё"""

    def __init__(self):
        super().__init__("Ледяное копьё", 25, 10)

    def cast(self):
        """Возвращает урон ледяного копья."""
        return self.damage


class LightningBolt(Spell):
    """Заклинание Удар молнии"""

    def __init__(self):
        super().__init__("Удар молнии", 40, 20)

    def cast(self):
        """Возвращает урон удара молнии."""
        return self.damage