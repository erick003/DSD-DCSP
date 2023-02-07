const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

app.use(express.json());

// Defina as rotas do Gateway de API
app.get('/api/:resource', async (req, res) => {
  const resource = req.params.resource;
  const response = await axios.get(`https://exemplo.com/api/${resource}`);
  res.send(response.data);
});

app.post('/api/:resource', async (req, res) => {
  const resource = req.params.resource;
  const data = req.body;
  const response = await axios.post(`https://exemplo.com/api/${resource}`, data);
  res.send(response.data);
});

app.listen(PORT, () => {
  console.log(`Gateway de API iniciado na porta ${PORT}`);
});