import serial  
import time  
import tkinter as tk  

class RGBColorPicker:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("RGB Color Picker")  

        # Serial setup  
        self.serial_port = serial.Serial('COM10', 115200, timeout=1)  

        # Initial RGB values  
        self.red = tk.IntVar(value=128)  
        self.green = tk.IntVar(value=128)  
        self.blue = tk.IntVar(value=128)  

        # Create sliders for RGB values  
        self.create_slider("Red", self.red, 0, 255)  
        self.create_slider("Green", self.green, 0, 255)  
        self.create_slider("Blue", self.blue, 0, 255)  

        # Frame to display the color  
        self.color_frame = tk.Frame(self.root, width=200, height=200)  
        self.color_frame.pack(pady=10)
        self.update_color()  

    def create_slider(self, name, variable, min_val, max_val):  
        frame = tk.Frame(self.root)  
        frame.pack(fill=tk.X, padx=5, pady=5)  

        label = tk.Label(frame, text=name)  
        label.pack(side=tk.TOP)  

        slider = tk.Scale(frame, from_=min_val, to=max_val, orient=tk.HORIZONTAL,  
                          variable=variable, command=lambda x: self.update_color())  
        slider.pack(side=tk.RIGHT, fill=tk.X, expand=True)  

    def update_color(self):  
        r = self.red.get()  
        g = self.green.get()  
        b = self.blue.get()  
        color_str = f'#{r:02x}{g:02x}{b:02x}'  
        self.color_frame.config(bg=color_str) 
        time.sleep(0.1)
        self.send_rgb(r, g, b) 

    def send_rgb(self, red, green, blue):  
        rgb_byte = bytes([red,green,blue])  
        self.serial_port.write(rgb_byte)
        # self.serial_port.close() 

if __name__ == "__main__":  
    root = tk.Tk()  
    app = RGBColorPicker(root)  
    root.mainloop()
