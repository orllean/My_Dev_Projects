function fx_tabuada(){
    let num = document.getElementById('txt_num').value
    let tabuada = document.getElementById('sel_tabuada')
    
    if (num.length == 0) {
        window.alert('* Favor digitar um número!')
    } else {
        tabuada.innerHTML =''
        let sel_lista = document.createElement('option')
        for(var c = 1; c <= 10; c++){
            //let sel_lista = document.createElement('option')
            sel_lista.text = `${Number(num)} x ${c} = ${Number(num) * c}`
            tabuada.appendChild(sel_lista)
        }
        Number(num)
    }
}