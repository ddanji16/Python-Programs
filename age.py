

print("Age Caclculation!\n");

print("1. know your Age by Year your are born!");
print("2. knoe your Year of Born by your Current Age");

born  = int(input("Enter Year you are Born: "));


sum = 2025 - born ;


print("Your age is: ",sum);

if sum <= 17:
      print("Your are Under Age still a Minor");

else:
      print("Your are Old enough and mature");
