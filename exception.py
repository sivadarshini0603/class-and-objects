class Exception_demo:
    def divide(self):
        try:
            a=int(input("Enter a number: "))
            b=int(input("Enter another number: "))
            print("result",a/b)
        except ZeroDivisionError:
            print("You can't divide by zero")
        except TypeError:
            print("type error occured")
        except Exception:
            print("something went wrong")
obj=Exception_demo()
obj.divide()
