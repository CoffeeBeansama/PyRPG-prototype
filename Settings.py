WIDTH    = 800
HEIGTH   = 600
FPS      = 60
TILESIZE = 64

#UI elements
Bar_height = 20
Healthbar_width = 200
Manabar_width = 140
Itembox_size = 80
UI_font = "Graphics/font/joystix.ttf"
UI_fontsize = 25

#general colors
Water_Color = "#71ddee"
UI_bgcolor = "#222222"
UI_bordercolor = "#111111"
Text_color = "#EEEEEE"

#upgrade ui
Textcolor_selected = "#111111"
Bar_color = '#EEEEEE'
Bar_colorselected = "#111111"
Upgrade_bgcolor_selected = "#EEEEEE"


#ui colors
Health_color = "red"
Mana_color = "blue"
UI_bordercolor_active = "gold"


#weapon
weapon_data = {

"sword" : {"cooldown": 100, "damage": 15, "graphics": "Graphics/weapons/sword/full.png"},

"lance" : {"cooldown": 400, "damage": 30, "graphics": "Graphics/weapons/lance/full.png"},

"axe" : {"cooldown": 300, "damage": 20, "graphics": "Graphics/weapons/axe/full.png"},

"rapier" : {"cooldown": 50, "damage": 8, "graphics": "Graphics/weapons/rapier/full.png"},
"sai" : {"cooldown": 80, "damage": 10, "graphics": "Graphics/weapons/sai/full.png"}

}
#magic
magic_data = {

"flame" : { 'strength': 5, 'mana_cost': 20, 'graphic': 'Graphics/particles/flame/fire.png'},
"heal" : { "strength": 20, "mana_cost": 10, 'graphic': 'Graphics/particles/heal/heal.png' }

}

#enemy info

enemy_data = {

'squid' : {"health": 100, 'exp': 100, 'damage': 20, 'attack_type': "slash", "attack_sfx" : "audio/attack/slash.wav",'speed': 6,'knockback': 3, 'attack_radius': 80, "patrol_radius": 360 },

'raccoon' : {"health": 500, 'exp': 250, 'damage': 40, 'attack_type': "claw", "attack_sfx" : "audio/attack/claw.wav",'speed': 4,'knockback': 2, 'attack_radius': 120, "patrol_radius": 400 },

'spirit' : {"health": 100, 'exp': 110, 'damage': 8, 'attack_type': "thunder", "attack_sfx" : "audio/attack/fireball.wav",'speed': 8,'knockback': 3, 'attack_radius': 60, "patrol_radius": 350 },

'bamboo' : {"health": 70, 'exp': 100, 'damage': 6, 'attack_type': "leaf_attack", "attack_sfx" : "audio/attack/slash.wav",'speed': 6,'knockback': 3, 'attack_radius': 50, "patrol_radius": 300 }


}



 
