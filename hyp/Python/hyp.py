#!/usr/bin/env python3

## before we get ahead of ourselves, lets look at how classes work:
class myClass(object):

    # self.instance_variable = value #value specific to instance
    # class_variable = value #value shared across all class instances

    class_var = 10

    def __init__(self, instance_var):
        #init is called when you first create a myClass
        #init is know as the constructor function
        self.instance_var = instance_var

    def bypassClassMethod(self):
        #if you aren't going to use the function just yet, 
        #use pass, 
        #it bypasses the method
        pass

    def myClassMethod(self):
        #all methods in classes take self as an argument
        print(self.class_var)

    def changeClass_var(self, class_var):
        self.class_var = class_var



def main():

    #create newClass with instance_var = 20
    newClass = myClass(20)
    print(newClass.instance_var)
    #> 20
    print(newClass.class_var)
    #> 10

    #create newClass with instance_var = 35
    newClass_1 = myClass(35)
    print(newClass_1.instance_var)
    #> 35 this time
    print(newClass_1.class_var)
    #> also 10

    #calling a method is much like a variable
    newClass_2 = myClass(45)
    newClass_2.myClassMethod()
    #>prints 10

    #but you can also senf args
    newClass_2.changeClass_var(25)
    newClass_2.myClassMethod()
    #> prints 25 this time

    newClass_1.myClassMethod()
    #> this is still 10

if __name__ == '__main__':
    main()


