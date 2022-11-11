const labels = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
  ];

  const data = {
    labels: labels,
    datasets: [{
      label: 'My First dataset',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [0, 10, 5, 2, 20, 30, 45],
    }]
  };

  const config = {
    type: 'bar',
    data: data,
    options: {}
};

    const myChart = new Chart(
        document.getElementById('myChart'),
        config
      );


      const dataReports = {
        labels: [
          'Red',
          'Blue',
          
        ],
        datasets: [{
          label: 'My First Dataset',
          data: [300, 50, ],
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            
          ],
          hoverOffset: 4
        }]
      };

      const configReports = {
        type: 'doughnut',
        data: dataReports,
      };
    
      const myChartReports = new Chart(
        document.getElementById('myChartReports'),
        configReports
      );