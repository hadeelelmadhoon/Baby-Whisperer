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
        vAxis: {
            title: 'Reason',
            minValue: 0,
            maxValue: 6,
            ticks: [{ v: 1, f: 'Bellyache' },
                { v: 2, f: 'Discomfort' }, { v: 3, f: 'Burping' },
                { v: 4, f: 'Tired' }, { v: 5, f: 'Hungry' }
            ]
        },
        legend: 'none',
        colors: ['#88BDBC'],
        hAxis: {
            title: 'Time (24 Hours)',
            ticks: [{ v: 1, f: '1 AM' },
                { v: 5, f: '5 AM' },
                { v: 10, f: '10 AM' },
                { v: 15, f: '3 PM' },
                { v: 20, f: '8 PM' },
                { v: 24, f: '12 PM' }
            ],
            viewWindow: { max: 24 }
        }
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