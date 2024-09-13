async function fetchMetrics() {
    const response = await fetch('/api/metrics');
    const data = await response.json();
    document.getElementById('metrics').innerHTML = JSON.stringify(data);
}

setInterval(fetchMetrics, 5000);
