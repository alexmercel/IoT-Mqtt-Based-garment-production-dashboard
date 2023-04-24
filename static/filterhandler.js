
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
            const chart = document.getElementById('chart1');
            chart.innerHTML=''

		    let x = 0;

            for (const key in data) {
			const value = data[key];

			// Create a new rectangle for the bar
			const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');

			// Set the dimensions and position of the rectangle
			rect.setAttribute('x', x);
			rect.setAttribute('y', 300 - value * 10);
			rect.setAttribute('width', 50);
			rect.setAttribute('height', value * 10);

			// Add the rectangle to the chart
			chart.appendChild(rect);

            // Create a new text element for the label
			const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');

			// Set the position and content of the label
			label.setAttribute('x', x);
			label.setAttribute('y', 280 - value * 10);
			label.setAttribute('class', 'label');
            label.setAttribute('style', 'color:black');
			label.textContent = key;
			// Add the label to the chart
			chart.appendChild(label);
			x += 60;
		}
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
        const chart = document.getElementById('chart2');

        let x = 0;

        for (const key in data) {
        const value = data[key];

        // Create a new rectangle for the bar
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');

        // Set the dimensions and position of the rectangle
        rect.setAttribute('x', x);
        rect.setAttribute('y', 300 - value * 10);
        rect.setAttribute('width', 50);
        rect.setAttribute('height', value * 10);

        // Add the rectangle to the chart
        chart.appendChild(rect);

        // Create a new text element for the label
        const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');

        // Set the position and content of the label
        label.setAttribute('x', x);
        label.setAttribute('y', 280 - value * 10);
        label.setAttribute('class', 'label');
        label.setAttribute('style', 'color:black');
        label.textContent = key;
        // Add the label to the chart
        chart.appendChild(label);
        x += 60;
    }
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
        const chart = document.getElementById('chart3');

        let x = 0;

        for (const key in data) {
        const value = data[key];

        // Create a new rectangle for the bar
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');

        // Set the dimensions and position of the rectangle
        rect.setAttribute('x', x);
        rect.setAttribute('y', 300 - value * 10);
        rect.setAttribute('width', 50);
        rect.setAttribute('height', value * 10);

        // Add the rectangle to the chart
        chart.appendChild(rect);

        // Create a new text element for the label
        const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');

        // Set the position and content of the label
        label.setAttribute('x', x);
        label.setAttribute('y', 280 - value * 10);
        label.setAttribute('class', 'label');
        label.setAttribute('style', 'color:black');
        label.textContent = key;
        // Add the label to the chart
        chart.appendChild(label);
        x += 60;
    }
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
        const chart = document.getElementById('chart4');

        let x = 0;

        for (const key in data) {
        const value = data[key];

        // Create a new rectangle for the bar
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');

        // Set the dimensions and position of the rectangle
        rect.setAttribute('x', x);
        rect.setAttribute('y', 300 - value * 10);
        rect.setAttribute('width', 50);
        rect.setAttribute('height', value * 10);

        // Add the rectangle to the chart
        chart.appendChild(rect);

        // Create a new text element for the label
        const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');

        // Set the position and content of the label
        label.setAttribute('x', x);
        label.setAttribute('y', 280 - value * 10);
        label.setAttribute('class', 'label');
        label.setAttribute('style', 'color:black');
        label.textContent = key;
        // Add the label to the chart
        chart.appendChild(label);
        x += 60;
    }
        })
        .catch((error) => {
            console.error('Error:', error);
            // handle the error, like displaying an error message to the user
        });

});
}


