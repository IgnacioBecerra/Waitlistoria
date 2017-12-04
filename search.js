const axios = require('axios')

axios.get('https://api.github.com/users/' + 'IgnacioBecerra')
  .then(function(response){
    console.log(response.data);
    console.log(response.status);
  });  