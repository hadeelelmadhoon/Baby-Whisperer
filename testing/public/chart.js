google.charts.load('current', { 'packages': ['gantt'] });
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

    console.log('ABout to call endpoint');

    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Task ID');
    data.addColumn('string', 'Task Name');
    data.addColumn('string', 'Resource');
    data.addColumn('date', 'Start Date');
    data.addColumn('date', 'End Date');
    data.addColumn('number', 'Duration');
    data.addColumn('number', 'Percent Complete');
    data.addColumn('string', 'Dependencies');

    var options = {
        height: 300,
        width: 600,
        backgroundColor: 'transparent',
        gantt: {
            trackHeight: 30
        }
    };

    var chart = new google.visualization.Gantt(document.getElementById('chart_div'));

    google.visualization.events.addListener(chart, 'error', (err) => console.log(err));

    console.log('About to call endpoint');
    $.ajax({
        url: 'http://localhost:8080/',
        method: 'GET',
        success: (item) => {
            console.log(item);
            const rowData = [];
            item.forEach((taskData) => {
                rowData.push([taskData.Task_ID, taskData.Task_Name, taskData.Resource, new Date(taskData.Start_Date), new Date(taskData.End_Date), 10, new Number(taskData.Percent_Complete), null]);
            });

            console.log(rowData);

            data.addRows(rowData);

            chart.draw(data, options);
        }
    });
}