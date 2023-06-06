import tkinter
import tkinter.messagebox
import customtkinter
import csv, json, logging, time
from tkinter import filedialog
from tkinter import ttk

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.activated = False
        self.button_state = "disabled"
        self.key = "KEY: xxxxxx xxxx xxx xxxxx."
        self.key_status = "STATUS: License not Active."
        self.progress_row = 0
        logging.basicConfig(filename='logger.log', level=logging.DEBUG,
                        format='%(asctime)s- [*] %(message)s')
        
        
        #set default csv file which is the last upload csv file.
        self.file = './generator.csv'

        # configure window
        self.title("Nike Accounts Creator")
        self.geometry(f"{1000}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Account Actions", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Lisence Key", command=self.license_view)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)   
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Create Accounts", command=self.create_accounts_view)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Settings", command=self.settings_view)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Progress", command=self.progress_View)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))

        self.tabview = customtkinter.CTkTabview(self, width=650, height=1000)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(10, 0), sticky="w")
        self.tabview.add("License Activation")
        self.tabview.tab("License Activation").grid_columnconfigure(1, weight=1)  # configure grid of individual tabs
        self.change_appearance_mode_event("Light")

        if self.activated:
            status_label = customtkinter.CTkLabel(self.tabview.tab("License Activation"), text=self.key_status)
            status_label.grid(row=1, column=0, padx=20, pady=(20, 10))

            status_label_1 = customtkinter.CTkLabel(self.tabview.tab("License Activation"), text=self.key)
            status_label_1.grid(row=0, column=0, padx=20, pady=(20, 10))

            # Enable other functionalities here
        
        else:
            status_label = customtkinter.CTkLabel(self.tabview.tab("License Activation"), text=self.key_status)
            status_label.grid(row=1, column=0, padx=20, pady=(20, 10))

            status_label_1 = customtkinter.CTkLabel(self.tabview.tab("License Activation"), text=self.key)
            status_label_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        
            self.string_input_button = customtkinter.CTkButton(self.tabview.tab("License Activation"),\
                text="Activate License",command=self.open_input_dialog_event)
            self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

    
    def license_view(self):
        # Create main entry and button
        self.tabview = customtkinter.CTkTabview(self, width=650, height=1000)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(10, 0), sticky="w")
        self.tabview.add("License Activation")
        self.tabview.tab("License Activation").grid_columnconfigure(1, weight=1)  # configure grid of individual tabs
        

        if self.activated:
            status_label = customtkinter.CTkLabel(self.tabview.tab("License Activation"), text=self.key_status)
            status_label.grid(row=1, column=0, padx=20, pady=(20, 10))

            status_label_1 = customtkinter.CTkLabel(self.tabview.tab("License Activation"), text=self.key)
            status_label_1.grid(row=0, column=0, padx=20, pady=(20, 10))

            # Enable other functionalities here
        else:
            status_label = customtkinter.CTkLabel(self.tabview.tab("License Activation"), text=self.key_status)
            status_label.grid(row=1, column=0, padx=20, pady=(20, 10))

            status_label_1 = customtkinter.CTkLabel(self.tabview.tab("License Activation"), text=self.key)
            status_label_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        
            self.string_input_button = customtkinter.CTkButton(self.tabview.tab("License Activation"),\
                text="Activate License",command=self.open_input_dialog_event)
            self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

    
    def create_accounts_view(self):
        # Create main entry and button
        self.tabview = customtkinter.CTkTabview(self, width=650, height=1000)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(10, 0), sticky="w")
        self.tabview.add("Create Accounts")
        self.tabview.tab("Create Accounts").grid_columnconfigure(1, weight=1)  # configure grid of individual tabs

        if self.activated:
            self.data = self.read_csv_file(self.file)
            self.filtered_data = [row for row in self.data if row[-1] == "Status"]
            self.row_number = len(self.filtered_data)
            self.number = f"{self.row_number} Pending accounts"

            self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Create Accounts"),\
                text="Upload Csv file",command=self.file_upload)
            self.string_input_button.grid(row=0, column=0,padx=(30, 10), pady=(20, 0), sticky="w")

            status_label = customtkinter.CTkLabel(self.tabview.tab("Create Accounts"), text=self.number)
            status_label.grid(row=2, column=0, padx=20, pady=(20, 10))


            self.table = ttk.Treeview(self.tabview.tab("Create Accounts"), columns=("Column 0", "Column 1", "Column 2", "Column 3", "Column 4", "Column 5"))
            self.table.grid(row=3, column=0, padx=(30, 0), pady=(20, 0), sticky="nsew")

            self.table.column("#0", width=0)  #Set the width of the first column
            self.table.column("Column 0", width=90)
            self.table.column("Column 1", width=90)
            self.table.column("Column 2", width=90)
            self.table.column("Column 3", width=90)
            self.table.column("Column 4", width=60)
            self.table.column("Column 5", width=150)

            self.table.tag_configure("header", background="gray")  #Change the background color of the header row
            self.table.heading("Column 0", text="Email", anchor="w")
            self.table.heading("Column 1", text="First Name", anchor="w")
            self.table.heading("Column 2", text="Last Time", anchor="w")
            self.table.heading("Column 3", text="Password", anchor="w")
            self.table.heading("Column 4", text="Country", anchor="w")
            self.table.heading("Column 5", text="Proxy", anchor="w")

            self.table.delete(*self.table.get_children())
            for row in self.filtered_data[1:]:
                self.item_id = self.table.insert("", "end", values=row)
                        
            self.button_2 = customtkinter.CTkButton(self.tabview.tab("Create Accounts"), text="Create Accounts", command=self.handle_accounts)
            self.button_2.grid(row=4, column=0, padx=(30, 10), pady=(20, 0), sticky="w")

    
    def settings_view(self):
        # Create main entry and button
        self.tabview = customtkinter.CTkTabview(self, width=650, height=1000)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(10, 0), sticky="w")
        self.tabview.add("Configurations")
        self.tabview.tab("Configurations").grid_columnconfigure(1, weight=1)  # configure grid of individual tabs

        with open("settings.json", "r") as file:
            data = json.load(file)
        
        self.setting1 = data["setting1"]
        self.setting2 = data["setting2"]
        self.setting3 = data["setting3"]
        

        if self.activated:
            self.entry_1 = customtkinter.CTkEntry(self.tabview.tab("Configurations"), placeholder_text=self.setting1, width=400)
            self.entry_1.grid(row=1, column=0, columnspan=2, padx=(100, 0), pady=(20, 20), sticky="w")

            self.entry_2 = customtkinter.CTkEntry(self.tabview.tab("Configurations"), placeholder_text=self.setting2, width=400)
            self.entry_2.grid(row=2, column=0, columnspan=2, padx=(100, 0), pady=(20, 20), sticky="w")

            self.entry_3 = customtkinter.CTkEntry(self.tabview.tab("Configurations"), placeholder_text=self.setting3, width=400)
            self.entry_3.grid(row=3, column=0, columnspan=2, padx=(100, 0), pady=(20, 20), sticky="w")

            status_label = customtkinter.CTkLabel(self.tabview.tab("Configurations"), text="You need help with google account settings?", underline=True,text_color="green")
            status_label.grid(row=4, column=0, padx=(100, 0), pady=(20, 20), sticky="w")
            status_label.bind("<Button-1>", lambda e: self.open_link("https://search.google.com/"))

            status_label = customtkinter.CTkLabel(self.tabview.tab("Configurations"), text="check here to get sms-active website", underline=True,text_color="green")
            status_label.grid(row=5, column=0, padx=(100, 0), pady=(20, 20), sticky="w")
            status_label.bind("<Button-1>", lambda e: self.open_link("https://botustech.com/"))

            self.button_2 = customtkinter.CTkButton(self.tabview.tab("Configurations"), text="Save Configs", command=self.save_configs)
            self.button_2.grid(row=6, column=0, padx=(100, 10), pady=(20, 0), sticky="w")

            self.button_3 = customtkinter.CTkButton(self.tabview.tab("Configurations"),\
                 text="Edit Configs", command=self.edit_configs)
            self.button_3.grid(row=6, column=1, padx=20, pady=(20, 0), sticky="w")
            self.save_configs()

    def progress_View(self):
        # Create main entry and button
        self.tabview = customtkinter.CTkTabview(self, width=650, height=1000)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(10, 0), sticky="w")
        self.tabview.add("Creation Progress")
        self.tabview.tab("Creation Progress").grid_columnconfigure(1, weight=1)  # configure grid of individual tabs

        # Create a label to display progress
        self.progress_label = customtkinter.CTkScrollableFrame(self.tabview.tab("Creation Progress"),\
             label_text="Tracking accounts cretion process", label_text_color="green", width=500, height=400)
        self.progress_label.grid(row=0, column=0, padx=100, pady=(20, 10))

        self.progress_label.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []

        # Start reading the log file and updating the progress label
        log_file_path = "logger.log"  # Replace with the actual path of your log file
        update_interval = 3  # Update interval in seconds

        def update_progress():
            with open(log_file_path, "r") as file:
                progress = file.read().strip()

            # Update the progress label
            self.progress_label.configure()
            switch = customtkinter.CTkLabel(master=self.progress_label, text=f"{progress}")
            switch.grid(row=self.progress_row, column=0, padx=10, pady=(0, 20), sticky="w")

            # Schedule the next update
            self.after(update_interval * 1000, update_progress)

        # Start the first update
        update_progress()

    def edit_configs(self):
        # Enable editing of input fields
        self.entry_1.configure(state="normal")
        self.entry_2.configure(state="normal")
        self.entry_3.configure(state="normal")

    def save_configs(self):
        value_1 = self.entry_1.get()
        value_2 = self.entry_2.get()
        value_3 = self.entry_3.get()

        data = {
            "setting1": value_1,
            "setting2": value_2,
            "setting3": value_3
        }

        # Write the data to the JSON file
        with open("settings.json", "w") as file:
            json.dump(data, file, indent=4)

        # Disable editing of input fields
        self.entry_1.configure(state="disabled")
        self.entry_2.configure(state="disabled") 
        self.entry_3.configure(state="disabled")


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Enter License Key:", title="Key Activation")
        key = dialog.get_input()
        #authenticate the license keys and set the variables apropriatel
        status = "Active" #make sure you authenticate only users that have active license
        if key == "ABCD1234EFGH5678" and status == "Active":
            self.activated = True
            self.key = f"KEY: {key}"
            self.key_status = "STATUS: License Key Active"
            self.button_state = "normal"
            self.license_view()
    
    def open_link(event, link):
        import webbrowser
        webbrowser.open(link)

    def file_upload(self):
        filename = filedialog.askopenfilename()
        if filename:
            default_filename = "generator.csv"
            self.data = self.read_csv_file(filename)
            self.write_csv_file(default_filename, self.data)
        
        self.create_accounts_view()
    
    def handle_accounts(self):
        data = self.read_csv_file(self.file)
        self.filtered_data = [row for row in data if row[-1] == "Status"]
        for data in self.filtered_data:
            logging.debug(f'Handling: {data[0]}')
            self.progress_row += 1
        
    
    def read_csv_file(self, filename):
        # Read the data from the CSV file and return it
        data = []
        with open(filename, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        return data

    def write_csv_file(self, filename, data):
        # Add the "Status" column to the data
        data_with_status = [row + ["Status"] for row in data]
        
        # Write the data with the "Status" column to the CSV file
        with open(filename, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data_with_status)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()