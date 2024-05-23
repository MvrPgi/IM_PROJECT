from mysql_config import dbConfig
import mysql.connector as mysql
from tkinter import messagebox

class Applicant_Details:
    


      def __init__(self):
          self.con = mysql.connect(**dbConfig)
          self.cursor = self.con.cursor()
          print("You have connected to the  database")
          print(self.con)

      def __del__(self): 
        self.con.close()
        print("You have disconnected to the  database")

      def insert(self,Application_Status, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion,Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome,Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome):
          query = "INSERT INTO Applicant_Details (Application_Status, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
          data = (Application_Status, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome)
          self.cursor.execute(query, data)
          self.con.commit()
          messagebox.showinfo(title="PCSCO TABLE",message=" NEW RECORD ADDED SUCCESSFULLY")        