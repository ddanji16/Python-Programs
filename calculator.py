
print("Simple Calculator\n");

print("Menu For Calculation");

print("1. add (+)\n");
print("2. subtract (-)\n");
print("3. Multiply (x)\n");
print("4. Divide (÷)\n");

option = int(input("Enter Choice: "));

if option == 1:
     print("Addition for Two numbers! \n");
     num1 = int(input("Enter First Number: "));
     num2 = int(input("Enter Second Nunmber: "));
     total = num1 + num2;
     print("Thr sum of two number is: ",total);


elif  option == 2:
     print("Subraction for Two numbers! \n");
     num1 = int(input("Enter First Number: "));
     num2 = int(input("Enter Second Nunmber: "));
     deff = num1 - num2
     print("The defference  of two number is: ",deff);

elif  option == 3:
    print("Multiply for Two numbers! \n");
    num1 = int(input("Enter First Number: "));
    num2 = int(input("Enter Second Nunmber: "));
    prod = num1 *  num2
    print("Thr product  of two number is: ",prod);

elif option == 4:
   print("Division of Two Numbers!\n ");
   num1 = int(input("Enter First Number: "));
   num2 = int(input("Enter Second Number: "));
   div = num1 / num2;
   print("The Division of Two number is: ",div);
   
   

else:
     print("Invalid Input");

     
