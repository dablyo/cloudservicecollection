import cv2
import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk
import numpy as np

CAT=['angry','disgust','happy','sadness','surprise','fear','neutral']

class VideoCatch:
    def __init__(self, video_source=0,width=320,height=240):
        self.cap = cv2.VideoCapture(video_source)
        if not self.cap.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = width
        self.height = height
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,self.height)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,self.width)
        #self.callback = 

    def get_frame(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return (ret, frame)
            else:
                return (ret, None)
        else:
            return (ret, None)

    def __del__(self):
       if self.cap.isOpened():
           self.cap.release()

class fmeApp(object):
    def __init__(self):
        #GUI
        self.root = tk.Tk()
        self.var = tk.IntVar()
        #top frame
        self.frametop = tk.Frame(self.root, height=240, width=640)
        self.framebtm = tk.Frame(self.root, height=240, width=640)
        self.frametop.pack(side='top')
        self.framebtm.pack(side='bottom')
        
        self.scn = tk.Label(self.frametop,width=320) 	 	#top,left,screen
        self.scn.pack(side='left',fill='y')
        self.chart=tk.Label(self.frametop)
        self.chart.pack(expand='yes')
        #self.chart.pack(fill='both')
        self.btn = tk.Button(self.framebtm,text='quit',command=self.btnclick, width=100)
        self.btn.pack(side='left',fill='y')
        '''
        self.label_angry= tk.Label(self.framemsf_label,text='生气',height=2)
        self.label_disgust= tk.Label(self.framemsf_label,text='厌恶',height=2)
        self.label_happy= tk.Label(self.framemsf_label,text='高兴',height=2)
        self.label_sad  = tk.Label(self.framemsf_label,text='悲伤',height=2)
        self.label_surprise= tk.Label(self.framemsf_label,text='惊讶',height=2)
        self.label_fear= tk.Label(self.framemsf_label,text='害怕',height=2)
        '''
       
        self.cam = VideoCatch()


    def process(self):
        ret,frame = self.cam.get_frame()
        if ret:
            cv2img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA) 
            img = Image.fromarray(cv2img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.scn.imgtk = imgtk
            self.scn.config(image=imgtk)
            cv2imgc=np.ones((240,640,3),dtype=np.uint8)*255
            #cv2imgc = cv2.cvtColor(chartimg,cv2.COLOR_BGR2RGBA) 
            for i,c in enumerate(CAT):
                cv2.putText(cv2imgc,c,(10, 20+40*i),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
                cv2.rectangle(cv2imgc,(150,5+40*i),(300,5+40*i+20),(0,255,0),-1)
            imgc = Image.fromarray(cv2imgc)
            imgtkc = ImageTk.PhotoImage(image=imgc)
            self.chart.imgtk = imgtkc
            self.chart.config(image=imgtkc)
        self.root.after(50, self.process)

    def destructor(self):
        self.root.destroy()
        del self.cam
    def btnclick(self):
        self.cam.cap.release()
        self.root.quit() 

def main():
    app = fmeApp()
    app.process()
    app.root.mainloop()

if __name__ == '__main__':
    main()
