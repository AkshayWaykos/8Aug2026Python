from PraticProgram.Nestedif11 import password
from Variable_DataType.datatype2 import EmpName

print("=======Enter Joining & Exit Year Of Company========")

start=input("Enter joining Years of Company = ")
end=input("Enter Exit year of company = ")

print("Congratulation for " + str(int(end) - int(start)) +  " Year of service")

print("=======Enter Admission & Pass-out Year Of collage========")

addmission=input("Enter Admission Year of College = ")
PassOut=input("Enter Pass Out Year from collage = ")

print("Graduation has been completed in "+str(int(PassOut)-int(addmission))+" Years...!")

print("=======Enter Name & surname Of Student========")

StudentName=input("Enter Student Name =")
StudentSurname=input("Enter Student Surname =")

print( str(StudentName) +"",str(StudentSurname))

print("=======Enter EmpName & EmpID ========")

EName = input("Enter Emp Name = ")
EmpID = input("Enter ID no = ")

print((str(EName) + " ",str(EmpID)))

print("=======End ========")