from enum import Enum

class Item(Enum):
    WHIP = 1
    DAGGER = 2

class DamageMessage():
    def __init__(self, damage:int) -> None:
        self._damage = damage

    def get_damage(self):   
        return self._damage
    
class InventoryMessage():
    def __init__(self, equip:Item) -> None:
        self._item = equip

    def get_item(self):
        return self._item