import yagmail
import os
import datetime
date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP("hemanthkg777@gmail.com", "Malamma@#8722")

# sent the mail
yag.send(
    to=reversed,
    subject=sub, # email subject
    contents=hash,  # email body
    attachments= filename  # file attached
)
print("Email Sent!")
