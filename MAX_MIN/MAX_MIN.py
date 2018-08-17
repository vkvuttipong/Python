Allnummber = input("Enter your ค่าตัวเลขทั้งหมด: ")
print("จำนวนดตัวเลข  :" + Allnummber)

try :
    num = int(Allnummber)
    list = []

    i = 0
    while i < num :
      print("ตัวที่เลขที่ : " + str (i+1))

      x_number = input("Enter your ค่าตัวเลขทั: ")
      list.insert(i, int(x_number)) 
      i += 1


    x= 0
    v_max = 0
    v_min = max(list)

    while x < len(list) :

      if (v_min>list[x]):
          v_min = list[x]
      elif(v_max<list[x]):
          v_max = list[x]
      x += 1
      
    print ("ismin")
    print (v_min)
    print ("ismax")
    print (v_max)
except ValueError:
     print ("Oops!  That was no valid number.  Try again...")


