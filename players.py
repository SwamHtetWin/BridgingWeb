players = ['charles','mike','eli','matrina','william']
print(players[0:3]) #star at index 0 and stops at index 3, therefore, answer is 0,1,2
print(players[:4])#skipping start index means it will use default start index 0 
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())