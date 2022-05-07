import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("ooplaunch@gmail.com", "********")
message = "Hello"
server.sendmail(
  "ooplaunch@gmail.com", 
  "rehmanisold@gmail.com", 
  message)
#server.sendmail('ooplaunch@gmail.com', 'saadnasir31@gmail.com', message)
server.quit()
print('Done')