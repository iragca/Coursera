function compute()
{
    principal_amount = parseInt(document.getElementById("principal").value);
    interest_rate = parseFloat(document.getElementById("rate").value);
    num_of_years = parseInt(document.getElementById("years").value);
    year = new Date().getFullYear() + num_of_years;
    let interest = (principal_amount * interest_rate * num_of_years) / 100
    let amount = principal_amount + interest
    let result = document.getElementById("result")


    if (principal_amount <= 0) {
        alert("Please enter a valid number");
        document.getElementById("principal").focus();
    }

    else {
        result.innerHTML = `If you deposit $<mark>${principal_amount}</mark>,<br> 
        at an interest rate of <mark>${interest_rate}%</mark>,<br> 
        You will receive an amount of $<mark>${amount}</mark>,<br> 
        in the year <mark>${year}</mark>,<br>`;
    }
}

function updateRate() {
    let rateval = document.getElementById("rate").value;
    document.getElementById("rate_val").innerText = rateval;
}
        