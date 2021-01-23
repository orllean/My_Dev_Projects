function contar(){
    var ini = window.document.getElementById('txt_ini').value
    var fim = window.document.getElementById('txt_fim').value
    var pas = window.document.getElementById('txt_pas').value
    var res = window.document.getElementById('res')

    res.innerHTML = 'Contando... <br>'

    if (ini.length == 0 || fim.length == 0 || pas.length == 0) {
        res.innerHTML = '*Toodos os dados são necessários!'        
    } else {
        if (Number(pas) <= 0){
            window.alert('*Passo inválido! Executando contador com passo = 1')
            pas = 1
        }
        if (Number(ini) < Number(fim)) {
            for (var c = Number(ini); c <= Number(fim); c += Number(pas)) {
                 res.innerHTML += ` ${c} \u{1F449}`
             }
        } else {
            for(var c = Number(ini); c >= Number(fim); c-= Number(pas) ) {
                res.innerHTML += ` ${c} \u{1F448}`
            }
        }
        res.innerHTML += `\u{1F3C1}`
    }       
 } 