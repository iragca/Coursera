// Given variables
const dishData = [
  {
    name: "Italian pasta",
    price: 9.55,
  },
  {
    name: "Rice with veggies",
    price: 8.65,
  },
  {
    name: "Chicken with potatoes",
    price: 15.55,
  },
  {
    name: "Vegetarian Pizza",
    price: 6.45,
  },
];
const tax = 1.2;

// Step 1: Define the getPrices function
function getPrices(taxBoolean) {
  // Step 2: Loop over the dishData array
  for (let dish of dishData) {
    // Step 3: Declare finalPrice without assigning a value
    let finalPrice;

    // Step 4: Check if taxBoolean is true
    if (taxBoolean === true) {
      finalPrice = dish.price * tax; // Calculate price with tax
    }
    // Step 5: Check if taxBoolean is false
    else if (taxBoolean === false) {
      finalPrice = dish.price; // Use the price as-is
    }
    // Step 6: Handle invalid taxBoolean
    else {
      console.log("You need to pass a boolean to the getPrices call!");
      return; // Exit the function
    }

    // Step 7: Log the dish name and price
    console.log(`Dish: ${dish.name} Price: $${finalPrice}`);
  }
}

// Step 8: Define the getDiscount function
function getDiscount(taxBoolean, guests) {
  // Step 9: Invoke getPrices with taxBoolean
  getPrices(taxBoolean);

  // Step 10: Defensive check for guests
  if (typeof guests === "number" && guests > 0 && guests < 30) {
    // Step 11: Calculate discount
    let discount = 0;

    if (guests < 5) {
      discount = 5;
    } else if (guests >= 5) {
      discount = 10;
    }

    console.log("Discount is: $" + discount);
  } else {
    // Step 12: Handle invalid guests value
    console.log("The second argument must be a number between 0 and 30");
  }
}

// Example invocations
getDiscount(true, 2); // Should calculate with tax and 5% discount
getDiscount(false, 10); // Should calculate without tax and 10% discount
