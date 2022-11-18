
   
   





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
      data: [
        ProblemLigar,
        ProblemNoInternet,
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

        // CHAMADOS EM CADA LABORATORIO

      const labelsLab = [
        'Laboratorio 301',
        'laboratorio 302',
        'laboratorio 303',
        'laboratorio 401',
        'laboratorio 402',
        'laboratorio 403',
        'laboratorio 404',
        'laboratorio 405',
        'laboratorio 406',
        'laboratorio 407',
        'laboratorio 408',
        'laboratorio 409',
        'laboratorio 410',
        'laboratorio 411',
        'laboratorio 412',
        ];
      
        const dataLab = {
          labels: labelsLab,
          datasets: [{
            label: 'numero de reports em laboratorios',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [
        Problem301,
        Problem302,
        Problem303,
        Problem401,
        Problem402,
        Problem403,
        Problem404,
        Problem405,
        Problem406,
        Problem407,
        Problem408,
        Problem409,
        Problem410,
        Problem411,
        Problem412,








            ],
              
          }]
        };
      
        const configLab = {
          type: 'bar',
          data: dataLab,
          options: {
            scales:{
              y:{
                suggestedMin: 0,
                suggestedMax: 10,
              }
      
            }
          }
      };
      
          const myChartLab = new Chart(
              document.getElementById('myChartLab'),
              configLab
            );


     // ALTERNANDO VISIBILIDADE DE GRAFICOS


     const abas = document.querySelectorAll('[data-botao]'); 

     esconderConteudos = () => {
       const conteudos = document.querySelectorAll('[data-grafico]')
   
       conteudos.forEach(conteudo => conteudo.classList.add('none'))
     }
     inativarAbas = () => {
       abas.forEach(aba => aba.classList.remove('aba-ativa-estatisticas'))
     }
     ativarConteudo = (valor) => {
       const conteudo = document.querySelectorAll(`[data-grafico="${valor}"]`)
   
       conteudo.forEach(conteudo=> conteudo.classList.remove('none'))
     }
     ativarAba = (aba) => {
       aba.classList.add('aba-ativa-estatisticas')
       
     }
     abas.forEach(aba => aba.addEventListener('click', () => {
         const valor = aba.dataset.botao
         console.log(valor)
   
         esconderConteudos()
         inativarAbas()
         ativarConteudo(valor)
         ativarAba(aba)
   })) 