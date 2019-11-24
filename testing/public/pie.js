google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

    const values = [];
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Reason');
    data.addColumn('number', 'Frequency');

    var options = {
        pieHole: 0.5,
        height: 500,
        width: 700,
        pieHole: 0.4,
        backgroundColor: 'transparent',
        colors: ['#88BDBC', '#c8dad3', '#F4976C', '#ffdc82', '#E85A4F'],
        pieSliceTextStyle: {
            color: 'white',
        },
        pieSliceText: 'label',
        legend: 'none'
    };

    var chart = new google.visualization.PieChart(document.getElementById('donut_single'));

    google.visualization.events.addListener(chart, 'error', (err) => console.log(err));

    // Track the frequency of each issue
    var bellyache = 0,
        discomfort = 0,
        burping = 0,
        tired = 0,
        hungry = 0;

    $.ajax({
        url: 'http://localhost:8080/',
        method: 'GET',
        success: (item) => {
            item.forEach((taskData) => {
                if (taskData.Task_Name == "Bellyache") {
                    bellyache = bellyache + 1;
                } else if (taskData.Task_Name == "Discomfort") {
                    discomfort = discomfort + 1;
                } else if (taskData.Task_Name == "Burping") {
                    burping = burping + 1;
                } else if (taskData.Task_Name == "Tired") {
                    tired = tired + 1;
                } else if (taskData.Task_Name == "Hungry") {
                    hungry = hungry + 1;
                }
            });
            values.push(['Bellyache', bellyache]);
            values.push(['Discomfort', discomfort]);
            values.push(['Burping', burping]);
            values.push(['Tired', tired]);
            values.push(['Hungry', hungry]);

            data.addRows(values);
            console.log(values);

            chart.draw(data, options);
        }

    });
}