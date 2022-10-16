import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import re
import json

from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.label import Label

values = []

class Home(Screen):
    def next(self):
        self.manager.current = 'Home_Reg'



class Register1(Screen):

    email = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    def val_email(self):
        if bool(re.match('^[.\w+-]+@[A-Za-z0-9]+\.[a-zA-Z]{1,3}$', self.email.text)) is True:
            self.manager.current = 'Reg2'

    def store(self):
        values.append(self.username.text)
        values.append(self.email.text)
        values.append(self.password.text)
        values.append("Cartype Placebolder")




class Register2(Screen):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f'Your car: {value}'
        values[3] = value


    def get_name(self):
        if not values:
            return None
        return values

    def Reg_Submit(self):
        with open("users.json", 'r+') as file:

            file_data = json.load(file)
            new_data = {"name": values[0],
                        "email": values[1],
                        "password:": values[2],
                        "cartype": values[3]
                        }
            # Join new_data with file_data inside Users
            file_data["Users"].append(new_data)

            print(file_data)

            file.seek(0)
            # Convert it back to json.
            json.dump(file_data, file, indent=2)

            file.close()




class Home_Reg(Screen):
    def on_pre_enter(self, *args):
        file = open('users.json')
        data = json.load(file)
        length = len(data['Users'])

        self.ids.Custom_Welcome.text = f"Welcome, {data['Users'][length-1]['name']}!"


# createdb(values[0], values[1], values[2], values[3])

class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class WindowManager(ScreenManager):
    pass


sm = WindowManager()

sm.add_widget(Home(name='Home'))
sm.add_widget(Home(name='Home_Reg'))
sm.add_widget(Register1(name='Reg1'))
sm.add_widget(Register2(name='Reg2'))



class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "700"
        # kv = Builder.load_file('my.kv')
        # return kv

if __name__ == "__main__":
    MyApp().run()




