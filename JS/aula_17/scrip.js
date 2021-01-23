var arrNum = []
function fxAdicionar() {
    let num = Number(document.getElementById('txt_num').value)
    if (num < 1 || num > 100) {
        window.alert('Valor inválio ou já add na lista!')
    } else {
        if (arrNum.indexOf(num) == -1) {
            document.getElementById('dv_res').innerHTML = ''
            let lista = document.getElementById('sel_valor')
            let elemento = document.createElement('option')
            arrNum.push(num)
            elemento.text = `num: [ ${num} ] add com sucesso!`
            lista.appendChild(elemento)
        } else {
            window.alert('Valor inválio ou já add na lista!')
        }
    }
}

function fxFinalizar() {
    let saida = document.getElementById('dv_res')
    if (arrNum.length == 0) {
        window.alert('Add um valor antes de finalizar!')
    } else {
        let maior = arrNum[0]
        let menor = arrNum[0]
        let soma = 0
        let media = 0
        
        for (let c in arrNum) {
            soma += arrNum[c]
            if (maior < arrNum[c]) {
                maior = arrNum[c]
            }
            if (menor > arrNum[c]) {
                menor = arrNum[c]
            }
        }
        media = soma / arrNum.length
        
        saida.innerHTML += `<p>Total de num add: [ ${arrNum.length} ]</p>`
        saida.innerHTML += `<p>O maior num add: [ ${maior} ]</p>`
        saida.innerHTML += `<p>O menor num add: [ ${menor} ]</p>`
        saida.innerHTML += `<p>A soma dos num's add: [ ${soma} ]</p>`
        saida.innerHTML += `<p>A media dos num's add: [ ${media} ]</p>`
        document.getElementById('txt_num').value = ''
        document.getElementById('txt_num').focus()

    }
}