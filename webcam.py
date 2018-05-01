import cv2
import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk

class packlayout(object):
    def __init__(self):
        self.master = tk.Tk()
        self.var = tk.IntVar()
        #top frame
        self.frametop = tk.Frame(self.master, height=240, width=1024)
        self.framebtm = tk.Frame(self.master, height=240, width=1024)
        self.frametop.pack(expand='YES',fill='both')
        self.framebtm.pack(expand='YES',fill='both')
        
        self.scn = tk.Canvas(self.frametop,width=320) 	 	#top,left,screen
        self.scn.pack(side='left',fill='y')
        self.framemsf_label=tk.Frame(self.frametop,width=100)	#top,middle,label
        self.framemsf_label.pack(side='left')#fill='y')
        self.framemsf_bar=tk.Frame(self.frametop)		#top,right,bar chart
        self.framemsf_bar.pack()#fill='both')

        self.label_angry= tk.Label(self.framemsf_label,text='angry',height=2)
        self.label_angry.pack()#side='left',anchor='e')
        self.label_t1= tk.Label(self.framemsf_label,text='',height=1)
        self.label_t1.pack()#side='left',anchor='e')
        
        self.label_disgust= tk.Label(self.framemsf_label,text='厌恶',height=2)
        self.label_disgust.pack()#side='left',anchor='e')
        self.label_t2= tk.Label(self.framemsf_label,text='',height=1)
        self.label_t2.pack()#side='left',anchor='e')
       
        self.label_happy= tk.Label(self.framemsf_label,text='高兴',height=2)
        self.label_happy.pack()#side='left')#,anchor='e')
        self.label_t3= tk.Label(self.framemsf_label,text='',height=1)
        self.label_t3.pack()#side='left',anchor='e')

        self.label_sad  = tk.Label(self.framemsf_label,text='悲伤',height=2)
        self.label_sad.pack()#side='left')#,anchor='e')
        self.label_t4= tk.Label(self.framemsf_label,text='',height=1)
        self.label_t4.pack()#side='left',anchor='e')

        self.label_surprise= tk.Label(self.framemsf_label,text='惊讶',height=2)
        self.label_surprise.pack()#side='left')#,anchor='e')
        self.label_t5= tk.Label(self.framemsf_label,text='',height=1)
        self.label_t5.pack()#side='left',anchor='e')

        self.label_fear= tk.Label(self.framemsf_label,text='害怕',height=2)
        self.label_fear.pack()#side='left')#,anchor='e')
        #self.label_angry= tk.Label(self.framemsf_label,text='生气')
        
        self.chart = tk.Canvas(self.framemsf_bar)
        self.chart.pack(fill='both')
        '''
        self.label_angry.grid(row=0,column=0,sticky='e')
        self.label_disgust.grid(row=1,column=0,sticky='e')
        self.label_happy.grid(row=2,column=0,sticky='e')
        self.label_sad.grid(row=3,column=0,sticky='e')
        self.label_surprise.grid(row=4,column=0,sticky='e')
        self.label_fear.grid(row=5,column=0,sticky='e')
        '''
        #self.msb = tk.Canvas(self.frametop,height=240,width=320)  #micro expression button
        '''
        self.lf = tk.Label(self.master, text="First").grid(sticky=tk.E)
        self.ls = tk.Label(self.master, text="Second").grid(sticky=tk.E)

        self.e1 = tk.Entry(self.master)
        self.e2 = tk.Entry(self.master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

        self.checkbutton = tk.Checkbutton(self.master, text='Preserve aspect', variable=self.var)
        self.checkbutton.grid(columnspan=2, sticky=tk.W)

        self.photo = tk.PhotoImage()#file='/home/wang/skin/dest3_restore/heqingsezhi/E1-01-04_huangheban.jpg')
        self.label = tk.Label(image=self.photo)
        self.label.image = self.photo
        self.label.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        self.button1 = tk.Button(self.master, text='Zoom in')
        self.button1.grid(row=2, column=2)

        self.button2 = tk.Button(self.master, text='Zoom out')
        self.button2.grid(row=2, column=3)
        '''
    def run(self):
        self.master.mainloop()

class VideoCatch:
    def __init__(self, video_source=0,width=320,height=240):
        self.cap = cv2.VideoCapture(video_source)
        if not self.cap.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = width
        self.height = height
        self.vid.set(self.height,cv2.CAP_PROP_FRAME_HEIGHT)
        self.vid.set(self.width,cv2.CAP_PROP_FRAME_WIDTH)
        #self.callback = 

    def get_frame(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    def __del__(self):
       if self.cap.isOpened():
           self.cap.release()

class fmeApp(object):
    def __init__(self):
        self.layout = packlayout()
        self.cam = VideoCatch()

    def process(self):
        _,frame = self.cam.get_frame()
        image = PIL.Image.fromarray(frame)
        frame_out = ImageTk.PhotoImage(image)
        self.layout.scn.create_image(0, 0, image = frame_out, anchor = tkinter.NW)
        self.layout.master.after(15, self.process)
        self.layout.run()        

def main():
    app = fmeApp()
    app.process()

if __name__ == '__main__':
    main()
    #app = fmeApp()
    #app.process()
    '''
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        _,frame = cap.read()
        cv2.imshow('test',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            	break
    cap.release()
    cv2.destroyAllWindows()   
    '''
    '''
    master = tk.Tk()
    var = tk.IntVar()

    tk.Label(master, text="First").grid(sticky=tk.E)
    tk.Label(master, text="Second").grid(sticky=tk.E)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    checkbutton = tk.Checkbutton(master, text='Preserve aspect', variable=var)
    checkbutton.grid(columnspan=2, sticky=tk.W)

    photo = tk.PhotoImage()#file='/home/wang/skin/dest3_restore/heqingsezhi/E1-01-04_huangheban.jpg')
    label = tk.Label(image=photo)
    label.image = photo
    label.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

    button1 = tk.Button(master, text='Zoom in')
    button1.grid(row=2, column=2)

    button2 = tk.Button(master, text='Zoom out')
    button2.grid(row=2, column=3)

    tk.mainloop()
    '''
