// Define a function to fetch and render data
function getProdline1() {
    // Fetch data from Flask API
    fetch('/Prodline1')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            // Get the table element
            const table = document.getElementById('Prodline1');

            // Clear any existing rows from the table
            while (table.rows.length > 0) {
                table.deleteRow(-1);
            }

            // Create a row for each item in the data
            data.forEach(item => {
                const row = table.insertRow(-1);
                const keys = Object.keys(item);

                // Create a cell for each key-value pair in the item
                keys.forEach(key => {
                    const cell = row.insertCell(-1);
                    cell.innerHTML = item[key];
                });
            });
        });
}

function getProdline2() {
    // Fetch data from Flask API
    fetch('/Prodline2')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            // Get the table element
            const table = document.getElementById('Prodline2');

            // Clear any existing rows from the table
            while (table.rows.length > 0) {
                table.deleteRow(-1);
            }

            // Create a row for each item in the data
            data.forEach(item => {
                const row = table.insertRow(-1);
                const keys = Object.keys(item);

                // Create a cell for each key-value pair in the item
                keys.forEach(key => {
                    const cell = row.insertCell(-1);
                    cell.innerHTML = item[key];
                });
            });
        });
}

function getProdline3() {
    // Fetch data from Flask API
    fetch('/Prodline3')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            // Get the table element
            const table = document.getElementById('Prodline3');

            // Clear any existing rows from the table
            while (table.rows.length > 0) {
                table.deleteRow(-1);
            }

            // Create a row for each item in the data
            data.forEach(item => {
                const row = table.insertRow(-1);
                const keys = Object.keys(item);

                // Create a cell for each key-value pair in the item
                keys.forEach(key => {
                    const cell = row.insertCell(-1);
                    cell.innerHTML = item[key];
                });
            });
        });
}

function getProdline4() {
    // Fetch data from Flask API
    fetch('/Prodline4')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            // Get the table element
            const table = document.getElementById('Prodline4');

            // Clear any existing rows from the table
            while (table.rows.length > 0) {
                table.deleteRow(-1);
            }

            // Create a row for each item in the data
            data.forEach(item => {
                const row = table.insertRow(-1);
                const keys = Object.keys(item);

                // Create a cell for each key-value pair in the item
                keys.forEach(key => {
                    const cell = row.insertCell(-1);
                    cell.innerHTML = item[key];
                });
            });
        });
}