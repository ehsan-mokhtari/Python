#Ehsan Mokhtari
import numpy
import cv2

#creating our white 600*600 template
canvas = numpy.ones((600,600,3),dtype="uint8")*255
cv2.putText(canvas,"q=exit, w=reset, s=save, left-click=draw, right-click=erase",(12,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1,cv2.LINE_AA)
cv2.putText(canvas,"change color => b=black, l=blue, g=green, r=red, p=purple",(12,40),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1,cv2.LINE_AA)

#drawing and erasing boolean handlers
clicked,erase,texthandel = False,False,True
color = (0,0,0)

#handling clicks on the template
def click(event,point_x,point_y,flag,parameter):
    global canvas,clicked,erase,texthandel,color

    #when mouse is clicked for drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        if texthandel:
            #clearing text in stupid way :)
            canvas = numpy.ones((600,600,3),dtype="uint8")*255
            texthandel = False
        cv2.circle(canvas,(point_x,point_y),3,color,-1)
        erase=False
        clicked=True
    
    #when the mouse is clicked for erasing 
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(canvas,(point_x,point_y),4,(255,255,255),-1)
        erase=True
        clicked=False
    
    #when the mouse is drawing    
    elif event == cv2.EVENT_MOUSEMOVE and clicked:
        cv2.circle(canvas,(point_x,point_y),3,color,-1)
    
    #when the mouse is erasing    
    elif event == cv2.EVENT_MOUSEMOVE and erase:
        cv2.circle(canvas,(point_x,point_y),4,(255,255,255),-1) 
    
    #when the mouse stops drawing       
    elif event == cv2.EVENT_LBUTTONUP:
        clicked=False
    
    #finally when the mouse stops erasing    
    elif event == cv2.EVENT_RBUTTONUP:
        erase=False

cv2.namedWindow("drawing")
cv2.setMouseCallback("drawing",click)

while True:
    cv2.imshow("drawing",canvas)
    ch = cv2.waitKey(1)

    if ch & 0xFF == ord('r'):
        color = (0,0,255)
    if ch & 0xFF == ord('g'):
        color = (0,255,0)
    if ch & 0xFF == ord('b'):
        color = (0,0,0)
    if ch & 0xFF == ord('l'):
        color = (255,0,0)
    if ch & 0xFF == ord('p'):
        color = (255,0,255)                

    #press q for exit the panel
    if ch & 0xFF == ord('q'):
        break
    #press s for save
    if ch & 0xFF == ord('s'):
        cv2.imwrite("output.png",canvas)
    #press r for reset    
    if ch & 0xFF == ord('w'):
        texthandel = True
        canvas = numpy.ones((600,600,3),dtype="uint8")*255
        cv2.putText(canvas,"q=exit, w=reset, s=save, left-click=draw, right-click=erase",(12,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1,cv2.LINE_AA)
        cv2.putText(canvas,"change color => b=black, l=blue, g=green, r=red, p=purple",(12,40),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1,cv2.LINE_AA)
        

cv2.destroyAllWindows()
#done