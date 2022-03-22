from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window

import tkinter as tk
from tkinter import filedialog

class TrackingApp(App):
    def build(self):
        current_width, current_height = Window.size

        self.window = BoxLayout(orientation="vertical")
        self.window.padding = 20

        self.main_logo = Image(source="logo-placeholder.png",
                                     pos_hint={"center_x": 0.5},
                                     size_hint=(0.5, None))
        self.window.add_widget(self.main_logo)

        self.pane_split = BoxLayout(orientation="horizontal")
        self.window.add_widget(self.pane_split)

        self.left_pane = BoxLayout(orientation="vertical")
        self.pane_split.add_widget(self.left_pane)
        self.left_pane.size_hint = (0.6, 0.8)
        self.right_pane = BoxLayout(orientation="vertical")
        self.pane_split.add_widget(self.right_pane)
        self.right_pane.size_hint = (0.4, 0.8)

        #Model path selection widgets
        self.model_selection_prompt = Label(text="Please select the location of the saved model file:",
                                            font_size=18,
                                            )
        self.model_selection_prompt.bind(size=self.model_selection_prompt.setter('text_size')) 
        self.left_pane.add_widget(self.model_selection_prompt)

        self.model_selection_pane = BoxLayout(orientation="horizontal")
        self.left_pane.add_widget(self.model_selection_pane)

        self.model_btn = Button(text="Choose",
                                size_hint=(None, None),
                                bold=True,
                                height=current_height//16.6,
                                width=current_width//7.68)
        self.model_selection_pane.add_widget(self.model_btn)
        self.model_btn.bind(on_press=self.selectModel)

        self.model_path_field = TextInput(multiline=False,
                                        padding_y=(5,5),
                                        font_size=18,
                                        #size_hint=(0.4, 0.3),
                                        size_hint=(0.4, None),
                                        height=current_height//16.6,)
                                        #width=self.left_pane.size[0])
        self.model_selection_pane.add_widget(self.model_path_field)

        #Input path selection widgets
        self.input_selection_prompt = Label(text="Please select a file or directory for input:",
        font_size=18,)
        self.input_selection_prompt.bind(size=self.input_selection_prompt.setter('text_size'))
        self.left_pane.add_widget(self.input_selection_prompt)

        self.input_selection_pane = BoxLayout(orientation="horizontal")
        self.left_pane.add_widget(self.input_selection_pane)

        self.input_btn = Button(text="Choose",
                                size_hint=(None, None),
                                bold=True,
                                height=current_height//16.6,
                                width=current_width//7.68)
        self.input_selection_pane.add_widget(self.input_btn)
        self.input_btn.bind(on_press=self.selectInput)

        self.input_path_field = TextInput(multiline=False,
                                        padding_y=(5,5),
                                        font_size=18,
                                        size_hint=(0.4, None),
                                        height=current_height//16.6)
        self.input_selection_pane.add_widget(self.input_path_field)

        #Output path selection widgets
        self.output_selection_prompt = Label(text="Please select a directory to save results to:",
        font_size=18,)
        self.output_selection_prompt.bind(size=self.output_selection_prompt.setter('text_size'))
        self.left_pane.add_widget(self.output_selection_prompt)

        self.output_selection_pane = BoxLayout(orientation="horizontal")
        self.left_pane.add_widget(self.output_selection_pane)

        self.output_btn = Button(text="Choose",
                                size_hint=(None, None),
                                bold=True,
                                height=current_height//16.6,
                                width=current_width//7.68)
        self.output_selection_pane.add_widget(self.output_btn)
        self.output_btn.bind(on_press=self.selectOutput)

        self.output_path_field = TextInput(multiline=False,
                                        padding_y=(5,5),
                                        font_size=18,
                                        size_hint=(0.4, None),
                                        height=current_height//16.6)
        self.output_selection_pane.add_widget(self.output_path_field)


        # #self.classification_box = BoxLayout(orientation="horizontal")
        # self.classification_box = GridLayout(cols=2)
        # #self.classification_box.size_hint = (0.5, None)
        # #self.classification_box.pos_hint = {"center_x": 0.4}
        # self.right_pane.add_widget(self.classification_box)
        # self.classification_label = Label(text="Classification model:")
        # self.classification_label.bind(size=self.classification_label.setter('text_size'))
        # self.classification_checkbox = CheckBox(group="model_type")
        # self.classification_box.add_widget(self.classification_label)
        # self.classification_box.add_widget(self.classification_checkbox)

        # self.detection_box = BoxLayout(orientation="horizontal")
        # self.detection_box.size_hint = (0.5, None)
        # self.detection_box.pos_hint = {"center_x": 0.4}
        # self.right_pane.add_widget(self.detection_box)
        # self.detection_label = Label(text="Detection model:")
        # self.classification_label.bind(size=self.classification_label.setter('text_size'))
        # self.detection_checkbox = CheckBox(group="model_type")
        # self.detection_box.add_widget(self.detection_label)
        # self.detection_box.add_widget(self.detection_checkbox)

        self.model_type_box = GridLayout(cols=2)
        # Add checkbox, widget and labels
        self.model_type_box.add_widget(Label(text ='Detection'))
        self.active = CheckBox(group='model_type')
        self.model_type_box.add_widget(self.active)
 
        self.model_type_box.add_widget(Label(text ='Classification'))
        self.active = CheckBox(active = True, group='model_type')
        self.model_type_box.add_widget(self.active)

        self.right_pane.add_widget(self.model_type_box)


        self.start_btn = Button(text="Begin",
                                size_hint=(None, None),
                                bold=True,
                                height=current_height//16.6,
                                width=current_width//7.68,
                                pos_hint={"center_x": 0.5})
        self.right_pane.add_widget(self.start_btn)


        self.cancel_btn = Button(text="Cancel",
                                size_hint=(None, None),
                                bold=True,
                                height=current_height//16.6,
                                width=current_width//7.68,
                                pos_hint={"center_x": 0.5})
        self.right_pane.add_widget(self.cancel_btn)


        return self.window

    def selectModel(self, *args):
        root = tk.Tk()
        root.withdraw()
        path = filedialog.askopenfilename()
        self.model_path_field.text = str(path)

    def selectInput(self, *args):
        root = tk.Tk()
        root.withdraw()
        path = filedialog.askopenfilename()
        self.input_path_field.text = str(path)

    def selectOutput(self, *args):
        root = tk.Tk()
        root.withdraw()
        path = filedialog.askopenfilename()
        self.output_path_field.text = str(path)


if __name__ == "__main__":
    TrackingApp().run()