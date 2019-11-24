// google.charts.load('current', { 'packages': ['corechart'] });
// google.charts.setOnLoadCallback(drawChart);

// function drawChart() {

//     var data = google.visualization.arrayToDataTable([
//         ['Reason', 'Hours per Day'],
//         ['Work', 11],
//         ['Eat', 2],
//         ['Commute', 2],
//         ['Watch TV', 2],
//         ['Sleep', 7]
//     ]);

//     var options = {
//         height: 600,
//         width: 700,
//         backgroundColor: 'transparent',
//         title: 'My Daily Activities'
//     };

//     var chart = new google.visualization.PieChart(document.getElementById('piechart'));

//     chart.draw(data, options);
// }

google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

    var data = google.visualization.arrayToDataTable([
        ['Task', 'Hours per Day'],
        ['Work', 11],
        ['Eat', 2],
        ['Commute', 2],
        ['Watch TV', 2],
        ['Sleep', 7]
    ]);

    var options = {
        pieHole: 0.5,
        height: 600,
        width: 700,
        pieHole: 0.4,
        backgroundColor: 'transparent',
        colors: ['#88BDBC', '#c8dad3', '#F4976C', '#ffdc82', '#E85A4F'],
        pieSliceTextStyle: {
            color: 'black',
        },
        legend: 'none'
    };

    var chart = new google.visualization.PieChart(document.getElementById('donut_single'));
    chart.draw(data, options);
}