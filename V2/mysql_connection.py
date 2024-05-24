from mysql_config import dbConfig
import mysql.connector as mysql
from tkinter import messagebox

class DatabaseConnection:
  def __init__(self):
    self.con = mysql.connect(**dbConfig)
    self.cursor = self.con.cursor()
    print("You have connected to the  database")
    print(self.con)

  def __del__(self): 
    self.con.close()
    print("You have disconnected to the  database")
#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------APPLICANT DETAILS--------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
  def insert(self,Application_Status, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion,Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome,Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome):
    query = "INSERT INTO Applicant_Details (Application_Status, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome) VALUES (%(Application_Status)s, %(Full_Name)s, %(Address)s, %(Civil_Status)s, %(Birth_Date)s, %(Age)s, %(Sex)s, %(Nationality)s, %(Religion)s, %(Highest_Educ_Attainment)s, %(Occupation)s, %(Monthly_Income)s, %(Membership)s, %(OtherSourceOfIncome)s, %(Monthly_Expenditures)s, %(GrossMonthlyIncome)s, %(NetMonthlyIncome)s)"
    data = {
      "Application_Status": Application_Status,
      "Full_Name": Full_Name,
      "Address": Address,
      "Civil_Status": Civil_Status,
      "Birth_Date": Birth_Date,
      "Age": Age,
      "Sex": Sex,
      "Nationality": Nationality,
      "Religion": Religion,
      "Highest_Educ_Attainment": Highest_Educ_Attainment,
      "Occupation": Occupation,
      "Monthly_Income": Monthly_Income,
      "Membership": Membership,
      "OtherSourceOfIncome": OtherSourceOfIncome,
      "Monthly_Expenditures": Monthly_Expenditures,
      "GrossMonthlyIncome": GrossMonthlyIncome,
      "NetMonthlyIncome": NetMonthlyIncome
    }
    self.cursor.execute(query, data)
    self.con.commit()
    messagebox.showinfo(title="PCSCO TABLE",message=" NEW RECORD ADDED SUCCESSFULLY")     
#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------GET LAST APPLICANT ID----------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
  def get_last_applicant_id(self):
    last_applicant_id_query = "SELECT LAST_INSERT_ID()"
    self.cursor.execute(last_applicant_id_query)
    last_applicant_id = self.cursor.fetchone()
    return last_applicant_id[0]
#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------HOUSEHOLD DETAILS--------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
  def insert(self,Hhold_Fam_Name, Hhold_Fam_Age, Hhold_Fam_CivilStatus, Hhold_Fam_RSWithPatient, Hhold_Fam_HighestEducAttain, Hhold_Fam_Occupation, Hhold_Fam_MonthlyIncome):
    household_query = "INSERT INTO Household_Details (Applicant_ID, Hhold_Fam_Name, Hhold_Fam_Age, Hhold_Fam_CivilStatus, Hhold_Fam_RSWithPatient, Hhold_Fam_HighestEducAttain, Hhold_Fam_Occupation, Hhold_Fam_MonthlyIncome) VALUES (%(Applicant_ID)s, %(Hhold_Fam_Name)s, %(Hhold_Fam_Age)s, %(Hhold_Fam_CivilStatus)s, %(Hhold_Fam_RSWithPatient)s, %(Hhold_Fam_HighestEducAttain)s, %(Hhold_Fam_Occupation)s, %(Hhold_Fam_MonthlyIncome)s)"
    last_applicant_id = self.get_last_applicant_id()
    household_data = {
        "Applicant_ID": last_applicant_id,
        "Hhold_Fam_Name": Hhold_Fam_Name,
        "Hhold_Fam_Age": Hhold_Fam_Age,
        "Hhold_Fam_CivilStatus": Hhold_Fam_CivilStatus,
        "Hhold_Fam_RSWithPatient": Hhold_Fam_RSWithPatient,
        "Hhold_Fam_HighestEducAttain": Hhold_Fam_HighestEducAttain,
        "Hhold_Fam_Occupation": Hhold_Fam_Occupation,
        "Hhold_Fam_MonthlyIncome": Hhold_Fam_MonthlyIncome
    }
    self.cursor.execute(household_query, household_data)
    self.con.commit()
    messagebox.showinfo(title="PCSCO TABLE",message=" NEW RECORD ADDED SUCCESSFULLY")

#--------------------------------------------------------------------------------------------------------------------------------------------------------  
#-------------------------------------------------------REFERENCE DETAILS--------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
  def insert(self, ReferenceNo, Date, ApplicantStatus):
    query = "INSERT INTO Reference_Details (ReferenceNo, Applicant_ID, Date, Applicant, Status) VALUES (%(ReferenceNo)s, %(Applicant_ID)s, %(Date)s, %(Status)s)"
    last_applicant_id = self.get_last_applicant_id()
    data = {
      "ReferenceNo": ReferenceNo,
      "Applicant_ID": last_applicant_id,
      "Date": Date,
      "Status": ApplicantStatus
    }
    self.cursor.execute(query, data)
    self.con.commit()
    messagebox.showinfo(title="PCSCO TABLE",message=" NEW RECORD ADDED SUCCESSFULLY")

      
            