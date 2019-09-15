#Problem 1.7
#the inputs of the tankSize, milesTraveled and gallonsLeft
print "Tank size?: \n";
$tankSize = <>;
print "How many miles have you traveled?: \n";
$milesTraveled = <>;
print "How many gallons do you have left?: \n";
$gallonsLeft = <>;

#the calculation for miles per gallon
$mpg = ($milesTraveled /($tankSize - $gallonsLeft));

#the "mpg * tankSize" checks to see how many more miles you can go till you need to fill your tank
$fullTank = ($mpg * $tankSize);

#round is used to print only one decimal place
print "You can drive $fullTank miles before you need to fill your tanks.\n\n";