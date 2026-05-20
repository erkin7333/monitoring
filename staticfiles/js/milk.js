const months = JSON.parse(document.getElementById('months-data').textContent);
const milk = JSON.parse(document.getElementById('milk-data').textContent)[0];

new Chart(document.getElementById('milkChart'), {
    type: 'bar',
    data: {
        labels: months,
        datasets: [{
            label: "Sut mahsulotlari",
            data: milk,
            backgroundColor: "blue"
        }]
    }
});