#Sagar Laud and Alex O'Connor
#We worked on the homework assignment alone, using only this semester's course materials and collaborated with Karan Pahawa.
#slaud3@mail.gatech.edu
from myro import *
initialize()


def light():
    
    aList=['0','1','2','3','4','5','6','7','8']
    bList=[]
    for x in aList:
        p=takePicture()
        light=getLight()
        wait(.5)  
        avg=(light[0]+light[1]+light[2])/3.0
        average=str(avg)
        bList.append(average)
	turnRight(1,1)
        savePicture(p,('pic'+x+'.gif'))
	show(p)
    
    a=getName()
    a=str(a)
    B= '<br/> These pictures were taken by: '

    myFile=open("myPage.html", "w")
    Top="""
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title>A Robot's Photo Album</title></head>
    <body>
    <h1>Welcome to my Picture Page!</h1>
    This page was made by Sagar Laud

    <table>
    <tr>
       <td><img src = "pic0.gif" alt="pic0.gif"></td><td><img src = "pic1.gif" alt="pic1.gif"></td><td><img src = "pic2.gif" alt="pic2.gif"></td>
    </tr><tr>"""

    value1="<td>"+bList[0]+"</td>"
    value2="<td>"+bList[1]+"</td>"
    value3="<td>"+bList[2]+"</td>"
    value4="<td>"+bList[3]+"</td>"
    value5="<td>"+bList[4]+"</td>"
    value6="<td>"+bList[5]+"</td>"
    value7="<tr><td>"+bList[6]+"</td>"
    value8="<td>"+bList[7]+"</td>"
    value9="<td>"+bList[8]+"</td>"

    row2="""
    </tr><tr>
       <td><img src = "pic3.gif" alt="pic3.gif"></td><td><img src = "pic4.gif" alt="pic4.gif"></td><td><img src = "pic5.gif" alt="pic5.gif"></td>
    </tr><tr>
        """
    
    row3="""
    </tr><tr>
       <td><img src = "pic6.gif" alt="pic6.gif"></td><td><img src = "pic7.gif" alt="pic7.gif"></td><td><img src = "pic8.gif" alt="pic8.gif"></td>
    </tr>
    """
    endTable="</tr></table>"

    myFile.write(Top)
    myFile.write(value1)
    myFile.write(value2)
    myFile.write(value3)
    myFile.write(row2)
    myFile.write(value4)
    myFile.write(value5)
    myFile.write(value6)
    myFile.write(row3)
    myFile.write(value7)
    myFile.write(value8)
    myFile.write(value9)
    myFile.write(endTable)
    
    
    pageBottom=""" 
    </body>
    </html>"""
    myFile.write(B); myFile.write(a)
    myFile.write(pageBottom)
    myFile.close()
light()
