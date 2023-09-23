document.getElementById('btn').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const city = document.getElementById('input').value;
    const apiKey = '53c8cf556a0cbe083d6f3830806309d8'; 
  
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=imperial`;
  
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        const weather_des = document.getElementById('weather_des');
  
        if(data.cod === '404') {
          weather_des.innerHTML = 'City not found :(';
        } else {
          const temperature = data.main.temp;
          const description = data.weather[0].description;
          weather_des.innerHTML = `${temperature}°F<br>${description}`;
        }
      })
      .catch(error => {
        console.error('Error fetching weather data:', error);
      });
  });
  