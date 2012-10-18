import pickle

##l = open('lottoFile','r')
##lotto = pickle.load(l)




#                       SPECIFIC NUMBER OCCURANCE TESTER
############################################################################
# Cycles through DB file. This is specifically set up to deal with a list of
# strings. Each index is a hand.
#                            ONE

#'lotto' is a list of strings (each w/ 6 numbers)

a = lotto
b = range(1,54)
counter=0
tally=0
percent2 = float(95.94) #NEEDS TO BE GENERALIZED
for s in b:
    for t in a:    
        for u in t.split():
            if s == int(u):
                counter += 1
    print str(s)+' appears in string lotto '+str(counter)+' times.  '+str(float(counter)/percent2)+'%'
    tally +=counter #if tally == len(h): this count in functional
    counter = 0    
print
print


#End Specific number occurance test
############################################################################



#                     ESTABLISHES 1% OF TOTAL HANDS PLAYED
############################################################################
percent = float((len(h)/6.0))/float(100.0) #--> 1599 sets of winning numbers in 'h'
##print len(h)%6 #--> 0
############################################################################



#                 Testing occurance of generic high/low
############################################################################

        #DEPENDS ON TUPLE BUILDER

b = 0
b1 = 0
b2 = 0
for x,y in h2:
    if x == y:
        b += 1
    if x < y:
        b1 += 1
    if x > y:
        b2 += 1
print 'Occurances in Q1 & Q2 were equal '+str(b)+' times.' 
equal = b/percent
print str(equal)+'%'
print 'Occurances in Q1 were less than Q2 '+str(b1)+' times.'
less = b1/percent
print str(less)+'%'
print 'Occurances in Q1 were greater than Q2 '+str(b2)+' times.'
more = b2/percent
print str(more)+'%'

#End Testing occurance of generic high/low 
####################################################################




#         Testing occurance of specific high/low ratios
#####################################################################

#                          DEPENDS ON TUPLE BUILER

c = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
for x,y in h2:
    if x==0 and y==6 :
        c += 1
    if x==1 and y==5 : 
        c1 += 1
    if x==2 and y==4 :
        c2 += 1
    if x==3 and y==3 :
        c3 += 1
    if x==4 and y==2 :
        c4 += 1
    if x==5 and y==1 :
        c5 += 1
    if x==6 and y==0 :
        c6 += 1

print
print str(c)+'  (0,6)' 
print str(c/percent)+'%'
print str(c1)+'  (1,5)'
print str(c1/percent)+'%'
print str(c2)+'  (2,4)' 
print str(c2/percent)+'%'
print str(c3)+'  (3,3)' 
print str(c3/percent)+'%'
print str(c4)+'  (4,2)' 
print str(c4/percent)+'%'
print str(c5)+'  (5,1)'
print str(c5/percent)+'%'
print str(c6)+'  (6,0)'
print str(c6/percent)+'%'

#End Testing occurance of specific high/low ratios
##########################################################################






##l2 = open('lottoFile-Integers','w')
##l3 = open('lottoFile-Hi_Low Split Tuples','w')
##pickle.dump(h, l2)
##pickle.dump(h2, l3)
##l2.close()
##l3.close()
