while True: 
        print("Choose Converter Menu!\n");
        print("1. Peso to Dollor.\n");
        print("2. Dollor to Peso.\n");
        print("3. exit.\n");


        choice = int(input("Enter Choice: "));

        if choice == 1:
                 peso = int(input("Enter amount of Peso: "));
                 dollor = peso /  56;
                 print("The Amount of Peso to Dollor is: " + str(dollor) + " Dollor");
        elif choice ==2:
                 dollor = int(input("Enter Amount of  Dollor: "));
                 peso = dollor *  56;
                 print("Thr Amount of Dollor to Peso is: " + str(peso) + " Peso");

        elif choice == 3:
                print("Exit successfully!");
                break;
      
        else:
             print("Invalid Input");

   
      
