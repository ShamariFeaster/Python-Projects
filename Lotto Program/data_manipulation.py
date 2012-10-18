
#                              INTEGER PARSER
############################################################################
#parsing 'lotto' in a list of integers called 'h' which has lenght of 9,594

h=[]
h2=[]
for x in lotto:  
    for y in x.split():
        z = int(y)
        h.append(z)



#End parsing 'lotto' in a list of integers called 'h'
############################################################################


#                                TUPLE BUILDER
############################################################################
a = 0
a1 = 0                    
for x in h:         #this tests how many numbers appear from the 
    if x <= 27:     # 1st quadrant (1-27) & 2nd quadrant (28-53)
        a += 1
    if x >= 28:
        a1 += 1
    if (a + a1)%6 == 0:
        h2.append((a,a1))
        a,a1 = 0,0
############################################################################
