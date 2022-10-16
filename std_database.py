class Faculty:

  def __init__(self,subject,teacher):
    self.subject = subject
    self.teacher = teacher


sub1=Faculty("Physics","Mr. KS Ojha")
sub2=Faculty("Chemistery","Mrs. Nariman Khan")
sub3=Faculty("Maths","Mrs. Ambika Sahu")
sub4=Faculty("English","Mrs Jaya Diwedi")
sub5=Faculty("Drawing","Mrs. Sangeeta Singh")
sub6=Faculty("Computer","!EMPTY POST!")
sub7=Faculty("extra subject1 here","newly assigned faculty1 here")
sub8=Faculty("extra subject2 here","newly assigned faculty2 here")

print("Following subjects are avialable in our intitute:\n")
print(sub1.subject)
print(sub2.subject)
print(sub3.subject)
print(sub4.subject)
print(sub5.subject)
print(sub6.subject)
print("\n\n")


print("Following are the name of respective assigned teacher against there respective subjects:")
print("     Note-If any subject has !EMPTY POST! then the user can apply\n ^_^GOOD LUCK^_^\n")
print(sub1.__dict__)
print(sub2.__dict__)
print(sub3.__dict__)
print(sub4.__dict__)
print(sub5.__dict__)
print(sub6.__dict__)
print("\n\n")

#addition of subjects
sub7.subject=input("Please enter optional subject1 here:")
sub7.teacher=input("Please enter name of newly assigned faculty1 here:")
sub8.subject=input("Please enter optional subject2 here:")
sub8.teacher=input("Please enter name of newly assigned faculty2 here:")
print("\n\n")
print("Newley assigned faculty in respectivec subjects are:")
print(sub7.__dict__)
print(sub8.__dict__)
print("\n \n")

#list of subjects
SUB=[sub1.subject,sub2.subject,sub3.subject,sub4.subject,sub5.subject,sub6.subject,sub7.subject,sub8.subject]

#list of Respective faculties
FAC=[sub1.teacher,sub2.teacher,sub3.teacher,sub4.teacher,sub5.teacher,sub6.teacher,sub7.teacher,sub8.teacher]

#Filling of empty post
if "!EMPTY POST!" in FAC:
  print(sub6.subject+" has a empty post for faculty")
  print("Eligible candidate can apply for this job.\n")
  input("Name:")
  input("Age:")
  input("DOB:")
  input("Gender:")
  input("Qualification:")
  input("Contact Number:")
  input("E-Mail ID:")
  input("Past experience (IF ANY) :")
  print("Thanks\nData has been recorded.")
  

#Resignation Of Faculty
leave1=input("Name of faculty who wants to leave:")
if leave1 in FAC:
  print("Resignation letter for "+leave1+" has been recorded.\nTHANK YOU!\n")
  levsub=input("Please enter the subject s/he taught:")
  if levsub in SUB:
    print(levsub+" has an empty post for Faculty.\n")
  else:
      print("Error\n No subject fount with this name.")
else:
  print("Error\n No faculty found with this name\n")

if leave1 in FAC:
  reason=input("Why you are leaving this job?\n")
  feedback=input("We appreciate your valuble feedback!\n*_*THANK YOU*_*")

#Filling up of last resigned post.
  print(levsub +" has an empty post,\n eligble candidate can apply by filling up form.\n")
  name=input("Name of eligible candidate:")
  DOB=input("Date of birth:")
  Ag=input("Age:")
  Gen=input("Gender:")
  Qua=input("Qualification:")
  Ph=input("Contact Number:")
  email=input("E-mail address:")

  print("\n\nThank You\n\nYour apllication has been collected.")
  print("                        We may contact you sortly.")
else:
  print("\n\nNO EMPTY POST\n\n")
  print("^-^                                            THANK YOU                                            ^-^")
