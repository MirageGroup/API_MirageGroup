
   console.log(ProblemLigar)
   





  // TIPOS DE PROBLEMAS 
const labels = [
  'O computador não liga',
  'O computador está sem internet',
  'O computador está muito lento',
  'O computador não está dando imagem',
  'O computador está sem som',
  'O computador está tendo a tela azul',
  'O computador está desligando sozinho',
  'O sistema operacional não está inicializando',
  'A tela está congelando',
  'O mouse não está funcionando',
  'O teclado não está funcionando',
  'Outro'
  ];

  const data = {
    labels: labels,
    datasets: [{
      label: 'Problemas reportados',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [ProblemLigar,ProblemNoInternet,
        ProblemLento,
        ProblemNoImage,
        ProblemNoSound,
        ProblemBlueScreen,
        ProblemTurnOff,
        ProblemInitialization,
        ProblemFreezingScreen,
        ProblemMouse,
        ProblemBoard,
        ProblemOther],
        
    }]
  };

  const config = {
    type: 'bar',
    data: data,
    options: {
      scales:{
        y:{
          suggestedMin: 0,
          suggestedMax: 10,
        }

      }
    }
};

    const myChart = new Chart(
        document.getElementById('myChart'),
        config
      );




      // CHAMADOS ABERTOS E FECHADOS
      const dataReports = {
        labels: [
          'chamadosAbertos',
          'chamadosFechados',
          
        ],
        datasets: [{
          label: 'My First Dataset',
          data: [chamadosAbertos, chamadosFechados, ],
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