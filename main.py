import cv2
import time
video_src = 'dataset/cars_on_highway (1080p).mp4'
#line a
ax1=70
ay=90
ax2=230
#line b
bx1=15
by=125
bx2=225

def Speed_Cal(time):
    try:
        Speed = (9.144*3600)/(time*1000)
        return Speed
    except ZeroDivisionError:
        print (5)

i = 1
start_time = time.time()
cap = cv2.VideoCapture(video_src)


while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    blurred = cv2.blur(img,ksize=(15,15))
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    
    cv2.line(img,(ax1,ay),(ax2,ay),(255,0,0),2)
    #line b
    cv2.line(img,(bx1,by),(bx2,by),(255,0,0),2)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.circle(img,(int((x+x+w)/2),int((y+y+h)/2)),1,(0,255,0),-1)

        while int(ay) == int((y+y+h)/2):
            start_time = time.time()
            break

        while int(ay) <= int((y+y+h)/2):
            if int(by) <= int((y+y+h)/2)&int(by+10) >= int((y+y+h)/2):
                cv2.line(img,(bx1,by),(bx2,by),(0,255,0),2)
                Speed = Speed_Cal(time.time() - start_time)
                print("Car Number "+str(i)+" Speed: "+str(Speed))
                i = i + 1
                cv2.putText(img, "Speed: "+str(Speed)+"KM/H", (x,y-15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3);
                break
            else :
                cv2.putText(img, "Calcuting", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),3)
                break


    cv2.imshow('video', img)

    if cv2.waitKey(33) == 27:
        break
cap.release()
cv2.destroyAllWindows()
