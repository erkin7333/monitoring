const months = JSON.parse(document.getElementById('months-data').textContent);
const meat = JSON.parse(document.getElementById('meat-data').textContent)[0];
const rice = JSON.parse(document.getElementById('rice-data').textContent)[0];

new Chart(document.getElementById('chart'), {
    type: 'line',
    data: {
        labels: months,
        datasets: [
            {
                label: "🥩 Go'sht",
                data: meat,
                borderColor: "#dc3545",
                backgroundColor: "rgba(220,53,69,0.1)",
                fill: true,
                tension: 0.4,
                pointRadius: 5,
                pointHoverRadius: 7
            },
            {
                label: "🍚 Guruch",
                data: rice,
                borderColor: "#198754",
                backgroundColor: "rgba(25,135,84,0.1)",
                fill: true,
                tension: 0.4,
                pointRadius: 5,
                pointHoverRadius: 7
            }
        ]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top'
            },
            tooltip: {
                mode: 'index',
                intersect: false
            }
        },
        interaction: {
            mode: 'nearest',
            intersect: false
        },
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});