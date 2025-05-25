import subprocess
from AppKit import NSWorkspace

def open_application(application_name):
    if application_name and application_name.strip():
        try:
            # subprocess.Popen(application_name)
            NSWorkspace.sharedWorkspace().launchApplication_(application_name)
        except FileNotFoundError:
            print(f"Application '{application_name}' not found. Make sure it's in your PATH.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid application name.")

open_application("Sublime Text")
#open_application("notepad")
