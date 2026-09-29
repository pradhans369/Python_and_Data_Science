# how to call a method form a child if there is the case of multiple inheritence and all parents and child has the same method

class Dad:
    def show(self):
        print("Hii from Dad")

class Mom:
    def show(self):
        print("Hii from Mom")

# Order matters here: Dad comes first, then Mom
class Student(Dad, Mom):
    def show(self):
        print("Hii from Child")



# ------------------------------------------------------------------



s1 = Student()

# show from child
s1.show()

# show from dad
super(Student, s1).show()
# When we wrote super(Student, s1), it went to the sequence of inheritence (Dad, Mom)
# Since Dad was right to Student, it printed show from Dad

# show form mom
super(Dad, s1).show()
# Since Mom was right to Dad, it printed show from Mom


