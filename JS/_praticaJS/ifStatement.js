/* operators
comparing values
>
<
<=
>=
== same
=== identical
!= 
!== 
*/

const status='200';

/* if (status === '200'){
    console.log('ok!')
} else if (status === 400) {
    console.log('Erro!')
} else {
    console.log('NaN')
} */
/* if (status === '200') console.log('ok!');
else if (status === 400) console.log('Erro!');
else console.log('NaN'); */

const message=(status===200)?'ok':'erro'; //oh boy!
console.log(message)