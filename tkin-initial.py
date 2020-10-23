#tkinter- GUI library for python
from tkinter import*    #importing everything from tkinter
from tkinter import filedialog
import numpy as np 
from tkinter import ttk #used for styling
import matplotlib.pyplot as plt
#creating tkinter window
root=Tk()

root.title("Software")
# creating fixed geometry of the tkinter window with dimensions 500x750
#.geometry("window width x window height + position right + position down")
root.geometry("500x750+2000+100")

def open_text():
    text_file = filedialog.askopenfilename(initialdir='/home/medch',title="open text file",filetypes=(("text files","*.txt"),("all files","*.*")))
    text_file =open(text_file,'r')
    stuff=text_file.read()
    my_text.insert(END,stuff)   #.insert(index, element)

    text_file.close()
    
def save_text():
    text_file = filedialog.askopenfilename(initialdir='/home/medch',title="open text file",filetypes=(("text files","*.txt"),("all files","*.*")))
    text_file=open(text_file,'w')
    text_file.write(my_text.get(1.0,END))   #.get(keyname, value)
#value is Optional. A value to return if the specified key does not exist.Default value None
    
def countWords(lines):
  wordDict = {}
  for line in lines:
    wordList = lines.split()
    for word in wordList:
      if word in wordDict: wordDict[word] += 1
      else: wordDict[word] = 1
  return wordDict
    
def findMostCommon(charDict):
  mostFreq = ''
  mostFreqCount = 0
  for k in charDict:
    if charDict[k] > mostFreqCount:
      mostFreqCount = charDict[k]
      mostFreq = k
  return mostFreq

def freq_word(word, wordDict):
    
    c=0
    if word in wordDict:
    	c=wordDict[word]
    return c

def count_lines():
    text_file = filedialog.askopenfilename(initialdir='/home/medch',title="open text file",filetypes=(("text files","*.txt"),("all files","*.*")))
    text_file =open(text_file,'r')
    stuff=text_file.read()
    answer=0
    CoList = stuff.split("\n") 
    for i in CoList:
        if i:
            answer +=1
    
    cw=countWords(stuff)
    
    fmc=findMostCommon(cw)
    words = len(stuff.split())  #default separator is any whitespace
    
    word=Entry.get(E8)
    f=freq_word(str(word),cw)
    
    Entry.insert(E4,0,answer)
    print(answer)
    Entry.insert(E5,0,str(words))
    print(str(words))
    Entry.insert(E6,0,str(fmc))
    print(str(fmc))
    Entry.insert(E7,0,str(f/72))
    print(str(f/72))
   
    
def plotHist():
    text_file = filedialog.askopenfilename(initialdir='/home/medch',title="open text file",filetypes=(("text files","*.txt"),("all files","*.*")))
    text_file =open(text_file,'r')
    stuff=text_file.read()  
    # Get a tuple of unique values and their frequency in numpy array
    labels,counts = np.unique(stuff.split(),return_counts=True)
    ticks = range(len(counts))
    plt.bar(ticks,counts,align='center')
    plt.xticks(ticks,labels)
    plt.show()






#The Text widget is used to display text in multiple lines.
my_text=Text(root,width=20,height=20)
"""pack is a geometry manager which organizes widgets in blocks before placing them in the parent widget."""
my_text.pack(pady=20)

L4 = Label(root, text="no of lines")
L4.pack(pady=5) #pady = External padding. Default is 0.
E4 = Entry(root, bd =5) #An Entry widget gets text input from the user.
E4.pack(pady=5)
L5 = Label(root, text="no of words")
L5.pack(pady=5)
E5 = Entry(root, bd =5)
E5.pack(pady=5)
L4 = Label(root, text="most frequent words")
L4.pack(pady=5)
E6 = Entry(root, bd =5)
E6.pack(pady=5)
w=Label(root, text="which words freq?")
w.pack(pady=5)
E8 = Entry(root, bd =5)
E8.pack(pady=5)
L4 = Label(root, text="words freq is:")
L4.pack(pady=5)
E7 = Entry(root, bd =5)
E7.pack(pady=5)


#The Button widget is used to display buttons in your application.
open_button=Button(root,text="open text file",command=open_text)
open_button.pack(pady=5)
save_button=Button(root,text="save file",command=save_text)
save_button.pack(pady=5)

B=Button(root, text ="Submit",command = lambda:[count_lines()])
B.pack(pady=5)
plotButton = ttk.Button(root, text="Plot Histogram", command=plotHist)
plotButton.pack()
root.mainloop()
