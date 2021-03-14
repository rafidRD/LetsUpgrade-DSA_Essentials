      # Question #
# Implement Linear Search using python.

Dy_Data = input("For Admin/API Only! Update the cabs present in the area: ").split()

user = input("Enter the cab's code: ")

def search():
        for i in range(len(Dy_Data)):
            if Dy_Data[i] == user:
                print("Cab found at",i, "KM distance.")
                return
        
            else:
                print("Cab not found at",i, "KM distance.")
search()

