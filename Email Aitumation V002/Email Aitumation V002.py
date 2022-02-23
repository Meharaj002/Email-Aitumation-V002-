import os
import smtplib
import imghdr #JPG && PNG
from email.message import EmailMessage
import datetime as DT


#Email Log
EMAIL_ADDRESS =  'YOUR_MAIL_ADDRESS_@gmail.com' #From ***VVIP Note:give access "Less secure apps" from  your Google Account
EMAIL_PASSWORD = 'YOUR_MAIL_PASSWOARD'                    #From_pass

#collecting maillist from folder
To_Mail_Lst=[]
Rech_MailList_Path='E:\\Personal Project\\Email Automation\\Email Aitumation V002\\To_Send_Mail_List.txt'
MailFile=open(Rech_MailList_Path,'r')
MF_LinesLst=MailFile.readlines()

for mail in MF_LinesLst:
    if mail[-1]=='\n':
        To_Mail_Lst.append(mail[:-1])
    else:
        To_Mail_Lst.append(mail)
print(To_Mail_Lst)

##To_Mail_Lst=['mssiam12@gmail.com','meharaj.sami.siam@g.bracu.ac.bd']

#making Attendence in .csv
CSV_Path='E:\\Personal Project\\Email Automation\\Email Aitumation V002\\SendingMail_DateTimeAddress.csv'
def MakeAttendence(addrss='Mail_Address',date='Date',FlName='File_Name'):
    
    with open(CSV_Path, 'r+') as Attnd:
        Attnd.readlines()
        Attnd.writelines(str(addrss) + ' <:> ' + str(date) + ' <:> ' + str(FlName)+'\n')
        



#mailing Fn
def Automate_Mail(msg,File_Name):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        
        #writing .csv attendence
        PresentTime=DT.datetime.now()
        DateTime=PresentTime.strftime('%d-%m-%y <> %H:%M:%S')
        #print(DateTime)
        MakeAttendence(To_Mail_Lst,DateTime,File_Name)
        
        print('######Sended#####')

#Add Attachment
def AutoMail_attachment(FileName):
    
    #Mail Setup
    msg = EmailMessage()
    msg['Subject'] = 'Pdf sending test'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ', '.join(To_Mail_Lst)# SMTP takes multiple mail as string(,)
    
    #attachment
    with open(FileName,'rb') as f:
        File_Data=f.read()
        #print(File_Data,type(File_Data))
        
    msg.add_attachment(File_Data,maintype='application',subtype='octet-stream',filename=FileName) #maintype='application' && subtype='octet-stream', python >>> grneric bag zip type

    Automate_Mail(msg,FileName)

#File Setup
FileAdress=os.chdir('E:\\Personal Project\\Email Automation\\Email Aitumation V002\\PDF Folder\\') #folder of Pdfs

for file in os.listdir(FileAdress):
    #print(file,type(file))
    pass
    AutoMail_attachment(file)

