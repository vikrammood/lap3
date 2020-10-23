from tkinter import*
from tkinter import filedialog
import numpy as np 
from tkinter import ttk
import matplotlib.pyplot as plt
root=Tk()

root.title("Software")
root.geometry("500x750")

def open_text():
    text_file = filedialog.askopenfilename(initialdir='/home/medch',title="open text file")
    text_file =open(text_file,'r')
    stuff=text_file.read()
    my_text.insert(END,stuff)

    text_file.close()
    
def save_text():
    text_file = filedialog.askopenfilename(initialdir='/home/medch',title="open text file")
    text_file=open(text_file,'w')
    text_file.write(my_text.get(1.0,END))

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

def count_lines():
    text_file = filedialog.askopenfilename(initialdir='/home/medch',title="open text file")
    text_file =open(text_file,'r')
    stuff=text_file.read()
    answer=0
    CoList = stuff.split("\n") 
    for i in CoList:
        if i:
            answer +=1
    
    cw=countWords(stuff)
    
    fmc=findMostCommon(cw)
    words = len(stuff.split())
    
    Entry.insert(E4,0,answer)
    print(answer)
    Entry.insert(E5,0,str(words))
    print(str(words))
    Entry.insert(E6,0,str(fmc))
    print(str(fmc))
   
    
def plotHist():
    text_file = filedialog.askopenfilename(initialdir='/home/medch',title="open text file")
    text_file =open(text_file,'r')
    stuff=text_file.read()     
    labels,counts = np.unique(stuff.split(),return_counts=True)
    ticks = range(len(counts))
    plt.bar(ticks,counts,align='center')
    plt.xticks(ticks,labels)
    plt.show()







my_text=Text(root,width=20,height=20)
my_text.pack(pady=20)

L4 = Label(root, text="no of lines")
L4.pack(pady=5)
E4 = Entry(root, bd =5)
E4.pack(pady=5)
L5 = Label(root, text="no of words")
L5.pack(pady=5)
E5 = Entry(root, bd =5)
E5.pack(pady=5)
L4 = Label(root, text="most frequent words")
L4.pack(pady=5)
E6 = Entry(root, bd =5)
E6.pack(pady=5)

open_button=Button(root,text="open text file",command=open_text)
open_button.pack(pady=5)
save_button=Button(root,text="save file",command=save_text)
save_button.pack(pady=5)

B=Button(root, text ="Submit",command = lambda:[count_lines()])
B.pack(pady=5)
plotButton = ttk.Button(root, text="Plot Histogram", command=plotHist)
plotButton.pack()
root.mainloop()
