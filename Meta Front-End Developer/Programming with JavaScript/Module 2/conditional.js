var age = -2;

if (age >= 65) {
  console.log("You get your income from your pension");
} else if (18 <= age && age < 65) {
  console.log("Each month you get a salary");
} else if (age < 18 && age >= 0) {
  console.log("You get an allowance");
} else {
  console.log("The value of the age variable is not valid");
}

var day = 0;

switch (day) {
  case 0:
    console.log("This number is an integer of 0");
    break;
  case "Tuesday":
    console.log("Do something");
    break;
  case "Wednesday":
    console.log("Do something");
    break;
  case "Thursday":
    console.log("Do something");
    break;
  case "Friday":
    console.log("Do something");
    break;
  case "Saturday":
    console.log("Do something");
    break;
  case "Sunday":
    console.log("Do something");
    break;
}
