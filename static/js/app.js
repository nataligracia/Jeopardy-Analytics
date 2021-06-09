// from jeopardy.json
d3.json("../data/jeopardy.json").then( function(tableData) {
    console.log(tableData)

    // get table references with d3.select()
    const tbody = d3.select('tbody');

    // define a function called buildTable that takes an argument called data
    function buildTable(data) {
    // the job of this function is to parse out the data and create an html table
    // clear out any existing data in tbody by setting the .html() to an empty string
    tbody.html('');

    // Next, loop forEach() dataRow in the data
    // and append a row and cells for each value in the row
    data.forEach((datarow) => {
        // .append() a table row "tr" to the tbody
        var row = tbody.append('tr');

        // Loop through forEach val in the Object.values(dataRow)
        Object.values(datarow).forEach((val) => {
        // append each value as a table cell (td)
        var cell = row.append('td');
        // set the .text of cell to the val
        cell.text(val);
        });
    });
    };

    var filters = {};

    function handleClick() {
    // Select all "form-control" class 
    var formControl = d3.selectAll('.form-control')
    // console.log(formControl._groups[0]);

    // Use the forEach function iterate each id from the "form-control" class, enabling the value update
    // Use the ._groups[0] to select the group array that consists the ids
    formControl._groups[0].forEach(function (updateElement) {
        var updateValue = updateElement.value;
        var filterId = updateElement.id;
        if (updateValue) {
        filters[filterId] = updateValue;
        }
        else {
        delete filters[filterId];
        }
    });

    // Call function to rebuild table
    filterTable();
    };

    // Define the filterTable function
    function filterTable () {
        let filteredData = tableData;
    
        Object.entries(filters).forEach(([key, value]) => {
        filteredData = filteredData.filter(row => row[key] === value);
        });
    
        buildTable(filteredData);
    };

    // Attach an event to listen for the form button #filter-btn to be clicked, it should call your handleClick function
    d3.selectAll('#filter-btn').on('click',handleClick);

    // Build the table with your buildTable function when the page loads
    buildTable(tableData);

});