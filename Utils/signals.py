from enum import Enum


class Item(Enum):
    WHIP = 1
    DAGGER = 2
    NONE = 3
class TargetType(Enum):
    ENEMY = 1
    PLAYER = 2
    ALL_SPRITES = 3
    NONE= 4

class DamageMessage():
    def __init__(self, damage:int, ObjType:TargetType) -> None:
        self.damage = damage
        self.target = ObjType

    
    
class InventoryMessage():
    def __init__(self, equip:Item, ObjType:TargetType) -> None:
        self.item = equip
        self.target = ObjType