#!/bin/env python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

class ParamInput(BoxLayout):
    value = StringProperty('')
    label_text = StringProperty('Param label')

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class ParamInputText(ParamInput):
    pass


class ParamInputDropdown(ParamInput):
    pass


class ParamInputBoolean(ParamInput):
    pass


class ParamInputPopup(ParamInput):
    pass


class ParamInputBrowseFile(ParamInput):
    pass


class FormPanel(BoxLayout):
    def send_params(self):
        print('Params: ')
        for key, param in self.ids.items():
            if isinstance(param, ParamInput):
                print("{0}: {1}".format(key, param.get_value()))


class ShowcaseApp(App):

    def build(self):
        return FormPanel()


if __name__ == '__main__':
    ShowcaseApp().run()
