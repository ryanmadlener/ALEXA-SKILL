import requests

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return(launch(event, context))
    elif event['request']['type'] == "IntentRequest":
        return(intent_router(event, context))

def launch(event, context):
    return(statement("Greetings", "Hello user"))
    
def statement(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = build_Speech(body)
    speechlet['body'] = build_Card(title, body)
    speechlet['shouldEndSession'] = True
    return(build_response(speechlet))
    
def build_Speech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = body
    return(speech)
    
def build_Card(title, body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
    return(card)
    
def build_response(message, session_attributes = {}):
    response = {}
    response['Version'] = "1.0"
    response['session_attributes'] = session_attributes
    response['response'] = message
    return(response)

def intent_router(event, context):
    intent = event['request']['intent']['name']
    if intent == "TemperatureIntent":  
        return(temperature_intent(event, context)) 

    #REQUIRED INTENTS
    if intent == "AMAZON.HelpIntent":
        return(help_intent())
    if intent == "AMAZON.CancelIntent":
        return(cancel_intent())
    if intent == "AMAZON.StopIntent":
        return(stop_intent())
    if intent == "AMAZON.FallBackIntent":
        return(fall_back_intent())
    if intent == "AMAZON.NavigateHomeIntent":
        return(navigate_home_intent())

def temperature_intent(event, context): 
    original = event['request']['intent']['slots']
    user_defined_zipcode = original['zipcode']['value']
    temperature_kelvin = get_temp(user_defined_zipcode)
    temperature_fahrenheit = convert_to_fahrenheit(temperature_kelvin)
    temperature_celsius = convert_to_celsius(temperature_kelvin)
    return(statement("Temperature", "The temperature in " + str(user_defined_zipcode[0])
                    + " " + str(user_defined_zipcode[1]) + " " + str(user_defined_zipcode[2])
                    + " " + str(user_defined_zipcode[3]) + " " + str(user_defined_zipcode[4])
                    + " is " + temperature_celsius + " celsius and " + temperature_fahrenheit
                    + " fahrenheit"))

def get_temp(user_zipcode):
    weather = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=" + 
                            str(user_zipcode) + ",us&appid=1702ad888c2f7c1f299f97db731b64b6")
    json_format = weather.json()
    temp_kelvin = float(json_format["main"]["temp"])
    return(temp_kelvin)

def convert_to_fahrenheit(kelvin):
    temp_fahrenheit = 1.8 * (kelvin - 273) + 32
    return("%02d degrees" % temp_fahrenheit)

def convert_to_celsius(kelvin):
    temp_celsius = kelvin - 273.15
    return("%02d degrees" % temp_celsius)


#REQUIRED INTENT FUNCTIONS
def help_intent():
    return(statement("HelpIntent", "You need help"))

def cancel_intent():
    return(statement("CancelIntent", "You have cancelled your request"))

def stop_intent():
    return(statement("StopIntent", " "))

def fall_back_intent():
    return(statement("FallBackIntent", " "))

def navigate_home_intent():
    return(statement("NavigateHomeIntent", " "))