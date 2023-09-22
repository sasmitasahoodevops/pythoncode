class student:
    def study(self):
        print("i am studying in class 8 ")
class student1:

    def  study(self):
        print("i love mathematics")
class studentt(student,student1):
    pass
    #def position(self):
        #print("i secured 1st position:")

student2=studentt ()
student2.study()

