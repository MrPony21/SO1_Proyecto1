const express = require('express');
const app = express()
const port = 3000;

app.get('/',(req, res) => {
    res.send('Hola mundo de node js con docker')
})

app.listen(port, () => {
    console.log(`Servidor esta corriendo en puerto ${port}`)
})