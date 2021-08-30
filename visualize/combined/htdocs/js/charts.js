// Echtzeitdaten
let livechart = document.getElementById('Live_Chart');
let live_chart = new Chart(livechart, {
    type: 'line',
    data: {
        labels: ["first", "second", "third", "4", "5", "6", "7", "8", "9", "10"],
        color: 'rgba(255, 255, 255, 1)',
        datasets: [{
            label: "Live Temperature Data",
            data: [3,5,7,2,5,2,5,6],
            fill: true,
            background_color: 'rgba(255, 99, 132, 0.7)',
            borderColor: 'rgba(20, 206, 86, 0.7)'
        },{
            label: "Live Pressure Data",
            data: [8,3,1,2,8,3,11,5],
            fill: true,
            background_color: 'rgba(255, 99, 132, 0.7)',
            borderColor: 'rgba(255, 206, 86, 0.7)'
        }]
    }
});



//Menuetliche Daten
let min_c = document.getElementById('Minute_Chart');
let m_chart = new Chart(min_c, {
    type: 'line',
    data: {
        labels: ["first", "second", "third", "4", "5", "6", "7", "8", "9", "10"],
        color: 'rgba(255, 255, 255, 1)',
        datasets: [{
            label: "Minute Temperature Data",
            data: [3,5,7,2,5,2,5,6],
            fill: true,
            background_color: 'rgba(255, 99, 132, 0.7)',
            borderColor: 'rgba(20, 206, 86, 0.7)'
        },{
            label: "Minute Pressure Data",
            data: [8,3,1,2,8,3,11,5],
            fill: true,
            background_color: 'rgba(255, 99, 132, 0.7)',
            borderColor: 'rgba(255, 206, 86, 0.7)'
        }]
    }
});



//Alle Daten
let all_c = document.getElementById('All_Chart');
let a_chart = new Chart(all_c, {
    type: 'line',
    data: {
        labels: ["first", "second", "third", "4", "5", "6", "7", "8", "9", "10"],
        color: 'rgba(255, 255, 255, 1)',
        datasets: [{
            label: "All Temperature Data",
            data: [3,5,7,2,5,2,5,6],
            fill: true,
            background_color: 'rgba(255, 99, 132, 0.7)',
            borderColor: 'rgba(20, 206, 86, 0.7)'
        },{
            label: "All Pressure Data",
            data: [8,3,1,2,8,3,11,5],
            fill: true,
            background_color: 'rgba(255, 99, 132, 0.7)',
            borderColor: 'rgba(255, 206, 86, 0.7)'
        }]
    }
});
