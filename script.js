function validateForm() {

    let inputs = document.querySelectorAll("input");

    for (let i = 0; i < inputs.length; i++) {

        if (inputs[i].value === "") {
            alert("Please fill all fields.");
            return false;
        }

    }

    alert("Predicting Flood Risk...");

    return true;
}