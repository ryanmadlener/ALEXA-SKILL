# Ryan's Weather App (Alexa Skill)

Ryan's Weather App is an Alexa skill that takes a user defined zipcode and returns the temperature in the zipcode in celsius and fahrenheit

## How To Use The Skill

The invocation name is "ryan's weather app", meaning to utilize the skill you must say,

```
Alexa, open ryans weather app
```

To recieve the information about the weather in your zipcode, simply say,

```
Alexa, ask ryans weather app whats the weather in _your zipcode_
```

Alexa will then respond with, 

```
"The temperature in *your zipcode* is 32 degrees celsius and 90 degrees fahrenheit"
```

Alexa: 


The skill uses an OpenWeatherMap API to get the temperature data in kelvin, which I then convert to celsius and fahrenheit.



