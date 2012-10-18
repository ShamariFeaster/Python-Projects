import pickle

counter = 0
nums = open('lotto numbers.txt','r')
nums2 = nums.readlines()
nums.close()





##This section filters the massive list down to parts with
##the winning numbers in it
nums3 = filter(lambda x: len(x)>=60, nums2)


##This filters out hyphin and escape characters
def numberfilter(nlist):
    h=[]
    h2=[]
    finNums = ''
    for x in nlist:
        if x != '\t':
            h.append(x)
    for x in h:
        if x == '-':
            h.remove(x)
    for x in h:
        if x =='\n':
            h.remove(x)
    for x in h:
        if x =='/':
            h.remove(x)
    h2=h[6:] #here i am slicing the string to remove the date of numbers
    if len(h2) <= 27:
        finNums =  ''.join(h2) #turning my list into a string
    return finNums

lotto = []

for x in nums3:
    lotto.append(numberfilter(x))

#created the list object 'lotto' which store the winning number hostory
#as strings. Next is exporting this object to a file

lottoStore = open('lottoFile','w') #creates pickling object
pickle.dump(lotto, lottoStore) #dumps contents og 'lotto' into 'lottoStore' file
lottoStore.close()



