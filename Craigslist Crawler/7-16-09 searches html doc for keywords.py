##os.chdir(r"C:\Documents and Settings\a\Desktop\ijobs")
##files = glob.glob(r"C:\Documents and Settings\a\Desktop\ijobs\*.html")
##for x in files:
##    filename = os.path.basename(x)
##    html = open(filename,'r')
##    text = html.read()
##    html.close()
##    text = text.lower()
##    if 'python' in text and '.net' in text:
##        newfilename = r'C:\Documents and Settings\a\Desktop\hits\\'+filename
##        open(newfilename,'w').write(text)
##        print 'file copied'
##print 'finished'

"""
this module takes a url then parses out all hyperlinks
"""
import sgmllib

class MyParser(sgmllib.SGMLParser):
    "A simple parser class."

    def parse(self, s):
        "Parse the given string 's'."
        self.feed(s)
        self.close()

    def __init__(self, verbose=0):
        "Initialise an object, passing 'verbose' to the superclass."

        sgmllib.SGMLParser.__init__(self, verbose)
        self.hyperlinks = []

    def start_a(self, attributes):
        "Process a hyperlink and its 'attributes'."

        for name, value in attributes:
            if name == "href":
                self.hyperlinks.append(value)

    def get_hyperlinks(self):
        "Return the list of hyperlinks."

        return self.hyperlinks

import urllib, os

link=[]
holder_list=[]
counter = 0
counter2 = 0
f = urllib.urlopen("http://geo.craigslist.org/iso/us")
s = f.read()
myparser = MyParser()
myparser.parse(s)

# Get the hyperlinks.
for x in myparser.get_hyperlinks():#cycle through list of urls
    if x == r'http://www.craigslist.org/':
        continue
    if x == r'http://en.wikipedia.org/wiki/united_states':
        continue
    if x == r'http://forums.craigslist.org/?forumID=1':
        continue


    url_base = x
    software_section = urllib.urlopen(x+'sof').read()#software jobs section of CL
    #parse the links out of the software section
    myparser2 = MyParser()
    myparser2.parse(software_section)#now i can run a get_hyperlinks call on it


    for x in myparser2.get_hyperlinks():#list of urls and other data but now i need to filter out the usabe urls
        if x.startswith('/') and len(x)>9:
            holder_list.append(x)#list of usable url's (strings)
    print 'openning pages from software section.'


    for x in holder_list:

        if not x.endswith('l'):#filters out pages that dont end with '.html'
            continue

        individual_ad = urllib.urlopen(url_base+x).read()
        ia = individual_ad.lower()
        file_dir = r'C:\Documents and Settings\a\Desktop\tester'
        os.chdir(file_dir)#this is where files that match will be stored

        if 'sql' in ia:
            print 'Match found, writing file.'
            temp = open(file_dir+'\\'+str(counter)+'.html','w').write(individual_ad)#this write the file that is unaffected by the lower function
            counter += 1
        counter2 += 1

        if counter2 == 20:
            break
            
        
        

        
    break        
      

