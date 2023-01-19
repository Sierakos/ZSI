import tkinter as tk
from tkinter import ttk
from turtle import bgcolor
import chart
from concurrent import futures
import time
# from tkinter.messagebox import showinfo

thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    self.temperature = 0
    self.oczek = 0

    # configure the root window
    self.title('My Awesome App')
    self.geometry('720x400')

    # label
    self.label = ttk.Label(self, text='Projekt inteligentnego domu')
    self.label.grid(row=0,column=0,padx=5,pady=5)

    # button
    # self.button = ttk.Button(self, text='Click Me')
    # self.button['command'] = self.button_clicked
    # self.button.grid(row=1,column=0,padx=5,pady=5)

    # main layout
    self.main_frame = tk.Frame(self, width=700, height=400, bg='red')
    self.main_frame.grid(row=1,column=0,padx=5,pady=5)

    # four xd layouts
    self.left_frame = tk.Frame(self.main_frame, width=200, height=350, bg='gray')
    self.left_frame.grid(row=0,column=0,padx=5,pady=5)

    self.center_frame = tk.Frame(self.main_frame, width=200, height=350, bg='gray')
    self.center_frame.grid(row=0,column=1,padx=5,pady=5)

    self.right_frame = tk.Frame(self.main_frame, width=200, height=350, bg='gray')
    self.right_frame.grid(row=0,column=2,padx=5,pady=5)

    self.bottom_frame = tk.Frame(self.main_frame, width=200, height=350, bg='yellow')
    self.bottom_frame.grid(row=1,column=0,padx=5,pady=5)

    # output
    self.temp_label = tk.Label(self.left_frame, text='0°C', bg='gray')
    self.temp_label.grid(row=0,column=0,padx=100,pady=5)

    self.zal_label = tk.Label(self.center_frame, text='25°', bg='gray')
    self.zal_label.grid(row=0,column=0,padx=100,pady=5)

    self.wil_label = tk.Label(self.right_frame, text='75%', bg='gray')
    self.wil_label.grid(row=0,column=0,padx=100,pady=5)

    # input
    self.temp_entry_label = tk.Label(self.left_frame, text='temp. aktualna:', bg='gray')
    self.temp_entry_label.grid(row=1,column=0,padx=0,pady=5)

    self.temp_entry = tk.Entry(self.left_frame)
    self.temp_entry.grid(row=2,column=0,padx=0,pady=5)

    self.temp_entry_label_2 = tk.Label(self.left_frame, text='temp. oczekiwana:', bg='gray')
    self.temp_entry_label_2.grid(row=3,column=0,padx=0,pady=5)

    self.temp_entry_2 = tk.Entry(self.left_frame)
    self.temp_entry_2.grid(row=4,column=0,padx=0,pady=5)

    self.zal_entry = tk.Entry(self.center_frame)
    self.zal_entry.grid(row=1,column=0,padx=0,pady=5)

    self.wil_entry = tk.Entry(self.right_frame)
    self.wil_entry.grid(row=1,column=0,padx=0,pady=5)

    # buttons
    self.temp_button = tk.Button(self.left_frame, text="Insert", command=self.assign_temp)
    self.temp_button.grid(row=5,column=0,padx=0,pady=5)

    self.zal_button = tk.Button(self.center_frame, text="Insert")
    self.zal_button.grid(row=2,column=0,padx=0,pady=5)

    self.wil_button = tk.Button(self.right_frame, text="Insert")
    self.wil_button.grid(row=2,column=0,padx=0,pady=5)

    self.zeg_button = tk.Button(self.bottom_frame, text="włącz", command=self.button_clicked)
    self.zeg_button.grid(row=0,column=0,padx=0,pady=5)


    # self.te(str(self.temperature))


  def te(self, temp, oczek):
    while True:
      self.temperature = self.temperature
      temps = chart.temp_control(temp, oczek)
      if temps[0] >= 1 and temps[1] == 0:
        self.temperature += temps[0]
      elif temps[0] == 1:
        self.temperature = self.temperature
      elif temps[1] >= 1 and temps[0] == 0:
        self.temperature -= temps[1]

      self.temp_label['text'] = str(self.temperature) + '°C'
    

  def button_clicked(self, text=''):
    thread_pool_executor.submit(self.blocking_code)
    #self.te(self.temperature, self.oczek)

  def blocking_code(self):
    self.after(0, self.set_label_text, 'running')

    for i in range(10):
      self.after(0, self.funkcja, self.temperature, self.oczek)
      print(i)
      time.sleep(3)

    self.after(0, self.set_label_text, ' not running')

  def funkcja(self, temp, oczek):
    self.temperature = self.temperature
    temps = chart.temp_control(temp, oczek)
    if temps[0] >= 1 and temps[1] == 0:
      self.temperature += temps[0]
    elif temps[0] == 1:
      self.temperature = self.temperature
    elif temps[1] >= 1 and temps[0] == 0:
      self.temperature -= temps[1]

    self.temp_label['text'] = str(self.temperature) + '°C'

  def set_label_text(self, text=''):
    self.temp_label['text'] = str(self.temperature) + '°C'

  def assign_temp(self):
    self.temperature = int(self.temp_entry.get())
    self.oczek = int(self.temp_entry_2.get())
    self.temp_label['text'] = str(self.temperature) + '°C'

if __name__ == "__main__":
  app = App()
  app.mainloop()