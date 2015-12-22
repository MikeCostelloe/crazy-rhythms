<!--
function stats1() {
	//Conventional Margins start
	var margin = {top: 20, right: 40, bottom: 20, left: 80};
		width = 900 - margin.left - margin.right,
		height = 500 - margin.top - margin.bottom;

	var svg = d3.select("#chart2").append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
		.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
	//Conventional Margins end
	
	//Scales
	var x = d3.scale.linear()
		.range([0, width]);
		
	var y = d3.scale.linear()
		.range([height, 0]);
		
	//Color
	var color = d3.scale.category10();
	
	//Axes
	var xAxis = d3.svg.axis()
		.scale(x)
		.orient('bottom')
		.ticks(8);
		
	var yAxis = d3.svg.axis()
		.scale(y)
		.orient('left');
	
	//Lines
	var line = d3.svg.line()
		.x(function(d) { return x(d.Week); })
		.y(function(d) { return y(d.Record); });
	

	//Data load and two console logs, before and after the data.map
	d3.csv('http://mikecostelloe.com/crazyrhythms/files/R.csv', function(error, data) {
		
		//Splits into 10 colors by owner
		color.domain(d3.keys(data[0]).filter(function(key) { return key !== 'Week'; }));
	
		var owners = color.domain().map(function(name) {
			return {
				name: name,
				values: data.map(function(d) {
					return {Week: d.Week, Record: +d[name]};
					})
				};
			});
	
		//x-Domain corresponds to Weeks 
		x.domain([0,21]);
	
		//y-Domain to min/max of winPct's
		y.domain([
			d3.min(owners, function(c) { return d3.min(c.values, function(v) { return v.Record; }); }),
			d3.max(owners, function(c) { return d3.max(c.values, function(v) { return v.Record; }); })
		]);
	
		svg.append('g')
			.attr('class', 'x axis')
			.attr('transform', 'translate(0,' + height + ')')
			.call(xAxis)
			.append("text")
			.attr("x", width)
			.attr("y", -12)
			.attr("dy", ".71em")
			.style("text-anchor", "end")
			.text("Week");
		
		svg.append('g')
			.attr("class", "y axis")
			.call(yAxis)
			.append("text")
			.attr("transform", "rotate(-90)")
			.attr("y", 6)
			.attr("dy", ".71em")
			.style("text-anchor", "end")
			.text("Weekly total");
	
		//Selects .owner class (none exist at first) and creates them as needed	
		var owner = svg.selectAll('.owner')
			.data(owners)
			.enter().append('g')
			.attr('class', 'owner');
	
		//Assigns each owner a line and a unique color for it	
		owner.append('path')
			.attr('class', 'line')
			.attr('d', function(d) { return line(d.values); })
			.style('stroke', function(d) { return color(d.name); })
			
		//Adds a circle to each data node
		owner.append('g').selectAll('circle')
			.data(function(d) {return d.values; })
			.enter().append('circle')
			.attr('r', 4)
			.attr('cx', function(c) { return x(c.Week); })
			.attr('cy', function(c) { return y(c.Record); })
			.attr('fill', function(d) { return color(this.parentNode.__data__.name); }) //pulls color from range in way I don't understand
			.on('mouseover', function(d) {
				var xTip = parseFloat(d3.select(this).attr('cx'));
				var yTip = parseFloat(d3.select(this).attr('cy'));
			
				svg.append('text')
					.attr('id', 'tooltip')
					.attr('x', xTip + 5) 
					.attr('y', yTip - 10)
					.attr('fill', 'black')
					.text(d.Record);
				})
			
			.on('mouseout', function() {
				d3.select('#tooltip').remove()
			});

		//Adds the names at the end
		owner.append("text")
			.datum(function(d) { return {name: d.name, value: d.values[d.values.length - 1]}; })
			.attr("transform", function(d) { return "translate(" + x(d.value.Week) + "," + y(d.value.Record) + ")"; })
			.attr('class', 'labels')
			.attr("x", 5)
			.attr("dy", 5)
			.attr('fill', function(d) { return color(this.parentNode.__data__.name); }) //pulls color from range in way I don't understand
			.text(function(d) { return d.name; });
			
		//Dropdown menu listener	
		d3.select("#menu").on("change", change);
	
		function change() {
			var item = this.value;
			
			d3.csv('http://mikecostelloe.com/crazyrhythms/files/' + item + '.csv', function(error, data) {

			var owners = color.domain().map(function(name) {
				return {
					name: name,
					values: data.map(function(d) {
						return {Week: d.Week, Record: +d[name]};
						})
					};
				});

			//y-Domain to min/max of winPct's
			y.domain([
				d3.min(owners, function(c) { return d3.min(c.values, function(v) { return v.Record; }); }),
				d3.max(owners, function(c) { return d3.max(c.values, function(v) { return v.Record; }); })
			]);
			
			svg.select('.x.axis')
				.call(xAxis);
				
			svg.select('.y.axis')
				.call(yAxis);
				
			//Update class data
			svg.selectAll('.owner')
				.data(owners);

			//Update lines	
			owner.select('path')
				.transition()
				.attr('d', function(d) { return line(d.values); });
		
			//Update circles
			owner.selectAll('circle')
				.data(function(d) { return d.values; })
				.transition()
				.attr('cy', function(c) { return y(c.Record); });

			//Update labels
			owner.select(".labels")
				.datum(function(d) { return {name: d.name, value: d.values[d.values.length - 1]}; })
				.transition()
				.attr("transform", function(c) { return "translate(" + x(c.value.Week) + "," + y(c.value.Record) + ")"; })
				
		})};
	});
	};
stats1();