const stats=600;

switch (stats) {
    case 200:
        console.log('ok!')
        break;
    case 400:
    case 600:
        console.log('bad robot!')
        break;
    default:
        console.log('default!')
    break;
}