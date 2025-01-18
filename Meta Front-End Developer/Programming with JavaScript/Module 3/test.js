const car = {
    engine: true
}

const sportsCar = Object.create(car);
sportsCar.turbo = true;

for (prop in Object.keys(sportsCar)) {
    console.log(prop);
}
