lines = []
with open('resource_sat_tles.txt','r') as f:
        lines = f.readlines()

print lines
titles = []
line1s = []
line2s = []
for i in range(0,len(lines),3):
    lines[i][:-2:]
    lines[i+1][:-2:]
    lines[i+2][:-2:]
    title = lines[i][:-2:].replace(' ','')
    with open(title + '_' + lines[i+1][18:23:1] + '.tle','w') as f:
        f.write(title+'\n')
        f.write(lines[i+1][:-2:] + '\n')
        f.write(lines[i+2][:-2:] + '\n')
