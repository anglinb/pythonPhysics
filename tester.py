length = 1
mega_points = [
[ [0,length]      ,[length,length] ,[length,0]      ,[0,0]],
[ [length,length] ,[length,0]      ,[0,0]           ,[0,length]],
[ [length,0]      ,[0,0]           ,[0,length]      ,[length,length]],
[ [0,0]           ,[0,length]      ,[length,length] ,[length,0]]
]

print mega_points[2]
print mega_points[2].pop(0)
