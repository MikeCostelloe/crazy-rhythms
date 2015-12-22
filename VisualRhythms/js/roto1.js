<!--
function roto1() {
	
	var columns = ['Owner', 'R', 'HR', 'TB', 'RBI', 'SBN', 'OBP', 'IP', 'K', 'SV', 'ERA', 'WHIP', 'K-BB', 'TOTAL'];
	
	function tabulate(data, columns) {
		var table = d3.select("#table1").append("table")
			.attr('class', 'statTable');
		
		var thead = table.append("thead");
		
		var tbody = table.append("tbody");

		// append the header row
		thead.append("tr")
			.selectAll("th")
			.data(columns)
			.enter()
			.append("th")
				.text(function(column) { return column; });

		// create a row for each object in the data
		var rows = tbody.selectAll("tr")
			.data(data)
			.enter()
			.append("tr");

		// create a cell in each row for each column
		var cells = rows.selectAll("td")
			.data(function(row) {
				return columns.map(function(column) {
					return {column: column, value: row[column]};
				});
			})
			.enter()
			.append("td")
				.text(function(d) { return d.value; });
	
		return table;
	}
	
	d3.csv('http://mikecostelloe.com/crazyrhythms/files/roto2015.csv', function(error, data) {
		// render the table
		var rotoTable = tabulate(data, columns);

	});	
};
roto1();