    let agora = new Date
    let diaMes = agora.getDate()
    let numDiaSemana = agora.getDay()
    let numMes = agora.getMonth()
    let ano = agora.getFullYear()
    let hora = agora.getHours()
    let min = agora.getMinutes()
    let sec = agora.getSeconds()
    let mes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    let dia = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']
    
    /* let mes = new Array('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez') */
    console.log(`Dia: ${diaMes}`)
    console.log(`Mês: ${mes[numMes]}`)
    console.log(`Ano: ${ano}`)
    console.log(`Dia da semana: ${dia[numDiaSemana]}`)
    console.log(`Hora: ${hora}`)
    console.log(`Minutos: ${min}`)
    console.log(`Segundos: ${sec}`)
    console.log(`${diaMes} / ${mes[numMes]} / ${ano}`)
    console.log(agora.toDateString())
