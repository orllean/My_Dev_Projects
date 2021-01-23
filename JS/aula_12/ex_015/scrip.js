function bt_verificar(){
    var ano_a = new Date
    ano_a = ano_a.getFullYear()
    var ano_nasc = document.getElementById('txt_ano').value
    
    if (ano_nasc.length == 0 || ano_nasc >= ano_a) {
        window.alert('Verifique o campo "Ano de nascimento"')
    } else {
        var idade = ano_a - ano_nasc
        var resp = window.document.getElementById('resp')
        var sexo = window.document.getElementsByName('rd_sexo')
        var genero = ''
        var img = window.document.createElement('img')
        //img.setAttribute('id', 'foto')
        
        if (sexo[0].checked) {
            genero = 'Homem'

            if (idade < 10) {
                img.setAttribute('src', 'masc_crianca.png')
            } else if (idade < 18) {
                img.setAttribute('src', 'masc_adolescente.png')
            } else if (idade < 50) {
                img.setAttribute('src', 'masc_jovem.png')
            } else {
                img.setAttribute('src', 'masc_idoso.png')
            }
        } else {
            genero = 'Mulher'

            if (idade < 10) {
                img.setAttribute('src', 'fem_crianca.png')
            } else if (idade < 18) {
                img.setAttribute('src', 'fem_adolescente.png')
            } else if (idade < 50) {
                img.setAttribute('src', 'fem_jovem.png')
            } else {
                img.setAttribute('src', 'fem_idoso.png')
            }
        }
        resp.style.textAlign = 'center'
        resp.innerHTML = `<p>${genero} de ${idade} anos</p>`
        resp.appendChild(img)
    }    
}