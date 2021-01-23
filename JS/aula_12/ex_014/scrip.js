function carregar(){
    var hora = new Date
    var img = window.document.getElementById('img')
    var msn = window.document.getElementById('dv_hora')
    
    hora = hora.getHours()
    hora = 19
    
    msn.innerHTML = `Agora são ${hora} horas`
    if (hora >= 0 && hora <= 12) {
        img.src = 'img_manha.png'
        window.document.body.style.background = '#fbc156'        
    } else if (hora > 12 && hora < 18) {
        img.src = 'img_tarde.png'
        window.document.body.style.background = '#f0554ba'
    } else {
        img.src = 'img_noite.png'
        window.document.body.style.background = '#371d01'
    } 
}