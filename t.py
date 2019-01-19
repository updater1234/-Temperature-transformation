print ("this programme can help you convert F temperature to C temperature or convert C temperature to F temperature")
print ("C to F mode is 1 and F to C mode is 2")
choose = int(input("please enter your choice:"))
if choose == 1 :
  C = float(input("please enter F temperature:"))
  a = C * 1.8
  FFINAL = a + 32
  print("The F temperature is:")
  print (FFINAL)

if choose == 2 :
    F = float(input("please enter F temperature:"))
    a = F - 32
    CFINAL = a / 1.8
    print ("The C temperature is:")
    print (CFINAL)
