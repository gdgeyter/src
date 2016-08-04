/**
 * Created by gdgeyter on 27/07/16.
 */
d3.json(url_to_data, function(data) {
  nv.addGraph(function() {
    var chart = nv.models.lineChart();

    chart.xAxis
        .axisLabel("X-axis Label");

    chart.yAxis
        .axisLabel("Y-axis Label")
        .tickFormat(d3.format("d"))
        ;

    d3.select("svg")
        .datum(data)
        .transition().duration(500).call(chart);

    nv.utils.windowResize(
            function() {
                chart.update();
            }
        );

    return chart;
});
});

