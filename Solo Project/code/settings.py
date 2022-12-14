WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
    'player': -26,
    'object': -40,
    'grass': -10,
    'invisible': 0
}

#UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE  = 80
UI_FONT = 'graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

#general color
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

#UI COLOR
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

#weapon
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15,'graphics':'graphics/weapons/sword/full.png'},
    'scythe': {'cooldown': 400, 'damage': 30,'graphics':'graphics/weapons/scythe/full.png'},
    'axe': {'cooldown': 300, 'damage': 20,'graphics':'graphics/weapons/axe/full.png'},
    'stick': {'cooldown': 50, 'damage': 8,'graphics':'graphics/weapons/stick/full.png'},
    'sai': {'cooldown': 80, 'damage': 10,'graphics':'graphics/weapons/sai/full.png'}
}

# magic
magic_data = {
    'flame' : {'strength' : 100, 'cost' : 25, 'graphics':'graphics/particles/flame/fire.png'},
    'heal' : {'strength': 20, 'cost': 10, 'graphics':'graphics/particles/heal/heal.png'}
}

# enemy
monster_data = {
    'squid': {'health':350, 'exp':100, 'damage':15, 'attack_type': 'slash', 'attack_sound': 'audio/attack/slash.wav', 'speed' : 4, 'resistance': 2, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 2500, 'exp':200, 'damage':20, 'attack_type': 'claw', 'attack_sound': 'audio/attack/claw.wav', 'speed' : 7.5, 'resistance': 2, 'attack_radius': 220, 'notice_radius': 400},
    'spirit': {'health': 270, 'exp':110, 'damage':10, 'attack_type': 'thunder', 'attack_sound': 'audio/attack/fireball.wav', 'speed' : 7, 'resistance': 2, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 100, 'exp':120, 'damage':6, 'attack_type': 'leaf_attack', 'attack_sound': 'audio/attack/slash.wav', 'speed': 6, 'resistance': 1, 'attack_radius': 50, 'notice_radius': 300},
    'dragon': {'health': 3000, 'exp':120, 'damage':30, 'attack_type': 'flame', 'attack_sound': 'audio/attack/slash.wav', 'speed': 6, 'resistance': 2, 'attack_radius': 220, 'notice_radius': 300},
}
