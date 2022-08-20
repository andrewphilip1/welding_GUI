#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from PIL import Image,ImageTk
from openpyxl import *
from tkinter import ttk


root = Tk()
root.title("Welding")
root.geometry("1500x1500")
#root.iconbitmap("/Users/andrewkirubsingh/Desktop/IPEM/GUI/icon.ico")
frame1 = Frame(root)
frame1.pack(side=LEFT,fill=Y)
frame2 = Frame(root)
frame2.pack(side=RIGHT,fill=Y)

cb1var = StringVar()
cb2var = StringVar()
cb3var = StringVar()
cb4var = StringVar()
cb5var = StringVar()
cb6var = StringVar()

global seam_list
seam_list = ["U150","U140","U130", "U120", "U110", " 190", " 180", " 130", 
            " 170","1140", " 191", " 240", " 210", " 220", "U210", " 110", "U350", 
            "U340", "U330", "U320", "U310", " 390", " 380", " 330", " 370", "1340",
            " 391", " 440", " 410", " 420", "U410", " 310"]

wb = load_workbook('220118_Transposed_checklist_kommentiert_aps.xlsx') 
sheet = wb.active 

global top_error_list 
top_error_list= []

def insert(current_row,error_dict,main_frame): 
    for key,value in error_dict.items():
        if value.get() != "":
            sheet.cell(row=current_row , column=key).value = value.get()
    wb.save('220118_Transposed_checklist_kommentiert_aps.xlsx')
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
    CB_list=[cb1var.get(),cb2var.get(),cb3var.get(),cb4var.get(),cb5var.get(),cb6var.get()]
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
        elif popped == "Hohlräume":
            cavity(row_number)
        elif popped == "Feste Einschlüsse":
            solid_inclusions(row_number)
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
                
def error_checkboxes():
    CB1 = Checkbutton(frame2, text = "Risse                                       ", variable = cb1var,onvalue="Risse",offvalue="none")
    CB1.deselect()
    CB1.grid(row=0,column= 0)

    CB2 = Checkbutton(frame2, text = "Hohlräume                                   ", variable = cb2var,onvalue="Hohlräume",offvalue="none")
    CB2.deselect()
    CB2.grid(row=1,column= 0)

    CB3 = Checkbutton(frame2, text = "Feste Einschlüsse                           ", variable = cb3var,onvalue="Feste Einschlüsse",offvalue="none")
    CB3.deselect()
    CB3.grid(row=2,column= 0)

    CB4 = Checkbutton(frame2, text = "Bindefehler und ungenügende \nDurchschweißung", variable = cb4var,onvalue="Bindefehler und ungenügende Durchschweißung",offvalue="none")
    CB4.deselect()
    CB4.grid(row=3,column= 0)

    CB5 = Checkbutton(frame2, text = "Form- und Maßabweichungen                   ", variable = cb5var,onvalue="Form- und Maßabweichungen",offvalue="none")
    CB5.deselect()
    CB5.grid(row=4,column= 0)

    CB6 = Checkbutton(frame2, text = "Sonstige Unregelmäßigkeiten                  ", variable = cb6var,onvalue="Sonstige Unregelmäßigkeiten",offvalue="none")
    CB6.deselect()
    CB6.grid(row=5,column= 0)

    Button(frame2, text="Nächste", command=top_error_list_creator).grid(row=6,column= 0)

def crack(row_number):
    par100= StringVar()
    par1001 = StringVar()
    par101 = StringVar()
    par1011 = StringVar()
    par1012 = StringVar()
    par1013 = StringVar()
    par1014 = StringVar()
    par102 = StringVar()
    par1021 = StringVar()
    par1023 = StringVar()
    par1024 = StringVar()
    par103 = StringVar()
    par1031 = StringVar()
    par1033 = StringVar()
    par1034 = StringVar()
    par104 = StringVar()
    par1045 = StringVar()
    par1046 = StringVar()
    par1047 = StringVar()
    par105 = StringVar()
    par1051 = StringVar()
    par1053 = StringVar()
    par1054 = StringVar()
    par106 = StringVar()
    par1061 = StringVar()
    par1063 = StringVar()
    par1064 = StringVar()
    current_row=row_number
    crack_dict={4:par100,5:par1001,6:par101,7:par1011,8:par1012,9:par1013,10:par1014,11:par102,12:par1021,13:par1023,
           14:par1024,15:par103,16:par1031,17:par1033,18:par1034,19:par104,20:par1045,21:par1046,22:par1047,23:par105,
           24:par1051,25:par1053,26:par1054,27:par106,28:par1061,29:par1063,30:par1064}
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
    
    Label(frame3, text="100 - Riss: Nicht zulässig").grid(row = 0, column = 0)
    Entry(frame3, textvariable=par100,width = 10).grid(row = 0, column = 1)
    global image100
    image100 = Image.open('weld_ss/'+str(1011)+'.png')
    image100= image100.resize((200,150), Image.ANTIALIAS)
    image100= ImageTk.PhotoImage(image100)
    Label(frame3,image=image100).grid(row= 0,column= 2)
    
    Label(frame3, text="1001 - Mikroriss: Die Zulässigkeit hängt ab von der Art des \nGrundwerkstoffes und vor allem von der Rissanfälligkeit").grid(row = 0, column = 3)
    Entry(frame3, textvariable=par1001,width = 10).grid(row = 0, column = 4)
    global image1001
    image1001 = Image.open('weld_ss/'+str(1011)+'.png')
    image1001= image1001.resize((200,150), Image.ANTIALIAS)
    image1001= ImageTk.PhotoImage(image1001)
    Label(frame3,image=image1001).grid(row= 0,column= 5)
    
    Label(frame3, text="101 - Längriss: Leer in der Norm").grid(row = 1, column = 0)
    Entry(frame3, textvariable=par101,width = 10).grid(row = 1, column = 1)
    global image101
    image101 = Image.open('weld_ss/'+str(1011)+'.png')
    image101= image101.resize((200,150), Image.ANTIALIAS)
    image101= ImageTk.PhotoImage(image101)
    Label(frame3,image=image101).grid(row= 1,column= 2)
    
    Label(frame3, text="1011 - Längriss im Schweißgut: Leer in der Norm").grid(row = 1, column = 3)
    Entry(frame3, textvariable=par1011,width = 10).grid(row = 1, column = 4)
    global image1011
    image1011 = Image.open('weld_ss/'+str(1011)+'.png')
    image1011= image1011.resize((200,150), Image.ANTIALIAS)
    image1011= ImageTk.PhotoImage(image1011)
    Label(frame3,image=image1011).grid(row= 1,column= 5)
    
    Label(frame3, text="1012 - Längriss in der Bindezone: Leer in der Norm").grid(row = 2, column = 0)
    Entry(frame3, textvariable=par1012,width = 10).grid(row = 2, column = 1)
    global image1012
    image1012 = Image.open('weld_ss/'+str(1011)+'.png')
    image1012= image1012.resize((200,150), Image.ANTIALIAS)
    image1012= ImageTk.PhotoImage(image1012)
    Label(frame3,image=image1012).grid(row= 2,column= 2)

    Label(frame3, text="1013 - Längriss in der Wärmeeinflusszone: Leer in der Norm").grid(row = 2, column = 3)
    Entry(frame3, textvariable=par1013,width = 10).grid(row = 2, column = 4)
    global image1013
    image1013 = Image.open('weld_ss/'+str(1011)+'.png')
    image1013= image1013.resize((200,150), Image.ANTIALIAS)
    image1013= ImageTk.PhotoImage(image1013)
    Label(frame3,image=image1013).grid(row= 2,column= 5)
    
    Label(frame3, text="1014 - Längriss im Grundwerkstoff: Leer in der Norm").grid(row = 3, column = 0)
    Entry(frame3, textvariable=par1014,width = 10).grid(row = 3, column = 1)
    global image1014
    image1014 = Image.open('weld_ss/'+str(1011)+'.png')
    image1014= image1014.resize((200,150), Image.ANTIALIAS)
    image1014= ImageTk.PhotoImage(image1014)
    Label(frame3,image=image1014).grid(row= 3,column= 2)
    
    Label(frame3, text="102 - Querriss: Leer in der Norm").grid(row = 3, column = 3)
    Entry(frame3, textvariable=par102,width = 10).grid(row = 3, column = 4)
    global image102
    image102 = Image.open('weld_ss/'+str(1011)+'.png')
    image102= image102.resize((200,150), Image.ANTIALIAS)
    image102= ImageTk.PhotoImage(image102)
    Label(frame3,image=image102).grid(row= 3,column= 5)

    Label(frame3, text="1021 -Querriss im Schweißgut: Leer in der Norm").grid(row = 4, column = 0)
    Entry(frame3, textvariable=par1021,width = 10).grid(row = 4, column = 1)
    global image1021
    image1021 = Image.open('weld_ss/'+str(1021)+'.png')
    image1021= image1021.resize((200,150), Image.ANTIALIAS)
    image1021= ImageTk.PhotoImage(image1021)
    Label(frame3,image=image1021).grid(row= 4,column= 2)
    
    Label(frame3, text="1023 - Querriss im in der Wärmeeinflusszone: Leer in der Norm").grid(row = 4, column = 3)
    Entry(frame3, textvariable=par1023,width = 10).grid(row = 4, column = 4)
    global image1023
    image1023 = Image.open('weld_ss/'+str(1021)+'.png')
    image1023= image1023.resize((200,150), Image.ANTIALIAS)
    image1023= ImageTk.PhotoImage(image1023)
    Label(frame3,image=image1023).grid(row= 4,column= 5)
    
    Label(frame3, text="1024 -Querriss im Grundwerkstoff: Leer in der Norm").grid(row = 5, column = 0)
    Entry(frame3, textvariable=par1024,width = 10).grid(row = 5, column = 1)
    global image1024
    image1024 = Image.open('weld_ss/'+str(1021)+'.png')
    image1024= image1024.resize((200,150), Image.ANTIALIAS)
    image1024= ImageTk.PhotoImage(image1024)
    Label(frame3,image=image1024).grid(row= 5,column= 2)
    
    Label(frame3, text="103 - sternförmige Riss: Leer in der Norm").grid(row = 5, column = 3)
    Entry(frame3, textvariable=par103,width = 10).grid(row = 5, column = 4)
    global image103
    image103 = Image.open('weld_ss/'+str(1031)+'.png')
    image103= image103.resize((200,150), Image.ANTIALIAS)
    image103= ImageTk.PhotoImage(image103)
    Label(frame3,image=image103).grid(row= 5,column= 5)
    
    Label(frame3, text="1031 - sternförmige Riss im Schweißgut: Leer in der Norm").grid(row = 6, column = 0)
    Entry(frame3, textvariable=par1031,width = 10).grid(row = 6, column = 1)
    global image1031
    image1031 = Image.open('weld_ss/'+str(1031)+'.png')
    image1031= image1031.resize((200,150), Image.ANTIALIAS)
    image1031= ImageTk.PhotoImage(image1031)
    Label(frame3,image=image1031).grid(row= 6,column= 2)
    
    Label(frame3, text="1033 - sternförmige Riss in der Wärmeeinflusszone: Leer in der Norm").grid(row = 6, column = 3)
    Entry(frame3, textvariable=par1033,width = 10).grid(row = 6, column = 4)
    global image1033
    image1033 = Image.open('weld_ss/'+str(1031)+'.png')
    image1033= image1033.resize((200,150), Image.ANTIALIAS)
    image1033= ImageTk.PhotoImage(image1033)
    Label(frame3,image=image1033).grid(row= 6,column= 5)
    
    Label(frame3, text="1034 - sternförmige Riss im Grundwerkstoff: Leer in der Norm").grid(row = 7, column = 0)
    Entry(frame3, textvariable=par1034,width = 10).grid(row = 7, column = 1)
    global image1034
    image1034= Image.open('weld_ss/'+str(1031)+'.png')
    image1034= image1034.resize((200,150), Image.ANTIALIAS)
    image1034= ImageTk.PhotoImage(image1034)
    Label(frame3,image=image1034).grid(row= 7,column= 2)
    
    Label(frame3, text="104 - Endkraterriss: Nicht zulässig").grid(row = 7, column = 3)
    Entry(frame3, textvariable=par104,width = 10).grid(row = 7, column = 4)
    global image104
    image104= Image.open('weld_ss/'+str(1045)+'.png')
    image104= image104.resize((200,150), Image.ANTIALIAS)
    image104= ImageTk.PhotoImage(image104)
    Label(frame3,image=image104).grid(row= 7,column= 5)
    
    Label(frame3, text="1045 - Endkraterriss längs: Leer in der Norm").grid(row = 8, column = 0)
    Entry(frame3, textvariable=par1045,width = 10).grid(row = 8, column = 1)
    global image1045
    image1045= Image.open('weld_ss/'+str(1045)+'.png')
    image1045= image1045.resize((200,150), Image.ANTIALIAS)
    image1045= ImageTk.PhotoImage(image1045)
    Label(frame3,image=image1045).grid(row= 8,column= 2)
    
    Label(frame3, text="1046 - Endkraterriss quer: Leer in der Norm").grid(row = 8, column = 3)
    Entry(frame3, textvariable=par1046,width = 10).grid(row = 8, column = 4)
    global image1046
    image1046= Image.open('weld_ss/'+str(1046)+'.png')
    image1046= image1046.resize((200,150), Image.ANTIALIAS)
    image1046= ImageTk.PhotoImage(image1046)
    Label(frame3,image=image1046).grid(row= 8,column= 5)
    
    Label(frame3, text="1047 - Endkraterriss sternförmig: Leer in der Norm").grid(row = 9, column = 0)
    Entry(frame3, textvariable=par1047,width = 10).grid(row = 9, column = 1)
    global image1047
    image1047= Image.open('weld_ss/'+str(1047)+'.png')
    image1047= image1047.resize((200,150), Image.ANTIALIAS)
    image1047= ImageTk.PhotoImage(image1047)
    Label(frame3,image=image1047).grid(row= 9,column= 2)
    
    Label(frame3, text="105 - Rissanhäufung: Leer in der Norm").grid(row = 9, column = 3)
    Entry(frame3, textvariable=par105,width = 10).grid(row = 9, column = 4)
    global image105
    image105= Image.open('weld_ss/'+str(105)+'.png')
    image105= image105.resize((200,150), Image.ANTIALIAS)
    image105= ImageTk.PhotoImage(image105)
    Label(frame3,image=image105).grid(row= 9,column= 5)
    
    Label(frame3, text="1051 - Rissanhäufung im Schweißgut: Leer in der Norm").grid(row = 10, column = 0)
    Entry(frame3, textvariable=par1051,width = 10).grid(row = 10, column = 1)
    global image1051
    image1051= Image.open('weld_ss/'+str(105)+'.png')
    image1051= image1051.resize((200,150), Image.ANTIALIAS)
    image1051= ImageTk.PhotoImage(image1051)
    Label(frame3,image=image1051).grid(row= 10,column= 2)
    
    Label(frame3, text="1053 - Rissanhäufung in der Wärmeeinflusszone: Leer in der Norm").grid(row = 10, column = 3)
    Entry(frame3, textvariable=par1053,width = 10).grid(row = 10, column = 4)
    global image1053
    image1053= Image.open('weld_ss/'+str(105)+'.png')
    image1053= image1053.resize((200,150), Image.ANTIALIAS)
    image1053= ImageTk.PhotoImage(image1053)
    Label(frame3,image=image1053).grid(row= 10,column= 5)
    
    Label(frame3, text="1054 - Rissanhäufung im Grundwerkstoff: Leer in der Norm").grid(row = 11, column = 0)
    Entry(frame3, textvariable=par1054,width = 10).grid(row = 11, column = 1)
    global image1054
    image1054= Image.open('weld_ss/'+str(105)+'.png')
    image1054= image1054.resize((200,150), Image.ANTIALIAS)
    image1054= ImageTk.PhotoImage(image1054)
    Label(frame3,image=image1054).grid(row= 11,column= 2)
    
    Label(frame3, text="106 - verästelter Riss: Leer in der Norm").grid(row = 11, column = 3)
    Entry(frame3, textvariable=par106,width = 10).grid(row = 11, column = 4)
    global image106
    image106= Image.open('weld_ss/'+str(106)+'.png')
    image106= image106.resize((200,150), Image.ANTIALIAS)
    image106= ImageTk.PhotoImage(image106)
    Label(frame3,image=image106).grid(row= 11,column= 5)
    
    Label(frame3, text="1061 - verästelter Riss im Schweißgut: Leer in der Norm").grid(row = 12, column = 0)
    Entry(frame3, textvariable=par1061,width = 10).grid(row = 12, column = 1)
    global image1061
    image1061= Image.open('weld_ss/'+str(106)+'.png')
    image1061= image1061.resize((200,150), Image.ANTIALIAS)
    image1061= ImageTk.PhotoImage(image1061)
    Label(frame3,image=image1061).grid(row= 12,column= 2)
    
    Label(frame3, text="1063 - verästelter Riss in der Wärmeeinflusszone: Leer in der Norm").grid(row = 12, column = 3)
    Entry(frame3, textvariable=par1063,width = 10).grid(row = 12, column = 4)
    global image1063
    image1063= Image.open('weld_ss/'+str(106)+'.png')
    image1063= image1063.resize((200,150), Image.ANTIALIAS)
    image1063= ImageTk.PhotoImage(image1063)
    Label(frame3,image=image1063).grid(row= 12,column= 5)
    
    Label(frame3, text="1064 - verästelter Riss im Grundwerkstoff: Leer in der Norm").grid(row = 13, column = 0)
    Entry(frame3, textvariable=par1064,width = 10).grid(row = 13, column = 1)
    global image1064
    image1064= Image.open('weld_ss/'+str(106)+'.png')
    image1064= image1064.resize((200,150), Image.ANTIALIAS)
    image1064= ImageTk.PhotoImage(image1064)
    Label(frame3,image=image1064).grid(row= 13,column= 2)
        
    Label(frame3, text="                                                             ").grid(row = 14, column = 0)
    Button(frame3, text="Nächste", command=lambda:insert(current_row,crack_dict,main_frame)).grid(row=15, column=3) 
    Label(frame3, text="                                                             ").grid(row = 16, column = 0)

def cavity(row_number):
    par200 = StringVar()
    par201 = StringVar()
    par2011 = StringVar()
    par2012 = StringVar()
    par2013 = StringVar()
    par2014 = StringVar()
    par2015 = StringVar()
    par2016 = StringVar()
    par2017 = StringVar()
    par2018 = StringVar()
    par202 = StringVar()
    par2021 = StringVar()
    par2024 = StringVar()
    par2025 = StringVar()
    par203 = StringVar()
    par2031 = StringVar()
    par2032 = StringVar()


    current_row=row_number
    cavity_dict={31:par200, 32:par201, 33:par2011, 34:par2012, 35:par2013, 36:par2014, 
                 37:par2015, 38:par2016, 39:par2017, 40:par2018, 41:par202, 42:par2021, 
                 43:par2024, 44:par2025, 45:par203, 46:par2031, 47:par2032}
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
    
    Label(frame3, text="200 - Hohlraum: Leer in der Norm").grid(row = 0, column = 0)
    Entry(frame3, textvariable=par200,width = 10).grid(row = 0, column = 1)
    global image200
    image200= Image.open('weld_ss/'+str(2011)+'.png')
    image200= image200.resize((200,150), Image.ANTIALIAS)
    image200= ImageTk.PhotoImage(image200)
    Label(frame3,image=image200).grid(row= 0,column= 2)
    
    Label(frame3, text="201 - Gaseinschluss: Leer in der Norm").grid(row = 0, column = 3)
    Entry(frame3, textvariable=par201,width = 10).grid(row = 0, column = 4)
    global image201
    image201= Image.open('weld_ss/'+str(2011)+'.png')
    image201= image201.resize((200,150), Image.ANTIALIAS)
    image201= ImageTk.PhotoImage(image201)
    Label(frame3,image=image201).grid(row= 0,column= 5)
    
    Label(frame3, text="2011 - Pore: Leer in der Norm").grid(row = 1, column = 0)
    Entry(frame3, textvariable=par2011,width = 10).grid(row = 1, column = 1)
    global image2011
    image2011= Image.open('weld_ss/'+str(2011)+'.png')
    image2011= image2011.resize((200,150), Image.ANTIALIAS)
    image2011= ImageTk.PhotoImage(image2011)
    Label(frame3,image=image2011).grid(row= 1,column= 2)
    
    Label(frame3, text="2012 - gleichmäßig verteilte Porosität: \nEinlagig: ≤ 1 % Mehrlagig: ≤ 2 % ≤1% \nd ≤ 0,2 s, aber max. 3 mm").grid(row = 1, column = 3)
    Entry(frame3, textvariable=par2012,width = 10).grid(row = 1, column = 4)
    global image2012
    image2012= Image.open('weld_ss/'+str(2012)+'.png')
    image2012= image2012.resize((200,150), Image.ANTIALIAS)
    image2012= ImageTk.PhotoImage(image2012)
    Label(frame3,image=image2012).grid(row= 1,column= 5)
    
    Label(frame3, text="2013 - Porennest: dA ≤15mm oder dA,max ≤Wp/2").grid(row = 2, column = 0)
    Entry(frame3, textvariable=par2013,width = 10).grid(row = 2, column = 1)
    global image2013
    image2013= Image.open('weld_ss/'+str(2013)+'.png')
    image2013= image2013.resize((200,150), Image.ANTIALIAS)
    image2013= ImageTk.PhotoImage(image2013)
    Label(frame3,image=image2013).grid(row= 2,column= 2)
    
    Label(frame3, text="2014 - Porenzeile: h ≤ 0,2 s, aber max. 2 mm \nl ≤ s, aber max. 25 mm").grid(row = 2, column = 3)
    Entry(frame3, textvariable=par2014,width = 10).grid(row = 2, column = 4)
    global image2014
    image2014= Image.open('weld_ss/'+str(2014)+'.png')
    image2014= image2014.resize((200,150), Image.ANTIALIAS)
    image2014= ImageTk.PhotoImage(image2014)
    Label(frame3,image=image2014).grid(row= 2,column= 5)
    
    Label(frame3, text="2015 - Gaskanal: h ≤ 0,2 s, aber max. 2 mm \nl ≤ s, aber max. 25 mm").grid(row = 3, column = 0)
    Entry(frame3, textvariable=par2015,width = 10).grid(row = 3, column = 1)
    global image2015
    image2015= Image.open('weld_ss/'+str(2015)+'.png')
    image2015= image2015.resize((200,150), Image.ANTIALIAS)
    image2015= ImageTk.PhotoImage(image2015)
    Label(frame3,image=image2015).grid(row= 3,column= 2)
    
    Label(frame3, text="2016 - Schlauchpore: h ≤ 0,2 s, aber max. 2 mm \nl ≤ s, aber max. 25 mm").grid(row = 3, column = 3)
    Entry(frame3, textvariable=par2016,width = 10).grid(row = 3, column = 4)
    global image2016
    image2016= Image.open('weld_ss/'+str(2016)+'.png')
    image2016= image2016.resize((300,150), Image.ANTIALIAS)
    image2016= ImageTk.PhotoImage(image2016)
    Label(frame3,image=image2016).grid(row= 3,column= 5)
    
    Label(frame3, text="2017 - Oberflächenpore: Nicht zulässig").grid(row = 4, column = 0)
    Entry(frame3, textvariable=par2017,width = 10).grid(row = 4, column = 1)
    global image2017
    image2017= Image.open('weld_ss/'+str(2017)+'.png')
    image2017= image2017.resize((200,150), Image.ANTIALIAS)
    image2017= ImageTk.PhotoImage(image2017)
    Label(frame3,image=image2017).grid(row= 4,column= 2)
    
    Label(frame3, text="2018 - Oberflächenporosität: Leer in der Norm").grid(row = 4, column = 3)
    Entry(frame3, textvariable=par2018,width = 10).grid(row = 4, column = 4)
    global image2018
    image2018= Image.open('weld_ss/'+str(2017)+'.png')
    image2018= image2018.resize((200,150), Image.ANTIALIAS)
    image2018= ImageTk.PhotoImage(image2018)
    Label(frame3,image=image2018).grid(row= 4,column= 5)
    
    Label(frame3, text="202 - Lunker: Nicht zulässig").grid(row = 5, column = 0)
    Entry(frame3, textvariable=par202,width = 10).grid(row = 5, column = 1)
    global image202
    image202= Image.open('weld_ss/'+str(2021)+'.png')
    image202= image202.resize((200,150), Image.ANTIALIAS)
    image202= ImageTk.PhotoImage(image202)
    Label(frame3,image=image202).grid(row= 5,column= 2)
    
    Label(frame3, text="2021 -interdendritischer Lunker (Makrolunker): \nLeer in der Norm").grid(row = 5, column = 3)
    Entry(frame3, textvariable=par2021,width = 10).grid(row = 5, column = 4)
    global image2021
    image2021= Image.open('weld_ss/'+str(2021)+'.png')
    image2021= image2021.resize((200,150), Image.ANTIALIAS)
    image2021= ImageTk.PhotoImage(image2021)
    Label(frame3,image=image2021).grid(row= 5,column= 5)
    
    Label(frame3, text="2024 - Endkraterlunker: Nicht zulässig").grid(row = 6, column = 0)
    Entry(frame3, textvariable=par2024,width = 10).grid(row = 6, column = 1)
    global image2024
    image2024= Image.open('weld_ss/'+str(2024)+'.png')
    image2024= image2024.resize((250,150), Image.ANTIALIAS)
    image2024= ImageTk.PhotoImage(image2024)
    Label(frame3,image=image2024).grid(row= 6,column= 2)
    
    Label(frame3, text="2025 -offener Endkraterlunker: Nicht zulässig").grid(row = 6, column = 3)
    Entry(frame3, textvariable=par2025,width = 10).grid(row = 6, column = 4)
    global image2025
    image2025= Image.open('weld_ss/'+str(2025)+'.png')
    image2025= image2025.resize((200,150), Image.ANTIALIAS)
    image2025= ImageTk.PhotoImage(image2025)
    Label(frame3,image=image2025).grid(row= 6,column= 5)
    
    Label(frame3, text="203 - Mikrolunker: Leer in der Norm").grid(row = 7, column = 0)
    Entry(frame3, textvariable=par203,width = 10).grid(row = 7, column = 1)
    global image203
    image203= Image.open('weld_ss/'+str(2025)+'.png')
    image203= image203.resize((200,150), Image.ANTIALIAS)
    image203= ImageTk.PhotoImage(image203)
    Label(frame3,image=image203).grid(row= 7,column= 2)
    
    Label(frame3, text="2031 -interdendritischer Mikrolunker: Leer in der Norm").grid(row = 7, column = 3)
    Entry(frame3, textvariable=par2031,width = 10).grid(row = 7, column = 4)
    global image2031
    image2031= Image.open('weld_ss/'+str(2025)+'.png')
    image2031= image2031.resize((200,150), Image.ANTIALIAS)
    image2031= ImageTk.PhotoImage(image2031)
    Label(frame3,image=image2031).grid(row= 7,column= 5)
    
    Label(frame3, text="2032 - transkristalliner Mikrolunker: \nLeer in der Norm").grid(row = 8, column = 0)
    Entry(frame3, textvariable=par2032,width = 10).grid(row = 8, column = 1)
    global image2032
    image2032= Image.open('weld_ss/'+str(2025)+'.png')
    image2032= image2032.resize((200,150), Image.ANTIALIAS)
    image2032= ImageTk.PhotoImage(image2032)
    Label(frame3,image=image2032).grid(row= 8,column= 2)
    
    Label(frame3, text="                                                             ").grid(row = 9, column = 0)
    Button(frame3, text="Nächste", command=lambda:insert(current_row,cavity_dict,main_frame)).grid(row=10, column=3) 
    Label(frame3, text="                                                             ").grid(row = 11, column = 0)
    
    
def binding_defects(row_number):
    par400= StringVar()
    par401 = StringVar()
    par4011 = StringVar()
    par4012 = StringVar()
    par4013= StringVar()
    par4014 = StringVar()
    par402 = StringVar()
    par4021 = StringVar()
    par403 = StringVar()

    current_row=row_number
    binding_defects_dict={66:par400,67:par401,68:par4011,69:par4012,70:par4013,71:par4014,72:par402,73:par4021,74:par403}
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
    
    Label(frame3, text="400 - Bindefehler und ungenügende \nDurchschweißung:Leer in der Norm").grid(row = 0, column = 0)
    Entry(frame3, textvariable=par400,width = 10).grid(row = 0, column = 1)
    global image400
    image400 = Image.open('weld_ss/'+str(4011)+'.png')
    image400= image400.resize((200,150), Image.ANTIALIAS)
    image400= ImageTk.PhotoImage(image400)
    Label(frame3,image=image400).grid(row= 0,column= 2)
    
    Label(frame3, text="401 - Bindefehler: Nicht zulässig").grid(row = 0, column = 3)
    Entry(frame3, textvariable=par401,width = 10).grid(row = 0, column = 4)
    global image401
    image401 = Image.open('weld_ss/'+str(4011)+'.png')
    image401= image401.resize((200,150), Image.ANTIALIAS)
    image401= ImageTk.PhotoImage(image401)
    Label(frame3,image=image401).grid(row= 0,column= 5)
    
    Label(frame3, text="4011 - Flankenbindefehler: Nicht zulässig").grid(row = 1, column = 0)
    Entry(frame3, textvariable=par4011,width = 10).grid(row = 1, column = 1)
    global image4011
    image4011 = Image.open('weld_ss/'+str(4011)+'.png')
    image4011= image4011.resize((200,150), Image.ANTIALIAS)
    image4011= ImageTk.PhotoImage(image4011)
    Label(frame3,image=image4011).grid(row= 1,column= 2)
    
    Label(frame3, text="4012 -Lagenbindefehler: Nicht zulässig").grid(row = 1, column = 3)
    Entry(frame3, textvariable=par4012,width = 10).grid(row = 1, column = 4)
    global image4012
    image4012 = Image.open('weld_ss/'+str(4012)+'.png')
    image4012= image4012.resize((300,150), Image.ANTIALIAS)
    image4012= ImageTk.PhotoImage(image4012)
    Label(frame3,image=image4012).grid(row= 1,column= 5)
    
    Label(frame3, text="4013 - Wurzelbindefehler : Nicht zulässig").grid(row = 2, column = 0)
    Entry(frame3, textvariable=par4013,width = 10).grid(row = 2, column = 1)
    global image4013
    image4013 = Image.open('weld_ss/'+str(4013)+'.png')
    image4013= image4013.resize((200,150), Image.ANTIALIAS)
    image4013= ImageTk.PhotoImage(image4013)
    Label(frame3,image=image4013).grid(row= 2,column= 2)

    Label(frame3, text="4014 - Mikrobindefehler: Leer in der Norm").grid(row = 2, column = 3)
    Entry(frame3, textvariable=par4014,width = 10).grid(row = 2, column = 4)
    global image4014
    image4014 = Image.open('weld_ss/'+str(4014)+'.png')
    image4014= image4014.resize((200,150), Image.ANTIALIAS)
    image4014= ImageTk.PhotoImage(image4014)
    Label(frame3,image=image4014).grid(row= 2,column= 5)
    
    Label(frame3, text="402 - ungenügende Durchschweißung : Nicht zulässig").grid(row = 3, column = 0)
    Entry(frame3, textvariable=par402,width = 10).grid(row = 3, column = 1)
    global image402
    image402 = Image.open('weld_ss/'+str(402)+'.png')
    image402= image402.resize((300,150), Image.ANTIALIAS)
    image402= ImageTk.PhotoImage(image402)
    Label(frame3,image=image402).grid(row= 3,column= 2)
    
    Label(frame3, text="403 -Spikebildung : Leer in der Norm").grid(row = 3, column = 3)
    Entry(frame3, textvariable=par403,width = 10).grid(row = 3, column = 4)
    global image403
    image403 = Image.open('weld_ss/'+str(403)+'.png')
    image403= image403.resize((200,150), Image.ANTIALIAS)
    image403= ImageTk.PhotoImage(image403)
    Label(frame3,image=image403).grid(row= 3,column= 5)
    
    Label(frame3, text="4021 - ungenügender Wurzeleinbrand : Nicht zulässig").grid(row = 4, column = 0)
    Entry(frame3, textvariable=par4021,width = 10).grid(row = 4, column = 1)
    global image4021
    image4021 = Image.open('weld_ss/'+str(4021)+'.png')
    image4021= image4021.resize((300,150), Image.ANTIALIAS)
    image4021= ImageTk.PhotoImage(image4021)
    Label(frame3,image=image4021).grid(row= 4,column= 2)
    
    Label(frame3, text="                                                             ").grid(row = 5, column = 0)
    Button(frame3, text="Nächste", command=lambda:insert(current_row,binding_defects_dict,main_frame)).grid(row=6, column=3) 
    Label(frame3, text="                                                             ").grid(row = 7, column = 0)


def solid_inclusions(row_number):
    par300= StringVar()
    par301 = StringVar()
    par3011 = StringVar()
    par3012 = StringVar()
    par3013 = StringVar()
    par302 = StringVar()
    par3021 = StringVar()
    par3022 = StringVar()
    par3023 = StringVar()
    par303 = StringVar()
    par3031 = StringVar()
    par3032 = StringVar()
    par3033 = StringVar()
    par3034 = StringVar()
    par304 = StringVar()
    par3041 = StringVar()
    par3042 = StringVar()
    par3043 = StringVar()

    current_row=row_number
    solid_inclusions_dict={48:par300,49:par301,50:par3011,51:par3012,52:par3013,53:par302,54:par3021,55:par3022,56:par3023,57:par303,
    58:par3031,59:par3032,60:par3033,61:par3034,62:par304,63:par3041,64:par3042,65:par3043}
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

    Label(frame3, text="300 - fester Einschluss:\n        h ≤ 0,2 s, aber max. 2 mm \nl ≤ s, aber max. 25 mm").grid(row = 0, column = 0)
    Entry(frame3, textvariable=par300,width = 10).grid(row = 0, column = 1)
    global image300
    image300 = Image.open('weld_ss/'+str(3011)+'.png')
    image300= image300.resize((200,150), Image.ANTIALIAS)
    image300= ImageTk.PhotoImage(image300)
    Label(frame3,image=image300).grid(row= 0,column= 2)

    Label(frame3, text="301 - fester Einschluss:\n        h ≤ 0,2 s, aber max. 2 mm \nl ≤ s, aber max. 25 mm").grid(row = 0, column = 3)
    Entry(frame3, textvariable=par301,width = 10).grid(row = 0, column = 4)
    global image301
    image301 = Image.open('weld_ss/'+str(3011)+'.png')
    image301= image301.resize((200,150), Image.ANTIALIAS)
    image301= ImageTk.PhotoImage(image301)
    Label(frame3,image=image301).grid(row= 0,column= 5)

    Label(frame3, text="3011 - Schlackeneinschluss zeilenförmig: Leer in der Norm").grid(row = 1, column = 0)
    Entry(frame3, textvariable=par3011,width = 10).grid(row = 1, column = 1)
    global image3011
    image3011 = Image.open('weld_ss/'+str(3011)+'.png')
    image3011= image3011.resize((200,150), Image.ANTIALIAS)
    image3011= ImageTk.PhotoImage(image3011)
    Label(frame3,image=image3011).grid(row= 1,column= 2)

    Label(frame3, text="3012 - Schlackeneinschluss vereinzelt: Leer in der Norm").grid(row = 1, column = 3)
    Entry(frame3, textvariable=par3012,width = 10).grid(row = 1, column = 4)
    global image3012
    image3012 = Image.open('weld_ss/'+str(3012)+'.png')
    image3012= image3012.resize((200,150), Image.ANTIALIAS)
    image3012= ImageTk.PhotoImage(image3012)
    Label(frame3,image=image3012).grid(row= 1,column= 5)

    Label(frame3, text="3013 - Schlackeneinschluss örtlich gehäuft : Leer in der Norm").grid(row = 2, column = 0)
    Entry(frame3, textvariable=par3013,width = 10).grid(row = 2, column = 1)
    global image3013
    image3013 = Image.open('weld_ss/'+str(3013)+'.png')
    image3013= image3013.resize((200,150), Image.ANTIALIAS)
    image3013= ImageTk.PhotoImage(image3013)
    Label(frame3,image=image3013).grid(row= 2,column= 2)

    Label(frame3, text="302 - Flussmitteleinschluss:\n        h ≤ 0,2 s, aber max. 2 mm \nl ≤ s, aber max. 25 mm").grid(row = 2, column = 3)
    Entry(frame3, textvariable=par302,width = 10).grid(row = 2, column = 4)
    global image302
    image302 = Image.open('weld_ss/'+str(3013)+'.png')
    image302= image302.resize((200,150), Image.ANTIALIAS)
    image302= ImageTk.PhotoImage(image302)
    Label(frame3,image=image302).grid(row= 2,column= 5)

    Label(frame3, text="3021 - Flussmitteleinschluss zeilenförmig : Leer in der Norm").grid(row = 3, column = 0)
    Entry(frame3, textvariable=par3021,width = 10).grid(row = 3, column = 1)
    global image3021
    image3021 = Image.open('weld_ss/'+str(3013)+'.png')
    image3021= image3021.resize((200,150), Image.ANTIALIAS)
    image3021= ImageTk.PhotoImage(image3021)
    Label(frame3,image=image3021).grid(row= 3,column= 2)

    Label(frame3, text="3022 - Flussmitteleinschluss vereinzelt : Leer in der Norm").grid(row = 3, column = 3)
    Entry(frame3, textvariable=par3022,width = 10).grid(row = 3, column = 4)
    global image3022
    image3022 = Image.open('weld_ss/'+str(3013)+'.png')
    image3022= image3022.resize((200,150), Image.ANTIALIAS)
    image3022= ImageTk.PhotoImage(image3022)
    Label(frame3,image=image3022).grid(row= 3,column= 5)

    Label(frame3, text="3023 -Flussmitteleinschluss örtlich gehäuft : Leer in der Norm").grid(row = 4, column = 0)
    Entry(frame3, textvariable=par3023,width = 10).grid(row = 4, column = 1)
    global image3023
    image3023 = Image.open('weld_ss/'+str(3013)+'.png')
    image3023= image3023.resize((200,150), Image.ANTIALIAS)
    image3023= ImageTk.PhotoImage(image3023)
    Label(frame3,image=image3023).grid(row= 4,column= 2)

    Label(frame3, text="303 - Oxideinschluss:\n        h ≤ 0,2 s, aber max. 2 mm \nl ≤ s, aber max. 25 mm").grid(row = 4, column = 3)
    Entry(frame3, textvariable=par303,width = 10).grid(row = 4, column = 4)
    global image303
    image303 = Image.open('weld_ss/'+str(3013)+'.png')
    image303= image303.resize((200,150), Image.ANTIALIAS)
    image303= ImageTk.PhotoImage(image303)
    Label(frame3,image=image303).grid(row= 4,column= 5)

    Label(frame3, text="3031 - Oxideinschluss zeilenförmig : Leer in der Norm").grid(row = 5, column = 0)
    Entry(frame3, textvariable=par3031,width = 10).grid(row = 5, column = 1)
    global imag3031
    imag3031 = Image.open('weld_ss/'+str(3013)+'.png')
    imag3031= imag3031.resize((200,150), Image.ANTIALIAS)
    imag3031= ImageTk.PhotoImage(imag3031)
    Label(frame3,image=imag3031).grid(row= 5,column= 2)

    Label(frame3, text="3032 - Oxideinschluss vereinzelt : Leer in der Norm").grid(row = 5, column = 3)
    Entry(frame3, textvariable=par3032,width = 10).grid(row = 5, column = 4)
    global image3032
    image3032 = Image.open('weld_ss/'+str(3013)+'.png')
    image3032= image3032.resize((200,150), Image.ANTIALIAS)
    image3032= ImageTk.PhotoImage(image3032)
    Label(frame3,image=image3032).grid(row= 5,column= 5)

    Label(frame3, text="3033 - Oxideinschluss örtlich gehäuft : Leer in der Norm").grid(row = 6, column = 0)
    Entry(frame3, textvariable=par3033,width = 10).grid(row = 6, column = 1)
    global image3033
    image3033 = Image.open('weld_ss/'+str(3013)+'.png')
    image3033= image3033.resize((200,150), Image.ANTIALIAS)
    image3033= ImageTk.PhotoImage(image3033)
    Label(frame3,image=image3033).grid(row= 6,column= 2)

    Label(frame3, text="3034 - Oxidhaut : Leer in der Norm").grid(row = 6, column = 3)
    Entry(frame3, textvariable=par3034,width = 10).grid(row = 6, column = 4)
    global image3034
    image3034 = Image.open('weld_ss/'+str(3013)+'.png')
    image3034= image3034.resize((200,150), Image.ANTIALIAS)
    image3034= ImageTk.PhotoImage(image3034)
    Label(frame3,image=image3034).grid(row= 6,column= 5)

    Label(frame3, text="304 - metallischer Einschluss:\n     h ≤ 0,2 s, aber max. 2 mm").grid(row = 7, column = 0)
    Entry(frame3, textvariable=par304,width = 10).grid(row = 7, column = 1)
    global image304
    image304 = Image.open('weld_ss/'+str(3013)+'.png')
    image304= image304.resize((200,150), Image.ANTIALIAS)
    image304= ImageTk.PhotoImage(image304)
    Label(frame3,image=image304).grid(row= 7,column= 2)

    Label(frame3, text="3041 - metallischer Einschluss Wolfram : Leer in der Norm").grid(row = 7, column = 3)
    Entry(frame3, textvariable=par3041,width = 10).grid(row = 7, column = 4)
    global image3041
    image3041 = Image.open('weld_ss/'+str(3013)+'.png')
    image3041= image3041.resize((200,150), Image.ANTIALIAS)
    image3041= ImageTk.PhotoImage(image3041)
    Label(frame3,image=image3041).grid(row= 7,column= 5)

    Label(frame3, text="3042 - metallischer Einschluss Kupfer : Nicht zulässig").grid(row = 8, column = 0)
    Entry(frame3, textvariable=par3042,width = 10).grid(row = 8, column = 1)
    global image3042
    image3042 = Image.open('weld_ss/'+str(3013)+'.png')
    image3042= image3042.resize((200,150), Image.ANTIALIAS)
    image3042= ImageTk.PhotoImage(image3042)
    Label(frame3,image=image3042).grid(row= 8,column= 2)

    Label(frame3, text="3043 - metallischer Einschluss sonstigem Metall : Leer in der Norm").grid(row = 8, column = 3)
    Entry(frame3, textvariable=par3043,width = 10).grid(row = 8, column = 4)
    global image3043
    image3043 = Image.open('weld_ss/'+str(3013)+'.png')
    image3043= image3043.resize((200,150), Image.ANTIALIAS)
    image3043= ImageTk.PhotoImage(image3043)
    Label(frame3,image=image3043).grid(row= 8,column= 5)
    
    Label(frame3, text="                                                             ").grid(row = 9, column = 0)
    Button(frame3, text="Nächste", command=lambda:insert(current_row,solid_inclusions_dict,main_frame)).grid(row=10, column=3) 
    Label(frame3, text="                                                             ").grid(row = 11, column = 0)

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
    shape_deviations_dict={75:par500,76:par501,77:par5011,78:par5012,79:par5013,80:par5014,
    81:par5015,82:par502,83:par503,84:par504,85:par5041,86:par5042,87:par5043,
    88:par505,89:par5051,90:par5052,91:par506,92:par5061,93:par5062,94:par507,
    95:par5071,96:par5072,97:par508,98:par509,99:par5091,100:par5092,101:par5093,
    102:par5094,103:par510,104:par511,105:par512,106:par513,107:par514,108:par515,
    109:par516,110:par517,111:par5171,112:par5172,113:par520,114:par521,115:par5211,
    116:par5212,117:par5213,118:par5214
    }
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
    
    Label(frame3, text="500 - Formfehler: \nLeer in der Norm ").grid(row = 0, column = 0)
    Entry(frame3, textvariable=par500,width = 10).grid(row = 0, column = 1)
    global image500
    image500 = Image.open('weld_ss/'+str(504)+'.png')
    image500= image500.resize((200,150), Image.ANTIALIAS)
    image500= ImageTk.PhotoImage(image500)
    Label(frame3,image=image500).grid(row= 0,column= 2)
    
    Label(frame3, text="501 - Einbrandkerbe:\nLeer in der Norm").grid(row = 1, column = 0)
    Entry(frame3, textvariable=par501,width = 10).grid(row = 1, column = 1)
    global image501
    image501 = Image.open('weld_ss/'+str(504)+'.png')
    image501= image501.resize((200,150), Image.ANTIALIAS)
    image501= ImageTk.PhotoImage(image501)
    Label(frame3,image=image501).grid(row= 1,column= 2)
    
    Label(frame3, text="5011 - durchlaufende Einbrandkerbe:\nh ≤ 0,05 t, aber max. 0,5 mm").grid(row = 0, column = 3)
    Entry(frame3, textvariable=par5011,width = 10).grid(row = 0, column = 4)
    global image5011
    image5011 = Image.open('weld_ss/'+str(5011)+'.png')
    image5011= image5011.resize((280,150), Image.ANTIALIAS)
    image5011= ImageTk.PhotoImage(image5011)
    Label(frame3,image=image5011).grid(row= 0,column= 5)
    
    Label(frame3, text="5012 - nicht durchlaufende Einbrandkerbe:\nh ≤ 0,05 t, aber max. 0,5 mm").grid(row = 1, column = 3)
    Entry(frame3, textvariable=par5012,width = 10).grid(row = 1, column = 4)
    global image5012
    image5012 = Image.open('weld_ss/'+str(5012)+'.png')
    image5012= image5012.resize((280,150), Image.ANTIALIAS)
    image5012= ImageTk.PhotoImage(image5012)
    Label(frame3,image=image5012).grid(row= 1,column= 5)
    
    Label(frame3, text="5013 - Wurzelkerben: Kurze Unregelmäßig-keit:\n h ≤ 0,05 t, aber max. 0,5 mm").grid(row = 2, column = 0)
    Entry(frame3, textvariable=par5013,width = 10).grid(row = 2, column = 1)
    global image5013
    image5013 = Image.open('weld_ss/'+str(5013)+'.png')
    image5013= image5013.resize((280,150), Image.ANTIALIAS)
    image5013= ImageTk.PhotoImage(image5013)
    Label(frame3,image=image5013).grid(row= 2,column= 2)

    Label(frame3, text="5014 - Längskerbe zwischen den Schweißraupen:\n Leer in der Norm").grid(row = 2, column = 3)
    Entry(frame3, textvariable=par5014,width = 10).grid(row = 2, column = 4)
    global image5014
    image5014 = Image.open('weld_ss/'+str(5014)+'.png')
    image5014= image5014.resize((200,150), Image.ANTIALIAS)
    image5014= ImageTk.PhotoImage(image5014)
    Label(frame3,image=image5014).grid(row= 2,column= 5)
    
    Label(frame3, text="5015 - örtlich unterbrochene Kerben:\nLeer in der Norm").grid(row = 3, column = 0)
    Entry(frame3, textvariable=par5015,width = 10).grid(row = 3, column = 1)
    global image5015
    image5015 = Image.open('weld_ss/'+str(5015)+'.png')
    image5015= image5015.resize((200,150), Image.ANTIALIAS)
    image5015= ImageTk.PhotoImage(image5015)
    Label(frame3,image=image5015).grid(row= 3,column= 2)
    
    Label(frame3, text="502 - zu große Nahtüberhöhung (Stumpfnaht):\n h ≤ 1 mm + 0,1 b, aber max. 5 mm").grid(row = 3, column = 3)
    Entry(frame3, textvariable=par502,width = 10).grid(row = 3, column = 4)
    global image502
    image502 = Image.open('weld_ss/'+str(502)+'.png')
    image502= image502.resize((280,150), Image.ANTIALIAS)
    image502= ImageTk.PhotoImage(image502)
    Label(frame3,image=image502).grid(row= 3,column= 5)

    Label(frame3, text="503 -zu große Nahtüberhöhung (Kehlnaht):\n h ≤ 1 mm + 0,1 b, aber max. 3 mm").grid(row = 4, column = 0)
    Entry(frame3, textvariable=par503,width = 10).grid(row = 4, column = 1)
    global image503
    image503 = Image.open('weld_ss/'+str(503)+'.png')
    image503= image503.resize((280,150), Image.ANTIALIAS)
    image503= ImageTk.PhotoImage(image503)
    Label(frame3,image=image503).grid(row= 4,column= 2)
    
    Label(frame3, text="504 - zu große Wurzelüberhöhung:\n h ≤ 1 mm + 0,2 b, aber max. 3 mm").grid(row = 4, column = 3)
    Entry(frame3, textvariable=par504,width = 10).grid(row = 4, column = 4)
    global image504
    image504 = Image.open('weld_ss/'+str(504)+'.png')
    image504= image504.resize((200,150), Image.ANTIALIAS)
    image504= ImageTk.PhotoImage(image504)
    Label(frame3,image=image504).grid(row= 4,column= 5)
    
    Label(frame3, text="5041 - örtliche Wurzelüberhöhung:\n Leer in der Norm").grid(row = 5, column = 0)
    Entry(frame3, textvariable=par5041,width = 10).grid(row = 5, column = 1)
    global imag5041
    imag5041 = Image.open('weld_ss/'+str(504)+'.png')
    imag5041= imag5041.resize((200,150), Image.ANTIALIAS)
    imag5041= ImageTk.PhotoImage(imag5041)
    Label(frame3,image=imag5041).grid(row= 5,column= 2)
    
    Label(frame3, text="5042 - durchlaufende zu große Wurzelüberhöhung:\n Leer in der Norm").grid(row = 5, column = 3)
    Entry(frame3, textvariable=par5042,width = 10).grid(row = 5, column = 4)
    global image5042
    image5042 = Image.open('weld_ss/'+str(504)+'.png')
    image5042= image5042.resize((200,150), Image.ANTIALIAS)
    image5042= ImageTk.PhotoImage(image5042)
    Label(frame3,image=image5042).grid(row= 5,column= 5)
    
    Label(frame3, text="5043 - zu große Durchschmelzung:\n Leer in der Norm").grid(row = 6, column = 0)
    Entry(frame3, textvariable=par5043,width = 10).grid(row = 6, column = 1)
    global image5043
    image5043 = Image.open('weld_ss/'+str(5043)+'.png')
    image5043= image5043.resize((200,150), Image.ANTIALIAS)
    image5043= ImageTk.PhotoImage(image5043)
    Label(frame3,image=image5043).grid(row= 6,column= 2)
    
    Label(frame3, text="505 - schroffer Nahtübergang(fehlerhaftes Nahtprofil):\n α ≥150°").grid(row = 6, column = 3)
    Entry(frame3, textvariable=par505,width = 10).grid(row = 6, column = 4)
    global image505
    image505 = Image.open('weld_ss/'+str(5051)+'.png')
    image505= image505.resize((200,150), Image.ANTIALIAS)
    image505= ImageTk.PhotoImage(image505)
    Label(frame3,image=image505).grid(row= 6,column= 5)
    
    Label(frame3, text="5051 - fehlerhafter Nahtübergangswinkel:\n Leer in der Norm").grid(row = 7, column = 0)
    Entry(frame3, textvariable=par5051,width = 10).grid(row = 7, column = 1)
    global image5051
    image5051 = Image.open('weld_ss/'+str(5051)+'.png')
    image5051= image5051.resize((200,150), Image.ANTIALIAS)
    image5051= ImageTk.PhotoImage(image5051)
    Label(frame3,image=image5051).grid(row= 7,column= 2)
    
    Label(frame3, text="5052 - fehlerhafter Nahtübergangsradius:\n Leer in der Norm").grid(row = 7, column = 3)
    Entry(frame3, textvariable=par5052,width = 10).grid(row = 7, column = 4)
    global image5052
    image5052 = Image.open('weld_ss/'+str(5052)+'.png')
    image5052= image5052.resize((200,150), Image.ANTIALIAS)
    image5052= ImageTk.PhotoImage(image5052)
    Label(frame3,image=image5052).grid(row= 7,column= 5)
    
    Label(frame3, text="506 - Schweißgutüberlauf:\n Nicht zulässig").grid(row = 8, column = 0)
    Entry(frame3, textvariable=par506,width = 10).grid(row = 8, column = 1)
    global image506
    image506 = Image.open('weld_ss/'+str(5061)+'.png')
    image506= image506.resize((200,150), Image.ANTIALIAS)
    image506= ImageTk.PhotoImage(image506)
    Label(frame3,image=image506).grid(row= 8,column= 2)
    
    Label(frame3, text="5061 - Schweißgutüberlauf an der Decklage:\n Leer in der Norm").grid(row = 8, column = 3)
    Entry(frame3, textvariable=par5061,width = 10).grid(row = 8, column = 4)
    global image5061
    image5061 = Image.open('weld_ss/'+str(5061)+'.png')
    image5061= image5061.resize((200,150), Image.ANTIALIAS)
    image5061= ImageTk.PhotoImage(image5061)
    Label(frame3,image=image5061).grid(row= 8,column= 5)
    
    Label(frame3, text="5062 - Schweißgutüberlauf auf der Wurzelseite:\n Leer in der Norm").grid(row = 9, column = 0)
    Entry(frame3, textvariable=par5062,width = 10).grid(row = 9, column = 1)
    global image5062
    image5062 = Image.open('weld_ss/'+str(5062)+'.png')
    image5062= image5062.resize((200,150), Image.ANTIALIAS)
    image5062= ImageTk.PhotoImage(image5062)
    Label(frame3,image=image5062).grid(row= 9,column= 2)
    
    Label(frame3, text="507 - Kantenverrsatz:\n Leer in der Norm").grid(row = 9, column = 3)
    Entry(frame3, textvariable=par507,width = 10).grid(row = 9, column = 4)
    global image507
    image507 = Image.open('weld_ss/'+str(5071)+'.png')
    image507= image507.resize((250,150), Image.ANTIALIAS)
    image507= ImageTk.PhotoImage(image507)
    Label(frame3,image=image507).grid(row= 9,column= 5)
    
    Label(frame3, text="5071 - Kantenversatz bei Blechen:\n h ≤ 0,1 t, aber max. 3 mm").grid(row = 10, column = 0)
    Entry(frame3, textvariable=par5071,width = 10).grid(row = 10, column = 1)
    global image5071
    image5071 = Image.open('weld_ss/'+str(5071)+'.png')
    image5071= image5071.resize((250,150), Image.ANTIALIAS)
    image5071= ImageTk.PhotoImage(image5071)
    Label(frame3,image=image5071).grid(row= 10,column= 2)
    
    Label(frame3, text="5072 - Kantenversatz bei Rohren:\n h ≤ 0,5 t, aber max. 2 mm").grid(row = 10, column = 3)
    Entry(frame3, textvariable=par5072,width = 10).grid(row = 10, column = 4)
    global image5072
    image5072 = Image.open('weld_ss/'+str(5072)+'.png')
    image5072= image5072.resize((250,150), Image.ANTIALIAS)
    image5072= ImageTk.PhotoImage(image5072)
    Label(frame3,image=image5072).grid(row= 10,column= 5)
    
    Label(frame3, text="508 - Winkelversatz:\n Leer in der Norm").grid(row = 11, column = 0)
    Entry(frame3, textvariable=par508,width = 10).grid(row = 11, column = 1)
    global image508
    image508 = Image.open('weld_ss/'+str(508)+'.png')
    image508= image508.resize((250,150), Image.ANTIALIAS)
    image508= ImageTk.PhotoImage(image508)
    Label(frame3,image=image508).grid(row= 11,column= 2)
    
    Label(frame3, text="509 - verlaufenes Schweißgut:\n Kurze Unregelmäßig- keit:\n h ≤ 0,05 t, aber max. 0,5 mm").grid(row = 11, column = 3)
    Entry(frame3, textvariable=par509,width = 10).grid(row = 11, column = 4)
    global image509
    image509 = Image.open('weld_ss/'+str(5091)+'.png')
    image509= image509.resize((150,200), Image.ANTIALIAS)
    image509= ImageTk.PhotoImage(image509)
    Label(frame3,image=image509).grid(row= 11,column= 5)
    
    Label(frame3, text="5091 - verlaufenes Schweißgut \nverlaufen in Querposition:\n Leer in der Norm").grid(row = 12, column = 0)
    Entry(frame3, textvariable=par5091,width = 10).grid(row = 12, column = 1)
    global image5091
    image5091 = Image.open('weld_ss/'+str(5091)+'.png')
    image5091= image5091.resize((150,200), Image.ANTIALIAS)
    image5091= ImageTk.PhotoImage(image5091)
    Label(frame3,image=image5091).grid(row= 12,column= 2)
    
    Label(frame3, text="5092 -verlaufenes Schweißgut \nverlaufen in Wannen–oder \nÜberkopfposition:\n Leer in der Norm").grid(row = 12, column = 3)
    Entry(frame3, textvariable=par5092,width = 10).grid(row = 12, column = 4)
    global image5092
    image5092 = Image.open('weld_ss/'+str(5092)+'.png')
    image5092= image5092.resize((200,150), Image.ANTIALIAS)
    image5092= ImageTk.PhotoImage(image5092)
    Label(frame3,image=image5092).grid(row= 12,column= 5)
    
    Label(frame3, text="5093 - verlaufenes Schweißgut \nverlaufen bei einer Kehlnaht:\n Leer in der Norm").grid(row = 13, column = 0)
    Entry(frame3, textvariable=par5093,width = 10).grid(row = 13, column = 1)
    global image5093
    image5093 = Image.open('weld_ss/'+str(5093)+'.png')
    image5093= image5093.resize((200,150), Image.ANTIALIAS)
    image5093= ImageTk.PhotoImage(image5093)
    Label(frame3,image=image5093).grid(row= 13,column= 2)
    
    Label(frame3, text="5094 -verlaufenes Schweißgut \nabschmelzen an der Kante:\n Leer in der Norm").grid(row = 13, column = 3)
    Entry(frame3, textvariable=par5094,width = 10).grid(row = 13, column = 4)
    global image5094
    image5094 = Image.open('weld_ss/'+str(5094)+'.png')
    image5094= image5094.resize((200,150), Image.ANTIALIAS)
    image5094= ImageTk.PhotoImage(image5094)
    Label(frame3,image=image5094).grid(row= 13,column= 5)
    
    Label(frame3, text="510 - Durchbrand:\n Nicht zulässig").grid(row = 14, column = 0)
    Entry(frame3, textvariable=par510,width = 10).grid(row = 14, column = 1)
    global image510
    image510 = Image.open('weld_ss/'+str(510)+'.png')
    image510= image510.resize((200,150), Image.ANTIALIAS)
    image510= ImageTk.PhotoImage(image510)
    Label(frame3,image=image510).grid(row= 14,column= 2)
    
    Label(frame3, text="511 -Decklagenunterwölbung:\n Kurze Unregelmäßig- keit: \nh ≤ 0,05 t, aber max. 0,5 mm").grid(row = 14, column = 3)
    Entry(frame3, textvariable=par511,width = 10).grid(row = 14, column = 4)
    global image511
    image511 = Image.open('weld_ss/'+str(511)+'.png')
    image511= image511.resize((280,150), Image.ANTIALIAS)
    image511= ImageTk.PhotoImage(image511)
    Label(frame3,image=image511).grid(row= 14,column= 5)
    
    Label(frame3, text="512 - übermäßige Ungleichschenkligkeit \nbei Kehlnähten:\n h ≤ 1,5 mm + 0,15 a").grid(row = 15, column = 0)
    Entry(frame3, textvariable=par512,width = 10).grid(row = 15, column = 1)
    global image512
    image512 = Image.open('weld_ss/'+str(512)+'.png')
    image512= image512.resize((200,150), Image.ANTIALIAS)
    image512= ImageTk.PhotoImage(image512)
    Label(frame3,image=image512).grid(row= 15,column= 2)
    
    Label(frame3, text="513 -unregelmäßige (Naht-) Breite:\n Leer in der Norm").grid(row = 15, column = 3)
    Entry(frame3, textvariable=par513,width = 10).grid(row = 15, column = 4)
    global image513
    image513 = Image.open('weld_ss/'+str(515)+'.png')
    image513= image513.resize((200,150), Image.ANTIALIAS)
    image513= ImageTk.PhotoImage(image513)
    Label(frame3,image=image513).grid(row= 15,column= 5)
    
    Label(frame3, text="514 - unregelmäßige Nahtzeichnung:\n Leer in der Norm").grid(row = 16, column = 0)
    Entry(frame3, textvariable=par514,width = 10).grid(row = 16, column = 1)
    global image514
    image514 = Image.open('weld_ss/'+str(515)+'.png')
    image514= image514.resize((200,150), Image.ANTIALIAS)
    image514= ImageTk.PhotoImage(image514)
    Label(frame3,image=image514).grid(row= 16,column= 2)
    
    Label(frame3, text="515 -Wurzelrückfall:\n Kurze Unregelmäßig- keit: \nh ≤ 0,05 t, aber max.0,5 mm").grid(row = 16, column = 3)
    Entry(frame3, textvariable=par515,width = 10).grid(row = 16, column = 4)
    global image515
    image515 = Image.open('weld_ss/'+str(515)+'.png')
    image515= image515.resize((200,150), Image.ANTIALIAS)
    image515= ImageTk.PhotoImage(image515)
    Label(frame3,image=image515).grid(row= 16,column= 5)
    
    Label(frame3, text="516 - Wurzelporosität:\n Nicht zulässig").grid(row = 17, column = 0)
    Entry(frame3, textvariable=par516,width = 10).grid(row = 17, column = 1)
    global image516
    image516 = Image.open('weld_ss/'+str(515)+'.png')
    image516= image516.resize((200,150), Image.ANTIALIAS)
    image516= ImageTk.PhotoImage(image516)
    Label(frame3,image=image516).grid(row= 17,column= 2)
    
    Label(frame3, text="517 -Ansatzfehler:\n Nicht zulässig").grid(row = 17, column = 3)
    Entry(frame3, textvariable=par517,width = 10).grid(row = 17, column = 4)
    global image517
    image517 = Image.open('weld_ss/'+str(517)+'.png')
    image517= image517.resize((280,150), Image.ANTIALIAS)
    image517= ImageTk.PhotoImage(image517)
    Label(frame3,image=image517).grid(row= 17,column= 5)
    
    Label(frame3, text="5171 - Ansatzfehler in der Decklage:\n Leer in der Norm").grid(row = 18, column = 0)
    Entry(frame3, textvariable=par5171,width = 10).grid(row = 18, column = 1)
    global image5171
    image5171 = Image.open('weld_ss/'+str(517)+'.png')
    image5171= image5171.resize((280,150), Image.ANTIALIAS)
    image5171= ImageTk.PhotoImage(image5171)
    Label(frame3,image=image5171).grid(row= 18,column= 2)
    
    Label(frame3, text="5172 -Ansatzfehler in der Wurzellage:\n Leer in der Norm").grid(row = 18, column = 3)
    Entry(frame3, textvariable=par5172,width = 10).grid(row = 18, column = 4)
    global image5172
    image5172 = Image.open('weld_ss/'+str(517)+'.png')
    image5172= image5172.resize((280,150), Image.ANTIALIAS)
    image5172= ImageTk.PhotoImage(image5172)
    Label(frame3,image=image5172).grid(row= 18,column= 5)
    
    Label(frame3, text="520 - zu großer Verzug:\n Leer in der Norm").grid(row = 19, column = 0)
    Entry(frame3, textvariable=par520,width = 10).grid(row = 19, column = 1)
    global image520
    image520 = Image.open('weld_ss/'+str(517)+'.png')
    image520= image520.resize((200,150), Image.ANTIALIAS)
    image520= ImageTk.PhotoImage(image520)
    Label(frame3,image=image520).grid(row= 19,column= 2)
    
    Label(frame3, text="521 -mangelhafte Abmessungen der Schweißung:\n Leer in der Norm").grid(row = 19, column = 3)
    Entry(frame3, textvariable=par521,width = 10).grid(row = 19, column = 4)
    global image521
    image521 = Image.open('weld_ss/'+str(52115212)+'.png')
    image521= image521.resize((200,150), Image.ANTIALIAS)
    image521= ImageTk.PhotoImage(image521)
    Label(frame3,image=image521).grid(row= 19,column= 5)
    
    Label(frame3, text="5211 - zu große Schweißnahtdicke:\n Leer in der Norm").grid(row = 20, column = 0)
    Entry(frame3, textvariable=par5211,width = 10).grid(row = 20, column = 1)
    global image5211
    image5211 = Image.open('weld_ss/'+str(52115212)+'.png')
    image5211= image5211.resize((200,150), Image.ANTIALIAS)
    image5211= ImageTk.PhotoImage(image5211)
    Label(frame3,image=image5211).grid(row= 20,column= 2)
    
    Label(frame3, text="5212 -zu große Schweißnahtbreite:\n Leer in der Norm").grid(row = 20, column = 3)
    Entry(frame3, textvariable=par5212,width = 10).grid(row = 20, column = 4)
    global image5212
    image5212 = Image.open('weld_ss/'+str(52115212)+'.png')
    image5212= image5212.resize((200,150), Image.ANTIALIAS)
    image5212= ImageTk.PhotoImage(image5212)
    Label(frame3,image=image5212).grid(row= 20,column= 5)
    
    Label(frame3, text="5213 - zu kleine Kehlnahtdicke:\n Nicht zulässig").grid(row = 21, column = 0)
    Entry(frame3, textvariable=par5213,width = 10).grid(row = 21, column = 1)
    global image5213
    image5213 = Image.open('weld_ss/'+str(5213)+'.png')
    image5213= image5213.resize((200,150), Image.ANTIALIAS)
    image5213= ImageTk.PhotoImage(image5213)
    Label(frame3,image=image5213).grid(row= 21,column= 2)
    
    Label(frame3, text="5214 -zu große Kehlnahtdicke:\n h ≤ 1 mm + 0,15 a,\naber max. 3 mm").grid(row = 21, column = 3)
    Entry(frame3, textvariable=par5214,width = 10).grid(row = 21, column = 4)
    global image5214
    image5214 = Image.open('weld_ss/'+str(5214)+'.png')
    image5214= image5214.resize((200,150), Image.ANTIALIAS)
    image5214= ImageTk.PhotoImage(image5214)
    Label(frame3,image=image5214).grid(row= 21,column= 5)
    
    Label(frame3, text="                                                             ").grid(row = 22, column = 0)
    Button(frame3, text="Nächste", command=lambda:insert(current_row,shape_deviations_dict,main_frame)).grid(row=23, column=3) 
    Label(frame3, text="                                                             ").grid(row = 24, column = 0)

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
    misc_dict={119:par600,120:par601,121:par602,122:par6021,123:par603,124:par604,125:par605,
               126:par606,127:par607,128:par6071,129:par6072,130:par608,131:par610,132:par6101,
               133:par613,134:par614,135:par615,136:par617,137:par618}
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
    
    Label(frame3, text="600 - Sonstige Unregelmäßigkeiten: Leer in der Norm").grid(row = 0, column = 0)
    Entry(frame3, textvariable=par600,width = 10).grid(row = 0, column = 1)
    global image600
    image600= Image.open('weld_ss/blank.png')
    image600= image600.resize((200,150), Image.ANTIALIAS)
    image600= ImageTk.PhotoImage(image600)
    Label(frame3,image=image600).grid(row= 0,column= 2)
    
    Label(frame3, text="601 - Zündstelle: Nicht zulässig").grid(row = 0, column = 3)
    Entry(frame3, textvariable=par601,width = 10).grid(row = 0, column = 4)
    global image601
    image601= Image.open('weld_ss/blank.png')
    image601= image601.resize((200,150), Image.ANTIALIAS)
    image601= ImageTk.PhotoImage(image601)
    Label(frame3,image=image601).grid(row= 0,column= 5)
    
    Label(frame3, text="602 - Spritzer: Die Zulässigkeit hängt von der Anwendung ab, \nz. B. Werkstoff, Korrosionsschutz.").grid(row = 1, column = 0)
    Entry(frame3, textvariable=par602,width = 10).grid(row = 1, column = 1)
    global image602
    image602= Image.open('weld_ss/blank.png')
    image602= image602.resize((200,150), Image.ANTIALIAS)
    image602= ImageTk.PhotoImage(image602)
    Label(frame3,image=image602).grid(row= 1,column= 2)
    
    Label(frame3, text="6021 - Wolframspritzer: Leer in der Norm").grid(row = 1, column = 3)
    Entry(frame3, textvariable=par6021,width = 10).grid(row = 1, column = 4)
    global image6021
    image6021= Image.open('weld_ss/blank.png')
    image6021= image6021.resize((200,150), Image.ANTIALIAS)
    image6021= ImageTk.PhotoImage(image6021)
    Label(frame3,image=image6021).grid(row= 1,column= 5)
    
    Label(frame3, text="603 - Ausbrechung: Leer in der Norm").grid(row = 2, column = 0)
    Entry(frame3, textvariable=par603,width = 10).grid(row = 2, column = 1)
    global image603
    image603= Image.open('weld_ss/blank.png')
    image603= image603.resize((200,150), Image.ANTIALIAS)
    image603= ImageTk.PhotoImage(image603)
    Label(frame3,image=image603).grid(row= 2,column= 2)
    
    Label(frame3, text="604 - Schleifkerbe: Leer in der Norm").grid(row = 2, column = 3)
    Entry(frame3, textvariable=par604,width = 10).grid(row = 2, column = 4)
    global image604
    image604= Image.open('weld_ss/blank.png')
    image604= image604.resize((200,150), Image.ANTIALIAS)
    image604= ImageTk.PhotoImage(image604)
    Label(frame3,image=image604).grid(row= 2,column= 5)
    
    Label(frame3, text="605 - Meißelkerbe: Leer in der Norm").grid(row = 3, column = 0)
    Entry(frame3, textvariable=par605,width = 10).grid(row = 3, column = 1)
    global image605
    image605= Image.open('weld_ss/blank.png')
    image605= image605.resize((200,150), Image.ANTIALIAS)
    image605= ImageTk.PhotoImage(image605)
    Label(frame3,image=image605).grid(row= 3,column= 2)
    
    Label(frame3, text="606 - Unterschleifung: Leer in der Norm").grid(row = 3, column = 3)
    Entry(frame3, textvariable=par606,width = 10).grid(row = 3, column = 4)
    global image606
    image606= Image.open('weld_ss/blank.png')
    image606= image606.resize((200,150), Image.ANTIALIAS)
    image606= ImageTk.PhotoImage(image606)
    Label(frame3,image=image606).grid(row= 3,column= 5)
    
    Label(frame3, text="607 - Heftnahtunregelmäßigkeit: Leer in der Norm").grid(row = 4, column = 0)
    Entry(frame3, textvariable=par607,width = 10).grid(row = 4, column = 1)
    global image607
    image607= Image.open('weld_ss/blank.png')
    image607= image607.resize((200,150), Image.ANTIALIAS)
    image607= ImageTk.PhotoImage(image607)
    Label(frame3,image=image607).grid(row= 4,column= 2)
    
    Label(frame3, text="6071 - Heftnahtunregelmäßigkeit unterbrochene \n  Raupe oder kein Einbrand: Leer in der Norm").grid(row = 4, column = 3)
    Entry(frame3, textvariable=par6071,width = 10).grid(row = 4, column = 4)
    global image6071
    image6071= Image.open('weld_ss/blank.png')
    image6071= image6071.resize((200,150), Image.ANTIALIAS)
    image6071= ImageTk.PhotoImage(image6071)
    Label(frame3,image=image6071).grid(row= 4,column= 5)
    
    Label(frame3, text="6072 - Heftnahtunregelmäßigkeit fehlerhafte \n  Heftstelle wurde überschweißt: Leer in der Norm").grid(row = 5, column = 0)
    Entry(frame3, textvariable=par6072,width = 10).grid(row = 5, column = 1)
    global image6072
    image6072= Image.open('weld_ss/blank.png')
    image6072= image6072.resize((200,150), Image.ANTIALIAS)
    image6072= ImageTk.PhotoImage(image6072)
    Label(frame3,image=image6072).grid(row= 5,column= 2)
    
    Label(frame3, text="608 - Nahtversatz gegenüberliegender Schweißraupen \n  (beidseitiges Schweißen): Leer in der Norm").grid(row = 5, column = 3)
    Entry(frame3, textvariable=par608,width = 10).grid(row = 5, column = 4)
    global image608
    image608= Image.open('weld_ss/'+str(608)+'.png')
    image608= image608.resize((200,150), Image.ANTIALIAS)
    image608= ImageTk.PhotoImage(image608)
    Label(frame3,image=image608).grid(row= 5,column= 5)
    
    Label(frame3, text="610 - Anlauffarben: Die Zulässigkeit hängt von der \n  Anwendung ab, z. B. Werkstoff, Korrosionsschutz.").grid(row = 6, column = 0)
    Entry(frame3, textvariable=par610,width = 10).grid(row = 6, column = 1)
    global image610
    image610= Image.open('weld_ss/blank.png')
    image610= image610.resize((200,150), Image.ANTIALIAS)
    image610= ImageTk.PhotoImage(image610)
    Label(frame3,image=image610).grid(row= 6,column= 2)
    
    Label(frame3, text="6101 - Verfärbung: Leer in der Norm").grid(row = 6, column = 3)
    Entry(frame3, textvariable=par6101,width = 10).grid(row = 6, column = 4)
    global image6101
    image6101= Image.open('weld_ss/blank.png')
    image6101= image6101.resize((200,150), Image.ANTIALIAS)
    image6101= ImageTk.PhotoImage(image6101)
    Label(frame3,image=image6101).grid(row= 6,column= 5)
    
    Label(frame3, text="613 - verzunderte Oberfläche: Leer in der Norm").grid(row = 7, column = 0)
    Entry(frame3, textvariable=par613,width = 10).grid(row = 7, column = 1)
    global image613
    image613= Image.open('weld_ss/blank.png')
    image613= image613.resize((200,150), Image.ANTIALIAS)
    image613= ImageTk.PhotoImage(image613)
    Label(frame3,image=image613).grid(row= 7,column= 2)
    
    Label(frame3, text="614 - Flussmittelrests: Leer in der Norm").grid(row = 7, column = 3)
    Entry(frame3, textvariable=par614,width = 10).grid(row = 7, column = 4)
    global image614
    image614= Image.open('weld_ss/blank.png')
    image614= image614.resize((200,150), Image.ANTIALIAS)
    image614= ImageTk.PhotoImage(image614)
    Label(frame3,image=image614).grid(row= 7,column= 5)
    
    Label(frame3, text="615 - Schlackenrest: Leer in der Norm").grid(row = 8, column = 0)
    Entry(frame3, textvariable=par615,width = 10).grid(row = 8, column = 1)
    global image615
    image615= Image.open('weld_ss/blank.png')
    image615= image615.resize((200,150), Image.ANTIALIAS)
    image615= ImageTk.PhotoImage(image615)
    Label(frame3,image=image615).grid(row= 8,column= 2)
    
    Label(frame3, text="617 - schlechte Passung bei Kehlnähten:  \n  h ≤ 0,5 mm + 0,1 a, aber max. 2 mm").grid(row = 8, column = 3)
    Entry(frame3, textvariable=par617,width = 10).grid(row = 8, column = 4)
    global image617
    image617= Image.open('weld_ss/'+str(617)+'.png')
    image617= image617.resize((250,150), Image.ANTIALIAS)
    image617= ImageTk.PhotoImage(image617)
    Label(frame3,image=image617).grid(row= 8,column= 5)
    
    Label(frame3, text="618 - Schwellung: Leer in der Norm").grid(row = 9, column = 0)
    Entry(frame3, textvariable=par618,width = 10).grid(row = 9, column = 1)
    global image618
    image618= Image.open('weld_ss/'+str(618)+'.png')
    image618= image618.resize((225,150), Image.ANTIALIAS)
    image618= ImageTk.PhotoImage(image618)
    Label(frame3,image=image618).grid(row= 9,column= 2)
    
    
    Label(frame3, text="                                                             ").grid(row = 10, column = 0)
    Button(frame3, text="Nächste", command=lambda:insert(current_row,misc_dict,main_frame)).grid(row=11, column=3) 
    Label(frame3, text="                                                             ").grid(row = 12, column = 0)

    
Label(frame1, text= "Bitte wählen Sie die Achsnummer").grid(row= 0, column=0)
axle_list = list(range(1,501))
axle_variable = StringVar()
axle_variable.set("---auswählen---")
axle_drop = OptionMenu(frame1,axle_variable, *axle_list,command=seam).grid(row= 1, column=0)



root.mainloop()


# In[ ]:




