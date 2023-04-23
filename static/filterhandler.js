
//Function to get data for Article 1
function filterline1() {
    const form = document.querySelector('#my-form-line1');
    const formData = new FormData(form);
    form.addEventListener('submit', event => {
        event.preventDefault();
        const formData = new FormData(form);
        const params = Object.fromEntries(formData.entries());
        const queryString = new URLSearchParams(params).toString();
        const url = `/filterline?line=A&${queryString}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                // do something with the response data, like update the UI
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
            })
            .catch((error) => {
                console.error('Error:', error);
                // handle the error, like displaying an error message to the user
            });

    });
}

//Function to get data for Article 2
function filterline2() {
    const form = document.querySelector('#my-form-line2');
    const formData = new FormData(form);
    form.addEventListener('submit', event => {
        event.preventDefault();
        const formData = new FormData(form);
        const params = Object.fromEntries(formData.entries());
        const queryString = new URLSearchParams(params).toString();
        const url = `/filterline?line=B&${queryString}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                // do something with the response data, like update the UI
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
            })
            .catch((error) => {
                console.error('Error:', error);
                // handle the error, like displaying an error message to the user
            });

    });
}

//Function to get data for Article 3
function filterline3() {
    const form = document.querySelector('#my-form-line3');
    const formData = new FormData(form);
    form.addEventListener('submit', event => {
        event.preventDefault();
        const formData = new FormData(form);
        const params = Object.fromEntries(formData.entries());
        const queryString = new URLSearchParams(params).toString();
        const url = `/filterline?line=C&${queryString}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                // do something with the response data, like update the UI
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
            })
            .catch((error) => {
                console.error('Error:', error);
                // handle the error, like displaying an error message to the user
            });
    });
}

//Function to get data for Article 4
function filterline4() {
    const form = document.querySelector('#my-form-line4');
    const formData = new FormData(form);
    form.addEventListener('submit', event => {
        event.preventDefault();
        const formData = new FormData(form);
        const params = Object.fromEntries(formData.entries());
        const queryString = new URLSearchParams(params).toString();
        const url = `/filterline?line=D&${queryString}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                // do something with the response data, like update the UI
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
            })
            .catch((error) => {
                console.error('Error:', error);
                // handle the error, like displaying an error message to the user
            });

    });
}


