
# GAP code to generate input for this code
# (writes ~1.5GB file; takes several hours)
#
# P:=ProjectiveSpace(2,121);
# for l in List(Lines(P)) do
# linepoints:=[];
# for p in List(Points(P)) do
# Append(linepoints,[p in l]);
# od;
# AppendTo(PATH_TO_FILE_HERE,linepoints);
# od;

all_lines=[]
cur_line=[]

with open(PATH_TO_FILE_HERE, 'r') as f:
    while True:
        line_in = f.readline()
        if line_in == '':
            break
        else:
            line_in = line_in.replace('[',',')
            line_split = line_in.split(',')
            for pt in line_split:
                if 't' in pt:
                    cur_line.append(True)
                if 'f' in pt:
                    cur_line.append(False)
                if ']' in pt:
                    all_lines.append([i for i in range(len(cur_line)) if cur_line[i]])
                    cur_line = []



with open('C:/Users/paula/Documents/megamatch_121_cards.txt','w+') as f:
    f.writelines([','.join([str(n) for n in line_out])+'\n' for line_out in all_lines])





