import sys
import os
import tkinter as tk
from tkinter import PhotoImage, messagebox, Entry, Radiobutton


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



class Register(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)



        #LOAD THE IMAGES
        self.image_image_1 = PhotoImage(file=resource_path("resources/APP_1/image_1.png"))  
        self.image_entry_3 = PhotoImage(file=resource_path("resources/APP_1/entry_3.png"))
        self.image_entry_5 = PhotoImage(file=resource_path("resources/APP_1/entry_5.png"))
        self.image_image_6 = PhotoImage(file=resource_path("resources/APP_1/image_6.png"))
        self.image_entry_11 = PhotoImage(file=resource_path("resources/APP_1/entry_11.png"))
        self.image_entry_12 = PhotoImage(file=resource_path("resources/APP_1/entry_12.png"))    
        self.image_entry_9 = PhotoImage(file=resource_path("resources/APP_1/entry_9.png"))
        self.image_entry_16 = PhotoImage(file=resource_path("resources/APP_1/entry_16.png"))
        self.button_image_1 = PhotoImage(file=resource_path("resources/APP_1/button_1.png"))
       
        
        #BACKGROUND IMAGE
        self.create_image(120.0, 150.5, image=self.image_image_6)
        self.create_image(405.0, 46.0, image=self.image_image_1)

        #ENTRY IMAGES
        self.pageImage1_id = [] # Store the image ids to hide them later
        self.pageImage1_id.append(self.create_image(409.0, 190.5, image=self.image_entry_3))
        self.pageImage1_id.append(self.create_image(409.0, 237.5, image=self.image_entry_3))
        self.pageImage1_id.append(self.create_image(397.0, 120.5, image=self.image_entry_11))
        self.pageImage1_id.append(self.create_image(155.5, 120.5, image=self.image_entry_11))
        self.pageImage1_id.append(self.create_image(120.5, 310.5, image=self.image_entry_5))
        self.pageImage1_id.append(self.create_image(298.5, 310.5, image=self.image_entry_5))
        self.pageImage1_id.append(self.create_image(120.5, 340.5, image=self.image_entry_5))
        self.pageImage1_id.append(self.create_image(298.5, 340.5, image=self.image_entry_5))
        self.pageImage1_id.append(self.create_image(490.5, 342.5, image=self.image_entry_5))
        self.pageImage1_id.append(self.create_image(120.5, 410.5, image=self.image_entry_5))
        self.pageImage1_id.append(self.create_image(280.5, 410.5, image=self.image_entry_16))
        self.pageImage1_id.append(self.create_image(472.5, 410.5, image=self.image_entry_16))
        self.pageImage1_id.append(self.create_image(612.5, 410.5, image=self.image_entry_16))
        self.pageImage1_id.append(self.create_image(750.5, 410.5, image=self.image_entry_16))      

        
        #CREATE THE TEXTS OF FIRST PAGE
        self.PageText1_id = []     
        self.PageText1_id.append(self.create_text(49.0, 100.0, anchor="nw", text="Reference No:", fill="#000000", font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(289.0, 100,anchor ="nw", text="Date:",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(550.0, 100.0,anchor ="nw", text="Applicant Status:",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(49.0,172.0,anchor ="nw", text="Full Name Of The Patient    ",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(87.0,203.0,anchor ="nw", text="Surname",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(385., 205,anchor ="nw", text="First Name", fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(691.0,204,anchor ="nw", text="Middle Name",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(49.0, 219.0,anchor ="nw", text="Permanent Address",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(87.0, 250.0,anchor ="nw", text="No",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(120.0, 250.0,anchor ="nw", text="Street",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(180.0, 250.0,anchor ="nw", text="Barangay",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(320.0, 250.0,anchor ="nw", text="Municipality/City",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(500.0, 250.0,anchor ="nw", text="Province",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(700, 250.0,anchor ="nw", text="Region",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(49.0, 265.0,anchor ="nw", text="Civil Status",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(49.0, 290.0,anchor ="nw", text="Birthdate:",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(227.0, 290.0,anchor ="nw", text="Age:",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(420.0, 290.0,anchor ="nw", text = "Sex",fill="#000000",font=("Mada Regular", 10 * -1)))      
        self.PageText1_id.append(self.create_text(49.0, 321.5,anchor ="nw", text = "Nationality",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(227.0, 321.5,anchor ="nw", text = "Religion",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(49.0, 353, anchor ="nw", text = "Highest Educational Attainment",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(420.0, 321, anchor ="nw", text = "Occupation",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(650.0, 321, anchor ="nw", text = "Membership",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(49.0, 390, anchor ="nw", text = "Monthly Income",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(227.0, 390, anchor ="nw", text = "Other Sources Of Income",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(420.0, 390, anchor ="nw", text = "Monthly Expenditure",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(559.0, 390, anchor ="nw", text = "Gross Monthly Income",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(700.0, 390, anchor ="nw", text = "Net Monthly Income",fill="#000000",font=("Mada Regular", 10 * -1)))

# RADIO BUTTON
        self.Applicant_Status = tk.StringVar() 
        self.Applicant_Status.set("New Applicant")
        self.Civil_Status = tk.StringVar()
        self.Civil_Status.set("Single  ")
        self.Membership = tk.StringVar()
        self.Membership.set("Member")
        self.Sex = tk.StringVar()
        self.Sex.set("Female")
        self.Highest_Educational_Attainment = tk.StringVar()
        self.Highest_Educational_Attainment.set("None")

        self.New_Status = Radiobutton(
            self,
            text="New",
            bg="#FFFFFF",
            fg="#000716",
            activebackground="#FFFFFF",
            activeforeground="#000716",
            borderwidth=0,
            highlightthickness=0,
            value="New Applicant",
            variable=self.Applicant_Status,
        )

        self.Old_Status = Radiobutton(
            self,
            text="Old",
            bg="#FFFFFF",
            fg="#000716",
            activebackground="#FFFFFF",
            activeforeground="#000716",
            borderwidth=0,
            highlightthickness=0,
            value="Old Applicant",
            variable=self.Applicant_Status,
        )
        self.New_Status.place(
                x=550.0,
                y=115.5,
                width=50.0,
                height=10.0
                )
        self.Old_Status.place(
                x=640.0,
                y=115.5,
                width=50.0,
                height=10.0
                )
        self.Single = Radiobutton(        
            self,
            text="Single",
            bg="#FFFFFF",
            fg="#000716",
            activebackground="#FFFFFF",
            activeforeground="#000716",
            borderwidth=0,
            highlightthickness=0,
            value="Single",
            variable=self.Civil_Status,
            font=("Mada Regular", 10 * -1)
        )
        self.Widow = Radiobutton(
                self,
                text="Widow",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="Widow",
                variable=self.Civil_Status,
                font=("Mada Regular", 10 * -1)
                )
        self.Married = Radiobutton(
                self,
                text="Married",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="Married",
                variable=self.Civil_Status,
                font=("Mada Regular", 10 * -1)
                )
        self.Separated = Radiobutton(
                self,
                text="Separated",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="Separated",
                variable=self.Civil_Status,
                font=("Mada Regular", 10 * -1)
                )
        self.With_Partner = Radiobutton(
                self,
                text="With Partner",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="With Partner",
                variable=self.Civil_Status,
                font=("Mada Regular", 10 * -1)
                )
        # CIVIL STATUS PLACE
        self.Single.place(
                x=49.0,
                y=275.5,
                width=60.0,
                height=15.0
                )
        self.Widow.place(
                x=170.0,
                y=275.5,
                width=60.0,
                height=15.0
                )
        self.Married.place(
                x=270.0,
                y=275.5,
                width=60.0,
                height=15.0
                )
        self.Separated.place(
                x=370.0,
                y=275.5,
                width=70.0,
                height=15.0
                )
        self.With_Partner.place(
                x=470.0,
                y=276.5,
                width=80.0,
                height=15.0
                )
        self.Male = Radiobutton(
                self,
                text = "Male",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value = "Male",
                variable= self.Sex,
                font=("Mada Regular", 10 * -1)
                )
        self.Female = Radiobutton(
                self,
                text ="Female",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value = "Female",       
                variable = self.Sex,
                font=("Mada Regular", 10 * -1)
                ) 
        self.Male.place(
                x=410.0,
                y=305.5,
                width=60.0,
                height=15.0
        )       
        self.Female.place(
                x=500.0,
                y=305.5,
                width=60.0,
                height=15.0
        )

        self.Post_Graduate = Radiobutton(
                self,
                text="Post Graduate",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="Post Graduate",
                variable=self.Highest_Educational_Attainment,
                font=("Mada Regular", 10 * -1)
                )
        self.College = Radiobutton(
                self,
                text="College",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="College",
                variable=self.Highest_Educational_Attainment,
                font=("Mada Regular", 10 * -1)
                )
        self.Elementary_School = Radiobutton(
                self,
                text="Elementary",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="Elementary",
                variable=self.Highest_Educational_Attainment,
                font=("Mada Regular", 10 * -1)
                )
        self.Vocational = Radiobutton(
                self,
                text="Vocational",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="Vocational",
                variable=self.Highest_Educational_Attainment,
                font=("Mada Regular", 10 * -1)
                )
        self.High_School = Radiobutton(
                self,
                text="High School",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="High School",
                variable=self.Highest_Educational_Attainment,
                font=("Mada Regular", 10 * -1)
                )
        self._None = Radiobutton(
                self,
                text="None",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="None",
                variable=self.Highest_Educational_Attainment,
                font=("Mada Regular", 10 * -1)
                )
        self.Post_Graduate.place(
                x=49.0,
                y=375.5,
                width=100.0,
                height=15.0
                )
        self.College.place(
                x=170.0,
                y=375.5,
                width=60.0,
                height=15.0
                )
        self.Elementary_School.place(
                x=270.0,
                y=375.5,
                width=80.0,
                height=15.0
                )
        self.Vocational.place(
                x=370.0,
                y=375.5,
                width=80.0,
                height=15.0
                )
        self.High_School.place(
                x=470.0,
                y=375.5,
                width=80.0,
                height=15.0
                )
        self._None.place(
                x=570.0,
                y=375.5,
                width=60.0,
                height=15.0
                )
        

        self.Member = Radiobutton(
                self,
                text="Member",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="Member",
                variable=self.Membership,
                font=("Mada Regular", 10 * -1)
                )
        self.Non_Member = Radiobutton(
                self,
                text="Non-Member",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="Non-Member",
                variable=self.Membership,
                font=("Mada Regular", 10 * -1)
                )
        self.Dependent = Radiobutton( 
                self,
                text="Dependent",
                bg="#FFFFFF",
                fg="#000716",
                activebackground="#FFFFFF",
                activeforeground="#000716",
                borderwidth=0,
                highlightthickness=0,
                value="Dependent",
                variable=self.Membership,
                font=("Mada Regular", 10 * -1)
                )
        #MEMBERSHIP PLACE
        self.Member.place(
                x=585.0,
                y=335.5,
                width=59.0,
                height=15.0
                )
        self.Non_Member.place(
                x=655.0,
                y=335.5,
                width=75.0,
                height=15.0
                )
        self.Dependent.place(
                x=730.0,
                y=335.5,
                width=80.0,
                height=15.0
                )
        
        


    # Creating and placing the entry widget of the first page
        self.Reference_No = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Reference_No.place(  
        x=50.0,
        y=115.5,
        width=210.0,
        height=10.0
)
        self.Date = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Date.place(
        x=290.0,
        y=115.5,
        width=208.0,
        height=10.0
)
        self.FullName = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.FullName.place(
        x=53.0,
        y=185.5,
        width=712.0,
        height=10.0
)

        self.Permanent_Address = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Permanent_Address.place(
        x = 52.0,
        y = 232.5,
        width=716.0,
        height=10.0
)
        self.Birthdate = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)       
        self.Birthdate.place(
        x=52.0,
        y=305.5,
        width=142.0,
        height=10.0
)   
        self.Age = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Age.place(
        x=230.0,
        y=305.5,
        width=140.0,
        height=10.0
)
        self.Nationality = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Nationality.place(
        x=52.0,
        y=335.5,
        width=142.0,
        height=10.0
)
        self.Religion = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Religion.place(
        x=230.0,
        y=335.5,
        width=142.0,
        height=10.0
)
        self.Occupation = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Occupation.place(
        x=420.0,
        y=335.5,
        width=142.0,
        height=10.0
)

        self.Monthly_Income = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Monthly_Income.place(
        x=52.0,
        y=405.5,
        width=110.0,
        height=10.0
)
        self.Other_Sources_Of_Income = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Other_Sources_Of_Income.place(
        x=230.0,
        y=405.5,
        width=105.0,
        height=10.0
)
        self.Monthly_Expenditure = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Monthly_Expenditure.place(
        x=420.0,
        y=405.5,
        width=105.0,
        height=10.0
)
        self.Gross_Monthly_Income = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Gross_Monthly_Income.place(
        x=559.0,
        y=405.5,
        width=105.0,
        height=10.0
)
        self.Net_Monthly_Income = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Net_Monthly_Income.place(
        x=700.0,
        y=405.5,
        width=105.0,
        height=10.0
)

        # Creating and placing the button widget
        self.button_1 = tk.Button(
        image=self.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command = self.hide
      
)
        self.button_1.place(
        x=635.0,
        y=450.0,
        width=100.0,
        height=30.0
)
#         self.button_2 = tk.Button(
#         image=self.button_image_1,
#         borderwidth=0,
#         highlightthickness=0,
#         command = self.show
# )   
#         self.button_2.place(
#         x=505.0,
#         y=450.0,
#         width=100.0,
#         height=30.0
# )
# 2ND PAGE
            
# HIDE THE WIDGETS
    def hide(self):
            for image_id in self.pageImage1_id:
                self.itemconfigure(image_id, state="hidden")
            for text_id in self.PageText1_id:
                self.itemconfigure(text_id, state="hidden")
            self.Reference_No.place_forget()
            self.Date.place_forget()
            self.FullName.place_forget()
            self.Permanent_Address.place_forget()
            self.Birthdate.place_forget()
            self.Age.place_forget()
            self.Nationality.place_forget()
            self.Religion.place_forget()
            self.Occupation.place_forget()
            self.Monthly_Income.place_forget()
            self.Other_Sources_Of_Income.place_forget()
            self.Monthly_Expenditure.place_forget()
            self.Gross_Monthly_Income.place_forget()
            self.Net_Monthly_Income.place_forget()


    
# # SHOW THE WIDGETS
#     def show(self):

#         for image_id in self.pageImage1_id:
#             self.itemconfigure(image_id, state="normal")
#         for text_id in self.PageText1_id:
#             self.itemconfigure(text_id, state="normal")
#             self.Reference_No.place()
#             self.Date.place()
#             self.FullName.place()
#             self.Permanent_Address.place()
#             self.Birthdate.place()
#             self.Age.place()
#             self.Nationality.place()
#             self.Religion.place()
#             self.Occupation.place()
#             self.Monthly_Income.place()
#             self.Other_Sources_Of_Income.place()
#             self.Monthly_Expenditure.place()
#             self.Gross_Monthly_Income.place()
#             self.Net_Monthly_Income.place()     
     





            

        
       

    
