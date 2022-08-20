#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk


root = Tk()
root.title("Welding Lean checklist")
root.geometry("1500x1500")
#root.iconbitmap("weld_ss/icon.ico")
frame1 = Frame(root)
frame1.pack(side=LEFT,fill=Y)
frame2 = Frame(root)
frame2.pack(side=RIGHT,fill=Y)

cb1var = StringVar()
cb4var = StringVar()
cb5var = StringVar()
cb6var = StringVar()

global seam_list
seam_list = ["U150","U140","U130", "U120", "U110", " 190", " 180", " 130", 
            " 170","1140", " 191", " 240", " 210", " 220", "U210", " 110", "U350", 
            "U340", "U330", "U320", "U310", " 390", " 380", " 330", " 370", "1340",
            " 391", " 440", " 410", " 420", "U410", " 310"]



global top_error_list 
top_error_list= []

def insert(current_row,main_frame): 
    main_frame.forget()
    top_error_list_iterator()
    

def seam_image_loader(seam_variable):
    global seam_image
    global row_number
    row_number=((seam_list.index(seam_variable))+32*(int(axle)-1))+17
    seam_image= (Image.open('seam_ss/'+seam_variable+'.png'))
    seam_image= seam_image.resize((400,350), Image.ANTIALIAS)
    seam_image= ImageTk.PhotoImage(seam_image)
    Label(frame1,image=seam_image).grid(row= 3,column= 1)
    Label(frame1, text = str(seam_list.index(seam_variable)+1) +" von 32").grid(row=4, column= 1)
    error_checkboxes()
    
def seam(event):
    global axle
    global all_seams_image
    all_seams_image= (Image.open('seam_ss/all_seams.png'))
    all_seams_image= all_seams_image.resize((600,400), Image.ANTIALIAS)
    all_seams_image= ImageTk.PhotoImage(all_seams_image)
    Label(frame1,image=all_seams_image).grid(row= 1,column= 1)
    axle = axle_variable.get()
    seam_variable = StringVar()
    seam_variable.set("---auswählen---")
    Label(frame1, text= "Bitte wählen Sie die Nahtnummer").grid(row= 2, column=0)
    seam_drop = OptionMenu(frame1,seam_variable, *seam_list,command=seam_image_loader).grid(row= 3, column=0)
    #go to seam_image_loader
    
def top_error_list_creator():
    global top_error_list
    CB_list=[cb1var.get(),cb4var.get(),cb5var.get(),cb6var.get()]
    for error in CB_list:
        if error!="none":
            top_error_list.append(error)
    frame1.forget()
    frame2.forget()
    top_error_list_iterator()
    
def top_error_list_iterator():
    global top_error_list
    if len(top_error_list) >=1 :
        popped = top_error_list.pop(0)
        if  popped == "Risse":
            crack(row_number)
        elif popped == "Bindefehler und ungenügende Durchschweißung":
            binding_defects(row_number)
        elif popped == "Form- und Maßabweichungen":
            shape_deviations(row_number)
        elif popped == "Sonstige Unregelmäßigkeiten":
            miscellaneous(row_number)
    else:
        frame1.pack(side=LEFT,fill=Y)
        frame2.pack(side=RIGHT,fill=Y)
        top_error_list=[]
def main_menu(main_frame):
    top_error_list.clear()
    main_frame.forget()
    frame1.pack(side=LEFT,fill=Y)
    frame2.pack(side=RIGHT,fill=Y)
                
def error_checkboxes():
    CB1 = Checkbutton(frame2, text = "Risse                                       ", variable = cb1var,onvalue="Risse",offvalue="none")
    CB1.deselect()
    CB1.grid(row=0,column= 0)

    CB4 = Checkbutton(frame2, text = "Bindefehler und ungenügende \nDurchschweißung", variable = cb4var,onvalue="Bindefehler und ungenügende Durchschweißung",offvalue="none")
    CB4.deselect()
    CB4.grid(row=1,column= 0)

    CB5 = Checkbutton(frame2, text = "Form- und Maßabweichungen                   ", variable = cb5var,onvalue="Form- und Maßabweichungen",offvalue="none")
    CB5.deselect()
    CB5.grid(row=3,column= 0)

    CB6 = Checkbutton(frame2, text = "Sonstige Unregelmäßigkeiten                  ", variable = cb6var,onvalue="Sonstige Unregelmäßigkeiten",offvalue="none")
    CB6.deselect()
    CB6.grid(row=4,column= 0)

    Button(frame2, text="Nächste", command=top_error_list_creator).grid(row=6,column= 0)

def crack(row_number):
    
    par100= StringVar()
    par101 = StringVar()
    par1013 = StringVar()
    par1014= StringVar()
    par104= StringVar()
    
    current_row=row_number
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH,expand=1)

    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    #adding scroll bar to canvas
    my_scroll_bar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scroll_bar.pack(side=RIGHT, fill=Y)

    #configuring the canvas
    my_canvas.configure(yscrollcommand=my_scroll_bar.set)
    my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    #creating another frame inside the canvas
    frame3 = Frame(my_canvas)

    #adding that frame to a window in the canvas
    my_canvas.create_window((0,0), window=frame3, anchor= "nw")

    #for scrolling with mouse wheel
    def on_mousewheel(event):
        my_canvas.yview_scroll(-1*(event.delta), "units")
    my_canvas.bind_all("<MouseWheel>", on_mousewheel)
    
    Label(frame3, text="100 - Riss:\nGröße der größten Riss x Lange x Anzahl der Risse\nEinheit: mm\u00b2").grid(row = 0, column = 0)
    Entry(frame3, textvariable=par100,width = 10).grid(row = 0, column = 1)
    global image100
    image100 = Image.open('weld_ss/blank.png')
    image100= image100.resize((300,200), Image.ANTIALIAS)
    image100= ImageTk.PhotoImage(image100)
    Label(frame3,image=image100).grid(row= 0,column= 2)
                                                       
    Label(frame3, text="101 - Längriss:\nGröße der größten Riss x Lange x Anzahl der Risse\nEinheit: mm\u00b2").grid(row = 0, column = 3)
    Entry(frame3, textvariable=par101,width = 10).grid(row = 0, column = 4)
    global image101
    image101 = Image.open('weld_ss/'+str(1011)+'.png')
    image101= image101.resize((300,200), Image.ANTIALIAS)
    image101= ImageTk.PhotoImage(image101)
    Label(frame3,image=image101).grid(row= 0,column= 5)
    
    Label(frame3, text="1013 - Längriss in der Wärmeeinflusszone:\n1014 - Längriss im Grundwerkstoff:\nGröße der größten Riss x Lange x Anzahl der Risse\nEinheit: mm\u00b2").grid(row = 1, column = 0)
    Entry(frame3, textvariable=par1013,width = 10).grid(row = 1, column = 1)
    global image1013
    image1013 = Image.open('weld_ss/'+str(1011)+'.png')
    image1013= image1013.resize((300,200), Image.ANTIALIAS)
    image1013= ImageTk.PhotoImage(image1013)
    Label(frame3,image=image1013).grid(row= 1,column= 2)
    
    Label(frame3, text="104 - Endkraterriss:\nGröße der größten Riss x Lange x Anzahl der Risse\nEinheit: mm\u00b2").grid(row = 1, column = 3)
    Entry(frame3, textvariable=par104,width = 10).grid(row = 1, column = 4)
    global image104
    image104= Image.open('weld_ss/'+str(1045)+'.png')
    image104= image104.resize((300,200), Image.ANTIALIAS)
    image104= ImageTk.PhotoImage(image104)
    Label(frame3,image=image104).grid(row= 1,column= 5)
        
    Label(frame3, text="                                                             ").grid(row = 2, column = 0)
    Button(frame3, text="Nächste", command=lambda:insert(current_row,main_frame)).grid(row=3, column=3) 
    Button(frame3, text="Hauptmenü", command=lambda:main_menu(main_frame)).grid(row=3, column=2)
    Label(frame3, text="                                                             ").grid(row =4, column = 0)


def binding_defects(row_number):
    par400= StringVar()
    par401 = StringVar()
    par4011 = StringVar()
    par4012 = StringVar()
    par4013= StringVar()

    current_row=row_number
    binding_defects_dict={66:par400,67:par401,68:par4011,69:par4012,70:par4013}
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH,expand=1)

    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    #adding scroll barto canvas
    my_scroll_bar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scroll_bar.pack(side=RIGHT, fill=Y)

    #configuring the canvas
    my_canvas.configure(yscrollcommand=my_scroll_bar.set)
    my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    #creating another frame inside the canvas
    frame3 = Frame(my_canvas)

    #adding that frame to a window in the canvas
    my_canvas.create_window((0,0), window=frame3, anchor= "nw")

    #for scrolling with mouse wheel
    def on_mousewheel(event):
        my_canvas.yview_scroll(-1*(event.delta), "units")
    my_canvas.bind_all("<MouseWheel>", on_mousewheel)
    
    Label(frame3, text="400 - Bindefehler und ungenügende \nDurchschweißung:\nGröße der größten \nUnregelmäßigkeit x Anzahl Unregelmäßigkeit\nEinheit: mm").grid(row = 0, column = 0)
    Entry(frame3, textvariable=par400,width = 10).grid(row = 0, column = 1)
    global image400
    image400 = Image.open('weld_ss/'+str(4011)+'.png')
    image400= image400.resize((300,200), Image.ANTIALIAS)
    image400= ImageTk.PhotoImage(image400)
    Label(frame3,image=image400).grid(row= 0,column= 2)
    
    Label(frame3, text="401 - Bindefehler:\nGröße der größten \nUnregelmäßigkeit x Anzahl Unregelmäßigkeit\nEinheit: mm").grid(row = 0, column = 3)
    Entry(frame3, textvariable=par401,width = 10).grid(row = 0, column = 4)
    global image401
    image401 = Image.open('weld_ss/'+str(4011)+'.png')
    image401= image401.resize((300,200), Image.ANTIALIAS)
    image401= ImageTk.PhotoImage(image401)
    Label(frame3,image=image401).grid(row= 0,column= 5)
    
    Label(frame3, text="4013 - Wurzelbindefehler:\nGröße der größten \nUnregelmäßigkeit x Anzahl Unregelmäßigkeit\nEinheit: mm").grid(row = 2, column = 0)
    Entry(frame3, textvariable=par4013,width = 10).grid(row = 2, column = 1)
    global image4013
    image4013 = Image.open('weld_ss/'+str(4013)+'.png')
    image4013= image4013.resize((300,200), Image.ANTIALIAS)
    image4013= ImageTk.PhotoImage(image4013)
    Label(frame3,image=image4013).grid(row= 2,column= 2)

    Label(frame3, text="                                                             ").grid(row = 5, column = 0)
    Button(frame3, text="Nächste", command=lambda:insert(current_row,main_frame)).grid(row=6, column=3) 
    Button(frame3, text="Hauptmenü", command=lambda:main_menu(main_frame)).grid(row=6, column=2)
    Label(frame3, text="                                                             ").grid(row = 7, column = 0)



def shape_deviations(row_number):
    par500= StringVar()
    par501 = StringVar()
    par5011 = StringVar()
    par5012 = StringVar()
    par5013 = StringVar()
    par5014 = StringVar()
    par5015 = StringVar()
    par502 = StringVar()
    par503 = StringVar()
    par504 = StringVar()
    par5041 = StringVar()
    par5042 = StringVar()
    par5043 = StringVar()
    par505 = StringVar()
    par5051 = StringVar()
    par5052 = StringVar()
    par506 = StringVar()
    par5061 = StringVar()
    par5062 = StringVar()
    par507 = StringVar()
    par5071 = StringVar()
    par5072 = StringVar()
    par508 = StringVar()
    par509 = StringVar()
    par5091 = StringVar()
    par5092 = StringVar()
    par5093 = StringVar()
    par5094 = StringVar()
    par510 = StringVar()
    par511 = StringVar()
    par512 = StringVar()
    par513 = StringVar()
    par514 = StringVar()
    par515 = StringVar()
    par516 = StringVar()
    par517 = StringVar()
    par5171 = StringVar()
    par5172 = StringVar()
    par520 = StringVar()
    par521 = StringVar()
    par5211 = StringVar()
    par5212 = StringVar()
    par5213 = StringVar()
    par5214 = StringVar()

    current_row=row_number

    main_frame = Frame(root)
    main_frame.pack(fill=BOTH,expand=1)

    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    #adding scroll barto canvas
    my_scroll_bar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scroll_bar.pack(side=RIGHT, fill=Y)

    #configuring the canvas
    my_canvas.configure(yscrollcommand=my_scroll_bar.set)
    my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    #creating another frame inside the canvas
    frame3 = Frame(my_canvas)

    #adding that frame to a window in the canvas
    my_canvas.create_window((0,0), window=frame3, anchor= "nw")

    #for scrolling with mouse wheel
    def on_mousewheel(event):
        my_canvas.yview_scroll(-1*(event.delta), "units")
    my_canvas.bind_all("<MouseWheel>", on_mousewheel)
    
    Label(frame3, text="500 - Formfehler:\nGröße der größten Abweichung / Blechdicke\nEinheit: Zahl").grid(row = 0, column = 0)
    Entry(frame3, textvariable=par500,width = 10).grid(row = 0, column = 1)
    global image500
    image500 = Image.open('weld_ss/'+str(504)+'.png')
    image500= image500.resize((250,200), Image.ANTIALIAS)
    image500= ImageTk.PhotoImage(image500)
    Label(frame3,image=image500).grid(row= 0,column= 2)
    
    Label(frame3, text="501 - Einbrandkerbe:\nGröße der größten Abweichung / Blechdicke\nEinheit: Zahl").grid(row = 0, column = 3)
    Entry(frame3, textvariable=par501,width = 10).grid(row = 0, column = 4)
    global image501
    image501 = Image.open('weld_ss/'+str(504)+'.png')
    image501= image501.resize((250,200), Image.ANTIALIAS)
    image501= ImageTk.PhotoImage(image501)
    Label(frame3,image=image501).grid(row= 0,column= 5)
    
    Label(frame3, text="5013 - Wurzelkerben: Kurze Unregelmäßig-keit:\nGröße der größten Abweichung / Blechdicke\nEinheit: Zahl").grid(row = 1, column = 0)
    Entry(frame3, textvariable=par5013,width = 10).grid(row = 1, column = 1)
    global image5013
    image5013 = Image.open('weld_ss/'+str(5013)+'.png')
    image5013= image5013.resize((320,190), Image.ANTIALIAS)
    image5013= ImageTk.PhotoImage(image5013)
    Label(frame3,image=image5013).grid(row= 1,column= 2)

    Label(frame3, text="503 -zu große Nahtüberhöhung (Kehlnaht):\nGröße der größten Abweichung / Blechdicke\nEinheit: Zahl").grid(row = 1, column = 3)
    Entry(frame3, textvariable=par503,width = 10).grid(row = 1, column = 4)
    global image503
    image503 = Image.open('weld_ss/'+str(503)+'.png')
    image503= image503.resize((320,190), Image.ANTIALIAS)
    image503= ImageTk.PhotoImage(image503)
    Label(frame3,image=image503).grid(row= 1,column= 5)    

    Label(frame3, text="5211 - zu große Schweißnahtdicke:\nGröße der größten Abweichung / Blechdicke\nEinheit: Zahl").grid(row = 2, column = 0)
    Entry(frame3, textvariable=par5211,width = 10).grid(row = 2, column = 1)
    global image5211
    image5211 = Image.open('weld_ss/'+str(52115212)+'.png')
    image5211= image5211.resize((250,200), Image.ANTIALIAS)
    image5211= ImageTk.PhotoImage(image5211)
    Label(frame3,image=image5211).grid(row= 2,column= 2)
    
    Label(frame3, text="5213 - zu kleine Kehlnahtdicke:\nGröße der größten Abweichung / Blechdicke\nEinheit: Zahl").grid(row = 2, column = 3)
    Entry(frame3, textvariable=par5213,width = 10).grid(row = 2, column = 4)
    global image5213
    image5213 = Image.open('weld_ss/'+str(5213)+'.png')
    image5213= image5213.resize((250,200), Image.ANTIALIAS)
    image5213= ImageTk.PhotoImage(image5213)
    Label(frame3,image=image5213).grid(row= 2,column= 5)
    
    Label(frame3, text="5214 -zu große Kehlnahtdicke:\nGröße der größten Abweichung / Blechdicke\nEinheit: Zahl").grid(row = 3, column = 0)
    Entry(frame3, textvariable=par5214,width = 10).grid(row = 3, column = 1)
    global image5214
    image5214 = Image.open('weld_ss/'+str(5214)+'.png')
    image5214= image5214.resize((250,200), Image.ANTIALIAS)
    image5214= ImageTk.PhotoImage(image5214)
    Label(frame3,image=image5214).grid(row= 3,column= 2)
    
    Button(frame3, text="Nächste", command=lambda:insert(current_row,main_frame)).grid(row=3, column=4) 
    Button(frame3, text="Hauptmenü", command=lambda:main_menu(main_frame)).grid(row=3, column=3)


def miscellaneous(row_number):
    par600 = StringVar()
    par601 = StringVar()
    par602 = StringVar()
    par6021 = StringVar()
    par603 = StringVar()
    par604 = StringVar()
    par605 = StringVar()
    par606 = StringVar()
    par607 = StringVar()
    par6071 = StringVar()
    par6072 = StringVar()
    par608 = StringVar()
    par610 = StringVar()
    par6101 = StringVar()
    par613 = StringVar()
    par614 = StringVar()
    par615 = StringVar()
    par617 = StringVar()
    par618 = StringVar()

    current_row=row_number
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH,expand=1)

    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    #adding scroll bar to canvas
    my_scroll_bar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scroll_bar.pack(side=RIGHT, fill=Y)

    #configuring the canvas
    my_canvas.configure(yscrollcommand=my_scroll_bar.set)
    my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    #creating another frame inside the canvas
    frame3 = Frame(my_canvas)

    #adding that frame to a window in the canvas
    my_canvas.create_window((0,0), window=frame3, anchor= "nw")

    #for scrolling with mouse wheel
    def on_mousewheel(event):
        my_canvas.yview_scroll(-1*(event.delta), "units")
    my_canvas.bind_all("<MouseWheel>", on_mousewheel)
    
    Label(frame3, text="602 - Spritzer:\nGröße der größten Abweichung\n Einheit: mm").grid(row = 0, column = 0)
    Entry(frame3, textvariable=par602,width = 10).grid(row = 0, column = 1)
    global image602
    image602= Image.open('weld_ss/blank.png')
    image602= image602.resize((250,200), Image.ANTIALIAS)
    image602= ImageTk.PhotoImage(image602)
    Label(frame3,image=image602).grid(row= 0,column= 2)

    Label(frame3, text="617 - schlechte Passung bei Kehlnähten:\nGröße der größten Abweichung\n Einheit: mm").grid(row = 1, column = 0)
    Entry(frame3, textvariable=par617,width = 10).grid(row = 1, column = 1)
    global image617
    image617= Image.open('weld_ss/'+str(617)+'.png')
    image617= image617.resize((400,250), Image.ANTIALIAS)
    image617= ImageTk.PhotoImage(image617)
    Label(frame3,image=image617).grid(row= 1,column= 2)
    
    Label(frame3, text="618 - Schwellung:\nGröße der größten Abweichung\n Einheit: mm").grid(row = 0, column = 3)
    Entry(frame3, textvariable=par618,width = 10).grid(row = 0, column = 4)
    global image618
    image618= Image.open('weld_ss/'+str(618)+'.png')
    image618= image618.resize((250,250), Image.ANTIALIAS)
    image618= ImageTk.PhotoImage(image618)
    Label(frame3,image=image618).grid(row= 0,column= 5)
    
    
    Label(frame3, text="                                                             ").grid(row = 2, column = 0)
    Button(frame3, text="Nächste", command=lambda:insert(current_row,main_frame)).grid(row=3, column=3)
    Button(frame3, text="Hauptmenü", command=lambda:main_menu(main_frame)).grid(row=3, column=2)
    Label(frame3, text="                                                             ").grid(row = 4, column = 0)

    
Label(frame1, text= "Bitte wählen Sie die Achsnummer").grid(row= 0, column=0)
axle_list = list(range(1,501))
axle_variable = StringVar()
axle_variable.set("---auswählen---")
axle_drop = OptionMenu(frame1,axle_variable, *axle_list,command=seam).grid(row= 1, column=0)



root.mainloop()


# In[ ]:




