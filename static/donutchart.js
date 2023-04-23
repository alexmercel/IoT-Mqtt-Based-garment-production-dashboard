
// For Line 1
function getProdchart1(){
    // Get the progress bars
    var progressBars = document.querySelectorAll('#donut-chart .progress-bar1');
    // Fetch the data from Flask
    fetch('/dataProdline1')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            // Calculate the total percentage value
            var total = data.reduce(function(sum, value) {
            return sum + value;
            }, 0);
            
            // Update the progress bars
            progressBars.forEach(function(bar, index) {
            var value = data[index];
            var percent = value / total * 100;
            bar.textContent = percent.toFixed(1) + '%';
            bar.style.width = percent + '%';
            });
        });
}

// For Line 2
function getProdchart2(){
    // Get the progress bars
    var progressBars = document.querySelectorAll('#donut-chart .progress-bar2');
    // Fetch the data from Flask
    fetch('/dataProdline2')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            // Calculate the total percentage value
            var total = data.reduce(function(sum, value) {
            return sum + value;
            }, 0);
            
            // Update the progress bars
            progressBars.forEach(function(bar, index) {
            var value = data[index];
            var percent = value / total * 100;
            bar.textContent = percent.toFixed(1) + '%';
            bar.style.width = percent + '%';
            });
        });
}

// For Line 3
function getProdchart3(){
    // Get the progress bars
    var progressBars = document.querySelectorAll('#donut-chart .progress-bar3');
    // Fetch the data from Flask
    fetch('/dataProdline3')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            // Calculate the total percentage value
            var total = data.reduce(function(sum, value) {
            return sum + value;
            }, 0);
            
            // Update the progress bars
            progressBars.forEach(function(bar, index) {
            var value = data[index];
            var percent = value / total * 100;
            bar.textContent = percent.toFixed(1) + '%';
            bar.style.width = percent + '%';
            });
        });
}

// For Line 4
function getProdchart4(){
    // Get the progress bars
    var progressBars = document.querySelectorAll('#donut-chart .progress-bar4');
    // Fetch the data from Flask
    fetch('/dataProdline4')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            // Calculate the total percentage value
            var total = data.reduce(function(sum, value) {
            return sum + value;
            }, 0);
            
            // Update the progress bars
            progressBars.forEach(function(bar, index) {
            var value = data[index];
            var percent = value / total * 100;
            bar.textContent = percent.toFixed(1) + '%';
            bar.style.width = percent + '%';
            });
        });
}
