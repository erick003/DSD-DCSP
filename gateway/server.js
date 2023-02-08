const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

app.use(express.json());

app.post('/api/realizar-luta/', async (req, res) => {
  const data = req.body;
  const response = await axios.post('http://localhost:8000/api/boxeadores/realizar-luta/', data);
  res.send(response.data);
});

app.get('/api/:resource/', async (req, res) => {
  const resource = req.params.resource;
  const response = await axios.get(`http://localhost:8000/api/${resource}/`);
  res.send(response.data);
});

app.listen(PORT, () => {
  console.log(`Gateway de API iniciado na porta ${PORT}`);
});