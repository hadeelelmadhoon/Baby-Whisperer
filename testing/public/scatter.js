google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

    const values = [];
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Time');
    data.addColumn('number', 'Reason');

    var options = {
        backgroundColor: 'transparent',
        height: 300,
        width: 600,
        hAxis: { title: 'Time (24 Hours)', minValue: 0, maxValue: 24 },
        vAxis: { title: 'Reason', minValue: 0, maxValue: 6 },
        legend: 'none'
    };

    var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));

    google.visualization.events.addListener(chart, 'error', (err) => console.log(err));

    $.ajax({
        url: 'http://localhost:8080/',
        method: 'GET',
        success: (item) => {
            item.forEach((taskData) => {
                var index;
                if (taskData.Task_Name == "Bellyache") {
                    index = 1;
                } else if (taskData.Task_Name == "Discomfort") {
                    index = 2;
                } else if (taskData.Task_Name == "Burping") {
                    index = 3;
                } else if (taskData.Task_Name == "Tired") {
                    index = 4;
                } else if (taskData.Task_Name == "Hungry") {
                    index = 5;
                }

                var time = taskData.Start_Date.substring(11, 13);
                values.push([Number(time), Number(index)]);
            });

            data.addRows(values);
            console.log(values);

            chart.draw(data, options);
        }

    });
}