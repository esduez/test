const axios = require('axios');

async function fetchTeaRewards(userId) {
  const response = await axios.get('https://api.tea.xyz/rewards', {
    params: { user: userId }
  });
  return response.data;
}

module.exports = { fetchTeaRewards };
