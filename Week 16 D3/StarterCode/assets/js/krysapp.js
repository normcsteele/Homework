// @TODO: YOUR CODE HERE!

//grab the containing box
var width = parseInt(d3.select('#scatter').style("width"));

//define the height of the graph
var height = width - width/3.9;

// margin for spacing the graph
var margin = 20;

// space the placing words
var labelArea = 110;

// padding for the text as the bootm and left axis
var paddingBot = 40;
var paddingLeft = 40;

// creat the canvas for the graph
var svg = d3
  .select('#scatter')
  .append('svg')
  .attr("width", width)
  .attr("height", height)
  .attr("class","chart");

  // define circleRadius
var circleRadius ;

function crGet() {
  if (width <= 530) {
    circleRadius = 5;
  }
  else {
    circleRadius = 10;
  }
}
crGet();

// variables for axises
// bottom axis. you make the class to reference on the HTML which is called a xText
svg.append("g").attr("class","xText");
// reference xText
var xText = d3.select(".xText")
// give xText a transform attribute
function xTextRefresh() {
  xText.attr("transform", "translate(" + ((width - labelArea) / 2 + labelArea) 
  + ", " + (height - margin - paddingBot) + ")")
}
xTextRefresh();

// xText to append 3 text names
// 1) poverty

xText
  .append("text")
  .attr("y", -26)
  .attr("data-name", "poverty")
  .attr("data-axis", "x")
  .attr("class", "aText active x")
  .text("In Poverty (%)")

// 2) age
xText
.append("text")
.attr("y", 0)
.attr("data-name", "age")
.attr("data-axis", "x")
.attr("class", "aText inactive x")
.text("Age (Median)")

// 3) Income
xText
.append("text")
.attr("y", 26)
.attr("data-name", "income")
.attr("data-axis", "x")
.attr("class", "aText inactive x")
.text("Household Income (Median)")

// Left Axis
var leftTextX = margin + paddingLeft
var leftTextY = (height + labelArea) / 2 - labelArea

// add a second layer group
svg.append("g").attr("class", "yText");

// refer to by yText
var yText = d3.select(".yText");

// similar to xTextRefresh
function yTextRefresh() {
  yText.attr("transform", "translate(" + leftTextX + ","  + leftTextY + ")rotate(-90)")
}
yTextRefresh();

// append text to the yaxis
// 1) obesity
yText
  .append("text")
  .attr("y", -26)
  .attr("data-name", "obesity")
  .attr("data-axis", "y")
  .attr("class"," aText active y")
  .text("Obese (%)")
// 2) smokers
yText
  .append("text")
  .attr("y", 0)
  .attr("data-name", "smokes")
  .attr("data-axis", "y")
  .attr("class"," aText inactive y")
  .text("Smoke (%)")
// 3) healthcare
yText
  .append("text")
  .attr("y", 26)
  .attr("data-name", "healthcare")
  .attr("data-axis", "y")
  .attr("class"," aText inactive y")
  .text("Lacks Healthcare (%)")

// pull your data
d3.csv("assets/data/data.csv").then(function(data) {
  visualization(data);
});

// purpose of visualization function
//purpose of function is to manipulate tall the visual elements
function visualization(theData) {
  var curX = "poverty";
  var curY = "obesity";
  // we need max and mins to store these values
  var xMin;
  var xMax;
  var yMin;
  var yMax;
  //create a tooltip function
  var toolTip = d3
    .tip()
    .attr("Class", "d3-tip")
    .offset([40,-60])
    .html(function(d){
      var theX;
      // grab the state name
      var theState = "<div>" + d.state + "</div>"
      // grab the y value's key and value
      var theY = "<div>" + curY + ": " + d[curY] + "%</div>"
      // if the x key is poverty do
      if (curX === "poverty") {
        //grab the x key and its value
        theX = "<div>" + curX +": " + d[curX] + "%</div>"
      }
      else {
        theX = "<div>" + curX + ": " + parseFloat(d[curX]).toLocaleString("en")
        + "</div>"
      }
      // display what we capture
      return theState + theX + theY
    });
  svg.call(toolTip);

  function xMinMax() {
    xMin = d3.min(theData , function(d) {
      return parseFloat(d[curX]) * .90;
    })
    xMax = d3.max(theData, function(d) {
      return parseFloat(d[curX]) * 1.10;
    })
  }

  function yMinMax() {
    yMin = d3.min(theData , function(d) {
      return parseFloat(d[curY]) * .90;
    })
    yMax = d3.max(theData, function(d) {
      return parseFloat(d[curY]) * 1.10;
    })
  }
  // change classes and appearance when a diffent label text is clicked
  function labelChange(axis, clickText) {
    // switch the currently active to inactive
    d3.selectAll(".aText")
      .filter("." + axis)
      .filter(".active")
      .classed("active",false)
      .classed("inactive", true);
      //switch the text to just clicked to active
      clickText.classed("inactive", false).classed("active",true);
  }
  // scatter plot
  xMinMax();
  yMinMax();
  // now that minmax for x and y is defined we can build our scales

  var xScale = d3
  .scaleLinear()
  .domain([xMin,xMax])
  .range([margin + labelArea, width - margin])

  var yScale = d3
  .scaleLinear()
  .domain([yMin,yMax])
  .range([height - margin - labelArea, margin])

  //passe the scales into the axis methods to create our area
  var xAxis = d3.axisBottom(xScale);
  var yAxis = d3.axisLeft(yScale);

  //determind the x and y tick count
  function tickCount () {
    if (width <= 500) {
      xAxis.ticks(5);
      YAxis.ticks(5);
    }
    else {
      xAxis.ticks(10);
      yAxis.ticks(10);
    }
  }
  tickCount();

  // append axis to the svg as group elements
  svg.append("g")
    .call(xAxis)
    .attr("class","xAxis")
    .attr("transform", "translate(0, " + (height - margin - labelArea) + ")");

  svg.append("g")
    .call(yAxis)
    .attr("class","yAxis")
    .attr("transform", "translate(" + (margin + labelArea) + ", 0)");

  // we append the circles to each row of data
  var theCircles = svg.selectAll("g theCircle").data(theData).enter();

  theCircles 
    .append("circle")
    .attr("cx", function(d) {
      return xScale(d[curX])
    })
    .attr("cy", function(d) {
      return yScale(d[curY])
    })
    .attr("r",circleRadius)
    .attr("class",function(d) {
      return "stateCirle " + d.abbr;
    })
    .on("mouseover", function(d) {
      toolTip.show(d,this);
      //highlight the state circle border that your selected
      d3.select(this).style("stroke", "blue");
    })
    .on("mouseout", function(d) {
      //remove the tooltip highlight
      toolTip.hide(d);
      d3.select(this).style("stroke","#e3e3e3")
    });
  
  theCircles
    .append("text")
    .text(function(d) {
      return d.abbr;
    })
    .attr("dx", function(d) {
      return xScale(d[curX]);
    })
    .attr("dy", function(d) {
      // when the size fo the text is the radius add a third of the radius to the height
      // pushes it to the middle of the circle
      return yScale(d[curY]) + circleRadius / 2.5;
    })
    .attr("font-size",circleRadius)
    .attr("class","stateText")
    .on("mouseover", function(d) {
      toolTip.show(d);
      d3.select("." + d.abbr).style("stroke", "blue");
    })
    .on("mouseout", function(d) {
      toolTip.hide(d);
      d3.select("." + d.abbr).style("stroke", "#e3e3e3");
    });

    // make the graphy dynamic
    d3.selectAll(".aText").on("click",function() {
      var self = d3.select(this)
      // we only want to select inactive labels
      if (self.classed("inactive")) {
        //grabe the name and axis saved to the label
        var axis = self.attr("data-axis")
        var name = self.attr("data-name")
        if (axis === "x") {
          curX = name;
          //change the min and max
          xMinMax();
          // update the domain of x
          xScale.domain([xMin,xMax]);
          
          svg.select(".xAxis").transition(300).call(xAxis);
          // with the axis change, change location of circle
          d3.selectAll("circle").each(function() {
            d3.select(this)
              .transition()
              .attr("cx", function(d) {
                return xScale(d[curX]);
                })
              .duration(300);
            });
          d3.selectAll(".stateText").each(function() {
            d3.select(this)
              .transition()
              .attr("dx", function(d) {
                  return xScale(d[curX]);
                  })
              .duration(300);
            });
          labelChange(axis, self);
        }
        else {
          // when y is click, do this
          curY = name;
          // change the min and max
          yMinMax();
          //update the y axis
          yScale.domain([yMin,yMax])

          svg.select(".yAxis").transition(300).call(yAxis)

          d3.selectAll("circle").each(function() {
            d3.select(this)
              .transition()
              .attr("cy", function(d) {
                return yScale(d[curY]);
                })
              .duration(300);
            });
          d3.selectAll(".stateText").each(function() {
            d3.select(this)
              .transition()
              .attr("dy", function(d) {
                  return yScale(d[curY]) + circleRadius/3;
                  })
              .duration(300);
            });
          labelChange(axis, self);
          } 
      }
    })
}