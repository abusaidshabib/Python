#Pass a Function as parameter
def disp(sh):
    return "Disp Function" + sh()

def show():
    return "SHow Function"

print(disp(show))


#Function return another function
def disp():
    def show():
        return "Show Function"
    print("Disp Function")
    return show

r_sh = disp()
print(r_sh())