word = set(input('plase enter a word'))
left_keyboard = set('QWERTYASDFGHZXCVBNqwertyasdfghzxcvbyhn')
right_keybord = set('UJMIKÖOLÇPŞĞİÜuıopğüjklşi.,möç')
if word == (left_keyboard & word) :
    print('False')

elif word == (right_keybord & word) :
    print('False')

else word == (right_keybord & left_keyboard & word) :
    print('True')