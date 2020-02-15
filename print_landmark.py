import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.font_manager import FontProperties 
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import keys
import landmark_coords

def get_erangel_pos(landmark):
  try:
    return landmark_coords.erangel[landmark]
  except:
    return False 

def get_miramar_pos(landmark):
  try:
    return landmark_coords.miramar[landmark]
  except:
    return False

def get_sanhok_pos(landmark):
  try:
    return landmark_coords.sanhok[landmark]
  except:
    return False
  

# Constant 
SHIFT = 10000

# GoogleSpreadSheet
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(keys.json_keyfile, scope)
gc = gspread.authorize(credentials)

# For Print Japanese
font_path = '/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

# Variable 
stack = []

# TeamList
roster_sheet = gc.open_by_key(keys.spreadsheetkey).worksheet('roster')
teams = roster_sheet.col_values(1)

# LandmarkList
landmark_sheet = gc.open_by_key(keys.spreadsheetkey).worksheet('landmark')
landmarks = landmark_sheet.get_all_values()
del landmarks[0]


# Erangel
fig = plt.figure(figsize=(18.00, 18.00), frameon=False, dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
img = mpimg.imread('maps/Erangel_Main_High_Res.png')
ax.imshow(img, extent=[0, 819200, 0, 819200])

for team in teams:
  for landmark in landmarks:
    if team == landmark[0]:
      if landmark[5] != '':
        pos = get_erangel_pos(landmark[5])
        if not pos:
          # dont match landmark.
          ax.text(1000, 1000 + (SHIFT*stack.count('no_landmark')), team + "(" + landmark[5] + ")", fontsize=16, color='yellow', weight='heavy')
          stack.append('no_landmark')

        else: 
          ax.text(pos['x'], pos['y'] - (SHIFT*stack.count(landmark[5])), team, fontsize=16, color='yellow', weight='heavy')
          stack.append(landmark[5])

          if landmark[6] != '':
            pos = get_erangel_pos(landmark[6])
            if not pos:
              # dont match landmark.
              ax.text(1000, 1000 + (SHIFT*stack.count('no_landmark')), team + "(" + landmark[6] + ")", fontsize=16, color='yellow', weight='heavy')
              stack.apend('no_landmark')

            else:
              ax.text(pos['x'], pos['y'] - (SHIFT*stack.count(landmark[6])), "(" + team + ")", fontsize=16, color='yellow', weight='heavy')
              stack.append(landmark[6])

      else:
        ax.text(1000, 1000 + (SHIFT*stack.count('no_landmark')), team, fontsize=16, color='yellow', weight='heavy')
        stack.append('no_landmark')


plt.savefig('erangel.png')
stack.clear()
fig.delaxes(ax)


# Miramer
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
img = mpimg.imread('maps/Miramar_Main_High_Res.png')
ax.imshow(img, extent=[0, 819200, 0, 819200])

for team in teams:
  for landmark in landmarks:
    if team == landmark[0]:
      if landmark[1] != '':
        pos = get_miramar_pos(landmark[1])
        if not pos:
          # dont match landmark.
          ax.text(1000, 1000 + (SHIFT*stack.count('no_landmark')), team + "(" + landmark[1] + ")", fontsize=16, color='yellow', weight='heavy')
          stack.append('no_landmark')
 
        else:
          ax.text(pos['x'], pos['y'] - (SHIFT*stack.count(landmark[1])), team, fontsize=16, color='yellow', weight='heavy')
          stack.append(landmark[1])

          if landmark[2] != '':
            pos = get_miramar_pos(landmark[2])
            if not pos:
              # dont match landmark.
              ax.text(1000, 1000 + (SHIFT*stack.count('no_landmark')), team + "(" + landmark[2] + ")", fontsize=16, color='yellow', weight='heavy')
              stack.append('no_landmark')

            else:
              ax.text(pos['x'], pos['y'] - (SHIFT*stack.count(landmark[2])), "(" + team + ")", fontsize=16, color='yellow', weight='heavy')
              stack.append(landmark[2]) 

      else:
        ax.text(1000, 1000 + (SHIFT*stack.count('no_landmark')), team, fontsize=16, color='yellow', weight='heavy')
        stack.append('no_landmark')


plt.savefig('miramar.png')
stack.clear()
fig.delaxes(ax)


# Sanhok
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
img = mpimg.imread('maps/Sanhok_Main_High_Res.png')
ax.imshow(img, extent=[0, 409600, 0, 409600])

for team in teams:
  for landmark in landmarks:
    if team == landmark[0]:
      if landmark[3] != '':
        pos = get_sanhok_pos(landmark[3])
        if not pos:
          # dont match landmark.
          ax.text(1000, 1000 + (SHIFT*stack.count('no_landmark')), team + "(" + landmark[3] + ")", fontsize=16, color='yellow', weight='heavy')
          stack.append('no_landmark')

        else: 
          ax.text(pos['x'], pos['y'] - (SHIFT*stack.count(landmark[3])), team, fontsize=16, color='yellow', weight='heavy')
          stack.append(landmark[3])

          if landmark[4] != '':
            pos = get_sanhok_pos(landmark[4])
            if not pos:
              # dont match landmark.
              ax.text(1000, 1000 + (SHIFT*stack.count('no_landmark')), team + "(" + landmark[4] + ")", fontsize=16, color='yellow', weight='heavy')
              stack.append('no_landmark')

            else:
             ax.text(pos['x'], pos['y'] - (SHIFT*stack.count(landmark[4])), "(" + team + ")", fontsize=16, color='yellow', weight='heavy')
             stack.append(landmark[4])
 
      else:
        ax.text(1000, 1000 + (SHIFT*stack.count('no_landmark')), team, fontsize=16, color='yellow', weight='heavy')
        stack.append('no_landmark')


plt.savefig('sanhok.png')
