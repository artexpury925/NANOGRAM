# mega_storage.py
from mega import Mega
import os
from flask import current_app

class MegaStorage:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MegaStorage, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self):
        if self.initialized:
            return

        mega = Mega()
        email = current_app.config['MEGA_EMAIL']
        password = current_app.config['MEGA_PASSWORD']

        try:
            self.m = mega.login(email, password)
            # Create/lookup Nanogram folder
            folder_node = self.m.find('Nanogram')
            if folder_node is None:
                folder_node = self.m.create_folder('Nanogram')
            self.nanogram_folder = folder_node
            self.initialized = True
            print("MEGA connected successfully – Arnold's storage ready!")
        except Exception as e:
            print(f"MEGA login failed: {e}")
            raise

    def upload_file(self, file_path, filename=None):
        if filename is None:
            filename = os.path.basename(file_path)
        file = self.m.upload(file_path, self.nanogram_folder[0])
        link = self.m.get_upload_link(file)
        return link  # public link anyone can view

    def delete_file(self, file_handle):
        self.m.delete(file_handle)