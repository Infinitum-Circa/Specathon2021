from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner
class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.connect_page = MainPage()
        screen = Screen(name='MainPage')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)
        self.info_page = FarmerPage()
        screen = Screen(name='Farmer')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)
        return self.screen_manager
class MainPage(BoxLayout):  
    def callback(self, instance):
        app.info_page.update_info("Welcome "+self.text,"City: "+self.city,"Soil Type: "+self.soil_type,"Plot Size: "+str(self.plot_value))
        #pp.info_page.no_of_crops(self.soil_type)
        app.screen_manager.current = 'Farmer'
    def __init__(self,**kwargs):
        self.text="Name"
        self.city="Chennai"
        self.soil_type="Heavy-clayey"
        self.plot_value=int(100)
        def on_text(instance, value):
            print('The widget', instance, 'have:', value)
            self.text=value
        def on_text2(instance, value):
            print('The widget', instance, 'have:', value)
            self.plot_value=int(value)
        def show_selected_value(spinner, text):
            print('The spinner', spinner, 'has text', text)
            self.soil_type=text
        def show_selected_value2(spinner, text):
            print('The spinner', spinner, 'has text', text)
            self.city=text
        super().__init__(**kwargs)
        self.orientation='vertical'
        img = Image(source='6seasons.jpeg',
                    size_hint=(None, None),
                    pos_hint={'center_x':.5, 'center_y':.5})
        label = Label(text='6 Seasons',
                      size_hint=(None, None),
                      pos_hint={'center_x': .5, 'center_y': .5})
        soil=('Heavy-clayey','clayey-loam','Deep-heavy clay','light sandy loam','loam','well-drained-sandy loams','Red Cotton','Black Cotton','Well-drained alluvium','brown regur soil','red regur soil','black regur soil','Well-drained-loamy soil','Regur','light loamy Soil','rich-well-drained alluvial','Rich loam','sandy alluvial','lateritic red','Deep-loamy','Red alluvial','rich in hums','red loam','sandy loam','well-drained lateritic')
        spinner=Spinner(text="Soil type",values=soil,size_hint =(None, None),size=(200, 44),pos_hint={'center_x': .5, 'center_y': .5})
        spinner.bind(text=show_selected_value)
        City=['Hyderabad','Vijayawada','Chennai','Coimbatore']
        spinner2=Spinner(text="City",values=City,size_hint =(None, None),pos_hint={'center_x': .5, 'center_y': .5},size=(200, 44))
        spinner2.bind(text=show_selected_value2,)
        img2 = Image(source='Infinitum Circa.png',
                    size_hint=(None, None),
                    pos_hint={'center_x':.5, 'center_y':.5})
        textinput = TextInput(text="Name",multiline=False,size_hint=(None,None),size=(100, 44),pos_hint={'center_x':.5, 'center_y':.5})
        textinput.bind(text=on_text)
        textinput2 = TextInput(text="Plot Area",multiline=False,size_hint=(None,None),size=(100, 44),pos_hint={'center_x':.5, 'center_y':.5})
        textinput2.bind(text=on_text2)
        button3 = Button(text='Submit', size_hint=(None, None),pos_hint={'center_x': .5, 'center_y': .5},size=(200, 50))
        button3.bind(on_press=self.callback)
        layout= self
        layout.add_widget(img)
        layout.add_widget(label)
        layout.add_widget(spinner)
        layout.add_widget(spinner2)
        layout.add_widget(textinput)
        layout.add_widget(textinput2)
        layout.add_widget(img2)
        layout.add_widget(button3)
        #return layout
class FarmerPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        self.orientation='vertical'
        self.message1=(Label(text='Name',size_hint =(None, None),size=(200, 44),
                    pos_hint={'center_x':.5, 'center_y':.5}))
        self.message2=(Label(text="City",size_hint =(None, None),size=(200, 44),
                    pos_hint={'center_x':.5, 'center_y':.5}))
        self.message3=(Label(text="Soil type",size_hint =(None, None),size=(200, 44),
                    pos_hint={'center_x':.5, 'center_y':.5}))
        img2 = Image(source='Infinitum Circa.png',
                    size_hint=(None, None),
                    pos_hint={'center_x':.5, 'center_y':.5})
        self.message4=(Label(text='Name',size_hint =(None, None),size=(200, 100),
                    pos_hint={'center_x':.5, 'center_y':.5}))
        self.message5=(Label(text='Plot Size',size_hint =(None, None),size=(200, 100),
                    pos_hint={'center_x':.5, 'center_y':.5}))
        self.add_widget(self.message1)
        self.add_widget(self.message5)
        self.add_widget(self.message2)
        self.add_widget(self.message3)
        self.add_widget(self.message4)
        self.add_widget(img2)   
    def update_info(self, message1,message2,message3,message4):
        self.message1.text = message1
        self.message2.text = message2
        self.message3.text = message3
        self.message5.text = message4
        crops={'Heavy-clayey': [' Rice', 'Wheat   '],
 'clayey-loam': [' Rice', 'Millets   ', 'Lentil', 'Oilseeds'],
 'Deep-heavy clay': ['Maize'],
 'light sandy loam': ['Maize'],
 'loam': ['Bajra', 'Lentil'],
 'well-drained-sandy loams': ['Wheat   ', 'Groundnut'],
 'Red Cotton': ['Groundnut'],
 'Black Cotton': ['Groundnut'],
 'Well-drained alluvium': ['Sugarcane', 'Coffee', 'Cocoa', 'Jute', 'Oil-palm'],
 'brown regur soil': ['Sugarcane'],
 'red regur soil': ['Sugarcane'],
 'black regur soil': ['Sugarcane'],
 'Well-drained-loamy soil': ['Sugar beet', 'Cotton'],
 'Regur': ['Cotton'],
 'light loamy Soil': ['Tea'],
 'rich-well-drained alluvial': ['Rubber'],
 'Rich loam': ['Flax'],
 'sandy alluvial': ['Coconut'],
 'lateritic red': ['Coconut'],
 'Deep-loamy': ['Oil-palm'],
 'Red alluvial': ['Clove'],
 'rich in hums': ['Black Pepper'],
 'red loam': ['Turmeric '],
 'sandy loam': ['Millets   ', 'Bajra', 'Pulses', 'Black Pepper'],
 'well-drained lateritic': ['Cardamom ']}
        no_of_crops=len(crops[message3.replace("Soil Type: ","")])
        land_size=int(message4.replace("Plot Size: ",""))
        crop_price=[1,14,3,5,9,12,45,6,8]
        def cons_f(x):
            return x.sum()
        def profit(x):
            profit2=0
            for i in range(no_of_crops):
                profit2=profit2+(x[i]*crop_price[i])
            return -1*(profit2) 
        from scipy.optimize import NonlinearConstraint, minimize,Bounds
        import numpy as np
        nonlinear_constraint = NonlinearConstraint(cons_f, land_size-1, land_size)
        bounds = Bounds([0]*no_of_crops,[land_size/3]*no_of_crops)
        x0 = np.zeros(no_of_crops)
        res = minimize(profit, x0,constraints=[nonlinear_constraint], bounds=bounds)#,options={'verbose': 1})
        text=""
        for i in range(len(crops[message3.replace("Soil Type: ","")])):
            text=text+crops[message3.replace("Soil Type: ","")][i]+" "+str(round(res.x[i]))+"\n"
        self.message4.text=text
text="Name"
if __name__ == '__main__':
    app = MainApp()
    app.run()

