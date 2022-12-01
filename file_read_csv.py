my_file = 'Mappe1.csv'



m = []
with open(my_file, 'r') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        r =[]
        i += 1
        print(f'{i}: {line}', end='')
        for c in line.split(';'):
            #delete semi-colon in between
            #print(type(c))
            #print(c)
          #  r.append(int(c))
        #m.append(r)
            print(m)

#r.append = append to our r(array containing the row
#m.append () = row will be append to m (overall matrix)
#PROCESS S called PARCING a point


