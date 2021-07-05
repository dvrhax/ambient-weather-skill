from mycroft import MycroftSkill, intent_file_handler


class AmbientWeather(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('weather.ambient.intent')
    def handle_weather_ambient(self, message):
        self.speak_dialog('weather.ambient')


def create_skill():
    return AmbientWeather()

