import smtplib as s

ob=s.SMTP("smtp.gmail.com",587)
ob.ehlo()#server function 
ob.starttls()#server funtion to conect with server 
ob.login("sbborfarooq@gmail.com","robbas@12345")
#now creating the subject and body of email 
subject="test python "
body="hi how are you ?"
message="subject:{}\n\n{}".format(subject,body)
#to whom you want to send making list
# listadd=[ "designerr53@gmail.com "]
ob.sendmail('sbborfarooq@gmail.com','designerr53@gmail.com',message)
print('mail send successfully')
ob.quit()
