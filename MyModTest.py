import support
import os

support.print_func("Rahul")
fo = open("student.txt", "+r",1)
print ("Name of the file: ", fo.name)
fo.write("Hello i am wrting")
str = fo.read(20)
print ("Read String is : ", str)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
#os.mkdir("mydir")
my=os.cpu_count()


print(my)
fo.close()