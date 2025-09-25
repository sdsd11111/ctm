const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

// Servir archivos estáticos
app.use(express.static(__dirname));

// Redirigir todas las rutas a index.html para SPA
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
  console.log('Presiona Ctrl+C para detener el servidor');
});
