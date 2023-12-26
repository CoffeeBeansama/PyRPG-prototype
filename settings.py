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
