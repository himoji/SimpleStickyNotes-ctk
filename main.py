import tkinter
import tkinter.messagebox
import customtkinter
import os

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

dir_name = f"{os.path.abspath(os.getcwd())}\\files"
path_names = os.listdir(dir_name)

def create_file(name):
	file = open(f"{dir_name}\\{name}", "a")
	file.close()
	print(f"created {name} at {dir_name}")
	print(f"path_names {path_names}")

def open_file(name):
	editWindow = TextEditApp(name)
	editWindow.mainloop()

class MainApp(customtkinter.CTk):
	def __init__(self):
		super().__init__()

		# configure window
		self.title("StickyNotes")
		self.geometry(f"{300}x{270}")

		# create sidebar frame with widgets
		self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
		self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
		self.sidebar_frame.grid_rowconfigure(4, weight=1)

		# create scrollable frame
		self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text=dir_name)
		self.scrollable_frame.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")
		self.scrollable_frame.grid_columnconfigure(1, weight=0)
		self.scrollable_frame_switches = []
		for i in range(len(path_names)):
			switch = customtkinter.CTkButton(master=self.scrollable_frame, text=f"{path_names[i]}", command=lambda: open_file(path_names[i]))
			switch.grid(row=i, column=0, padx=10, pady=(0, 20))
			self.scrollable_frame_switches.append(switch)

class TextEditApp(customtkinter.CTk):
	def __init__(self, file_name):
		super().__init__()
		self.file_name = file_name

		def open_file_text(name):
			try:
				file = open(f"{dir_name}\\{name}", "r")
				read_data = file.read()
				file.close()
				return read_data
			except Exception as err:
				print(f"[OPEN] {err} - {name}")
				

		def save_file(name):
			try:
				file = open(f"{dir_name}\\{name}", "w")
				text = self.textbox.get("1.0",'end-1c')
				file.write(text)
				file.close()
			except Exception as err:
				print(f"[SAVE] {err} - {name}")

		# configure window
		self.title("StickyNotesEditor")
		self.geometry(f"{1100}x{580}")

		# configure grid layout (2x2)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=0)
		self.grid_rowconfigure(0, weight=0)
		self.grid_rowconfigure(1, weight=1)

		# create textbox
		self.textbox = customtkinter.CTkTextbox(self, width=1100)
		self.textbox.grid(row=1, column=0, rowspan=2, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

		# create main entry and button
		self.entry = customtkinter.CTkEntry(self, placeholder_text=f"{file_name}")
		self.entry.grid(row=0, column=0, padx=(20, 0), pady=(20, 20), sticky="e")

		self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Save", command=lambda: save_file(file_name))
		self.main_button_1.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="e")

		# set default values
		self.textbox.insert("0.0", open_file_text(file_name))

		

if __name__ == "__main__":
	print("zxc",os.getcwd())
	app = MainApp()
	create_file("awww.txt")
	app.mainloop()
	
