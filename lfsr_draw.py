# All of the paremeters used for drawing
# Note that the paremeters are not dependend of each other so that this gives flexibility
# For example: youu are free to make thicker lines or smaller boxes

#The Border Size around the figure in cm
borderSize = 1

#All lines, including the boxes
lineWidth = "0.1"
#Circles tend to seem smaller, you may want to increase it
cirleLineWidth = "0.12"
#Some likes bigger arrowHead
arrowHead = "0.5"

#Size of the LFSR box cm
boxSize = 4
#box Color use Tikz format
boxColor = "{{rgb:black,1;white,5}}"

#used for the distance of the box variable names 
boxBelowTextDistance = 6

#size of the x-or drawing cm
xorSize = 1

# How for the Xor's must be printed
xorDistance = boxSize/2

#For the lables. Not working properly
fontSize = 100

#Set True if you want the LFSR is filled with initial values.
drawInitValues = True

#Set True if you want the LFSR's box names are written under.
printBoxNames = True

#strating position of the first box.
x = 25
y = 20

#Determines how far left does the feedback line go
lefFeedbackDestance = 2 * boxSize

#Latex preample for standalone Tikz
def printPreample():
     print('\\documentclass[convert={{density=300,size=1080x800,outext=.png}},tikz, border={0}cm]{{standalone}}'.format(borderSize))
     #print("\\usepackage[left=1.5in,top=1.5in,right=1.5in,bottom=1.5in]{geometry}")
     print("\\usepackage{xcolor}")
     print("\\usetikzlibrary{arrows.meta,backgrounds}")
     print("\\tikzset{{white background/.style={{show background rectangle,tight background,background rectangle/.style={{fill=white}} }} }}")
#     print("\\tikzset{mynode/.style={draw, fill={{rgb:black,1;white,5}}, minimum size=4cm,line width=0.1cm,font=\fontsize{100}{100}\selectfont, label={[yshift=-6cm,style={font=\fontsize{100}{100} } ] {#1} } }}")
     print("")
     print("\\begin{document}")
     print("\\begin{tikzpicture}[white background]\n\n")

#Latex end
def printPrologue():
     print("\n\\end{tikzpicture}")
     print("\\end{document}")
     
#Prints the LFSr Boxes if printBoxNames==True then the values are printed,too
def printSquare(x1,y1,value, index):
    
    print('%node {0}'.format(index))
    
    if printBoxNames == True:
        print('\t\draw node[draw, fill={7}, minimum size={3}cm,line width={4}cm,font=\\fontsize{{{5}}}{{{5}}}\selectfont, label={{[yshift=-{8}cm,style={{font=\\fontsize{{{5}}}{{{5}}} }} ] {{$x_{6}$}} }} ] at ({0}, {1}) {{{2}}};'.format(x1,y1,value,boxSize,lineWidth,fontSize,index,boxColor,boxBelowTextDistance))
    else:
        print('\t\draw node[draw, fill={6}, minimum size={3}cm,line width={4}cm,font=\\fontsize{{{5}}}{{{5}}}\selectfont] at ({0}, {1}) {{{2}}};'.format(x1,y1,value,boxSize,lineWidth,fontSize,boxColor))
    
    #print('\draw [line width={4}]({0},{1}) -- ({2},{1}) -- ({2},{3}) -- ({0},{3}) -- cycle;'.format(x1,y1,x1+size,y1+size,lineWidth))
    
#def printSquareWithNoLeftSide(x1,y1,size):
    
    #print('\draw [line width={4}]({0},{1}) -- ({2},{1}) -- ({2},{3}) -- ({0},{3});'.format(x1,y1,x1+size,y1+size,lineWidth))
 
#The arrow from a box to x-or if it is a tap point. 
def printTapLine(x1,y1,length, arrow=False):
    if arrow:
        print('\t\draw [arrows={{-Triangle[angle=90:{5}cm,black,fill=black,line width={4}cm]}},line width={4}cm]({0},{1}) -- ({2},{3});'.format(x1,y1,x1,y1+length,lineWidth,arrowHead))
    else:
        print('\t\draw [line width={4}cm]({0},{1}) -- ({2},{3});'.format(x1,y1,x1,y1+length,lineWidth))
        
def printArrow(x1,y1):
    print('\t\draw [arrows={{-Triangle[angle=90:{5}cm,black,fill=black,line width={4}cm]}}]({0},{1}) -- ({2},{3});'.format(x1,y1,x1-0.0001,y1,lineWidth,arrowHead))
    
def printXor(x1,y1):
    print('\t\\draw [line width={3}cm] ({0},{1}) circle ({2});'.format(x1,y1,xorSize,cirleLineWidth))
    
    lx1 = x1
    lx2 = x1
    ly1 = y1-xorSize
    ly2 = y1+xorSize
    
    print('\t\draw [line width={4}cm]({0},{1}) -- ({2},{3});'.format(lx1,ly1,lx2,ly2,cirleLineWidth))
    
    lx1 = x1 - xorSize
    lx2 = x1 + xorSize
    ly1 = y1
    ly2 = y1
    
    print('\t\draw [line width={4}cm]({0},{1}) -- ({2},{3});'.format(lx1,ly1,lx2,ly2,cirleLineWidth))

### Combine this with the below into a path.    
#def printTopLine(x1,y1,x2):
    #print('\draw [line width={3}cm]({0},{1}) -- ({2},{1});'.format(x1,y1,x2,lineWidth))
    
###This needs path. 
#def printFeedbackArrow(x1,y1,x2,y2):
    #print('\draw [line width={4}cm]({0},{1}) -- ({2},{3});'.format(x1,y1,x1,y2,lineWidth))
    #print('\draw [arrows={{-Triangle[angle=90:{5}cm,black,fill=black,line width={4}cm]}}, line width={4}cm]({0},{1}) -- ({2},{3});'.format(x1,y2,x2,y2,lineWidth,arrowHead))
    
    ##\draw[->,line width=0.1cm,arrows={-Triangle[angle=90:0.5cm,black,fill=black,line width=0.1cm]}] (49,16.0) -- (-5,16.0) -- (-5,10) -- (2.5,10);

def printToplineAndFeedbackArrow(x1, x2, x3, y1, y2):
    print('\draw[->,line width=0.1cm,arrows={{-Triangle[angle=90:{6}cm,black,fill=black,line width={5}cm]}}] ({0},{3}) -- ({1},{3}) -- ({1},{4}) -- ({2},{4});'.format(x1, x2, x3, y1, y2,lineWidth,arrowHead))

def printOutputArrow(x1, x2, y1,value):
    print('\draw[->,line width=0.1cm,arrows={{-Triangle[angle=90:{4}cm,black,fill=black,line width={3}cm]}},font=\\fontsize{{{5}}}{{{5}}}\selectfont] ({0},{2}) -- ({1},{2}) node[midway,above]{{{6}}};'.format(x1, x2, y1, lineWidth,arrowHead, fontSize, value))
    
def printFeedBackPolynomial(lfsr):
    count = lfsr.count(1)
    feedBackPolynomail ="The Feedback Polynomial is $ f(x) = x^{{" + str(len(lfsr)) + "}}+" 

    for i, val in enumerate(lfsr):
        if val == 1:
            if len(lfsr) - i -1 == 0:
                feedBackPolynomail += "1"
            else:
                feedBackPolynomail += "x^" + str(len(lfsr) - i -1)
            if count > 1:
                feedBackPolynomail += "+"
            count = count -1
            
    feedBackPolynomail += "$"    

    feedBackPolynomailX = x+ (boxSize* (len(lfsr))) / 2
    feedBackPolynomailY = y - boxSize * 1.5

    print('\draw node[minimum size={3}cm,line width={4}cm,font=\\fontsize{{{5}}}{{{5}}}\selectfont] at ({0}, {1}) {{{6}}};'.format(feedBackPolynomailX,feedBackPolynomailY,feedBackPolynomail,boxSize,lineWidth,fontSize,feedBackPolynomail))

###############################
#  Now definition of the LFSR
###############################


#The taps. left most is the x_0 
lfsrTaps = [1,0,0,1,0,1,0,1,0,1]

#The inits. left most is the value of x_0 
initVals = [1,0,1,0,1,1,1,0,0,0]

#We need this inorder to draw the feedback properly
lastTapPos = 0

#Latex starts
printPreample()

count = lfsrTaps.count(1)

for i, val in enumerate(lfsrTaps):
    
    if drawInitValues == True:
        printSquare(x + i * boxSize, y , val,len(lfsrTaps) - i -1)
    else:
        printSquare(x + i * boxSize, y , "",len(lfsrTaps) - i -1)
            
        
    if val == 1:
        if i == len(lfsrTaps)-1:
            
            printTapLine(x + i * boxSize,y + boxSize/2, xorDistance + xorSize )
        else:
            printTapLine(x + i * boxSize,y + boxSize/2, xorDistance)
            printXor    (x + i * boxSize, y + boxSize/2 + xorDistance + xorSize )
            if count > 1:
                printArrow(x + i * boxSize + xorSize, y + boxSize/2 + xorDistance + xorSize)

        count = count -1            
        
        lastTapPos = i

printToplineAndFeedbackArrow(x + (lastTapPos )* boxSize ,          #x1
                             x - lefFeedbackDestance,                       #x2
                             x - boxSize /2,                                #x3
                             y + boxSize/2 + xorDistance + xorSize,         #y1
                             y                                              #y2
                            )

printOutputArrow(x + (len(lfsrTaps) -1) * boxSize + boxSize/2, x + (len(lfsrTaps) -1) * boxSize + 2 * boxSize, y, lfsrTaps[0]) 

#print('\draw node[minimum size={0}cm,line width={1}cm,font=\\fontsize{{{2}}}{{{2}}}\selectfont] at ({3}, {4}) {{{5}}};'.format(boxSize,lineWidth,fontSize,x,y,value))

#print('\draw node[minimum size={0}cm,line width={1}cm,font=\\fontsize{{{2}}}{{{2}}}\selectfont] at ({3}, {4}) {{{5}}};'.format(boxSize,lineWidth,fontSize,(len(lfsrTaps) -1) * boxSize + 2 * boxSize,y+boxSize/2,"1"))

###############################
###Feed Back Polynomail Part
###############################

printFeedBackPolynomial(lfsrTaps)

#Latex Ends
printPrologue()
         

     #278397
     #272258
  