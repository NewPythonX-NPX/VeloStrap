# =================================================================
# COPYRIGHT (C) 2026 NEWPYTHONX STUDIOS.
# ALL RIGHTS RESERVED. 
# FOUNDER: @horimiya_lover8053 (Discord)
# THIS CODE IS PROTECTED UNDER THE NPX LICENSE.
# REMOVING THIS HEADER IS A VIOLATION OF THE EULA AGREEMENT.
#
# THIS PROJECT WAS CREATED WITH THE HELP OF AI USAGE, AI'S LISTED IN README.
# =================================================================

import requests
import os
import time
import random
import asyncio
import sys
import webbrowser
import customtkinter as ctk
import subprocess
import json
import threading
import shutil
import re
import traceback
from PIL import Image
from pypresence import Presence
import ctypes
import datetime
import socket
from difflib import get_close_matches
from tkinter import messagebox, filedialog

# ==========================================
# SETTINGS
# ==========================================

# DO NOT CHANGE
APP_VERSION = "Random String" 

# DO NOT CHANGE
DEBUG_TEST = False # Self-explaintory if you read code, else this just skips update checkes and give your extra info.

APP_IDS = [
    "NewIDSWillBeHereButIwontDisplayHere"
    "VeloStrapIsNew_26thMarch"
]

APP_NAME = "VeloStrap" 
VersionDetectionURL = "https://raw.githubusercontent.com/NewPythonX-NPX/version-detection/refs/heads/main/ExtraAppIDsForVeloStrap?v1"

# OTHER STUFF

DISCORD_CLIENT_ID = "Scraped" 
ROBLOX_MUTEX_NAME = "ROBLOX_singletonEvent"
ROBLOX_LIVE_VERSION_API = "https://clientsettings.roblox.com/v2/client-version/WindowsPlayer/channel/live"
DEFAULT_RENDERING = "DX11 (Standard)"
INSTALL_WAIT_SECONDS = 180
DOWNLOAD_CHUNK_SIZE = 1024 * 1024

RENDERING_OPTIONS = [
    "DX11 (Standard)",
    "OpenGL (Recommended for Older Hardware)",
    "Vulkan (Best for Modern FPS)"
]
TEXTURE_QUALITY_OPTIONS = ["Automatic", "Low", "Medium", "High"]
TEXTURE_QUALITY_FLAG_VALUES = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}
MSAA_OPTIONS = ["Automatic", "2x", "4x"]
MSAA_FLAG_VALUES = {
    "2x": 2,
    "4x": 4
}
MESH_QUALITY_LABELS = ["Lowest", "Low", "Normal", "High", "Highest"]
# Roblox only allowlists the geometry LOD distance flags themselves. The non-default
# presets below are inferred from community testing; "Normal" intentionally writes
# nothing so Roblox keeps its own built-in defaults.
MESH_QUALITY_FLAG_PRESETS = {
    0: {
        "DFIntCSGLevelOfDetailSwitchingDistance": 12,
        "DFIntCSGLevelOfDetailSwitchingDistanceL12": 18,
        "DFIntCSGLevelOfDetailSwitchingDistanceL23": 28,
        "DFIntCSGLevelOfDetailSwitchingDistanceL34": 40
    },
    1: {
        "DFIntCSGLevelOfDetailSwitchingDistance": 24,
        "DFIntCSGLevelOfDetailSwitchingDistanceL12": 36,
        "DFIntCSGLevelOfDetailSwitchingDistanceL23": 54,
        "DFIntCSGLevelOfDetailSwitchingDistanceL34": 78
    },
    2: {},
    3: {
        "DFIntCSGLevelOfDetailSwitchingDistance": 40,
        "DFIntCSGLevelOfDetailSwitchingDistanceL12": 60,
        "DFIntCSGLevelOfDetailSwitchingDistanceL23": 90,
        "DFIntCSGLevelOfDetailSwitchingDistanceL34": 130
    },
    4: {
        "DFIntCSGLevelOfDetailSwitchingDistance": 56,
        "DFIntCSGLevelOfDetailSwitchingDistanceL12": 84,
        "DFIntCSGLevelOfDetailSwitchingDistanceL23": 126,
        "DFIntCSGLevelOfDetailSwitchingDistanceL34": 182
    }
}
DEFAULT_TEXTURE_QUALITY_MODE = "Automatic"
DEFAULT_MSAA_MODE = "Automatic"
DEFAULT_MESH_QUALITY_LEVEL = 2
DEFAULT_GRAPHICS_QUALITY_OVERRIDE = 0
APPEARANCE_OPTIONS = ["Device", "Light", "Dark", "Midnight"]
CURSOR_KEYBOARD_MOUSE_FILES = {"ArrowCursor.png", "ArrowFarCursor.png"}
OFFLINE_MODE = False
SHIFTLOCK_CURSOR_FILE = "MouseLockedCursor.png"
MOUSE_CURSOR_PRESET_OPTIONS = ["Default", "Angular (2013)", "Cartoony (2006)"]
ROBLOX_UI_FONT_TARGET_FILES = (
    "BuilderSans-Regular.otf",
    "BuilderSans-Medium.otf",
    "BuilderSans-Bold.otf",
    "BuilderSans-ExtraBold.otf"
)
SUPPORTED_CUSTOM_FONT_EXTENSIONS = {".otf", ".ttf"}

DEFAULT_PROFILE_PRESETS = {
    "Potato Mode": {
        "Type": "PRESET-PROFILE",
        "Rendering Mode": "DX11 (Standard)",
        "discord_rpc": False,
        "MultiInstance": False,
        "Mouse Cursor Preset": "Default",
        "Emulate Old Character Sounds": False,
        "Use Old Avatar Editor Background": False
    },
    "Extra Mode": {
        "Type": "PRESET-PROFILE",
        "Rendering Mode": "DX11 (Standard)",
        "discord_rpc": True,
        "MultiInstance": True,
        "Mouse Cursor Preset": "Default",
        "Emulate Old Character Sounds": False,
        "Use Old Avatar Editor Background": False
    },
    "Cinematic Mode": {
        "Type": "PRESET-PROFILE",
        "Rendering Mode": "DX11 (Standard)",
        "discord_rpc": True,
        "MultiInstance": True,
        "Mouse Cursor Preset": "Default",
        "Emulate Old Character Sounds": False,
        "Use Old Avatar Editor Background": False
    },
    "Mac-Bootcamp-Windows": {
        "Type": "PRESET-PROFILE",
        "Rendering Mode": "OpenGL (Recommended for Older Hardware)",
        "discord_rpc": False,
        "MultiInstance": False,
        "Mouse Cursor Preset": "Default",
        "Emulate Old Character Sounds": False,
        "Use Old Avatar Editor Background": False
    },
    "2016 Roblox": {
        "Type": "PRESET-PROFILE",
        "Rendering Mode": "DX11 (Standard)",
        "discord_rpc": False,
        "MultiInstance": False,
        "Mouse Cursor Preset": "Angular (2013)",
        "Emulate Old Character Sounds": True,
        "Use Old Avatar Editor Background": True
    },
    "----------------------------------------------------------------------": {
        "Type": "LINE"
    }
}

FASTFLAG_NAME_PATTERN = re.compile(r"^(?:FFlag|DFFlag|SFFlag|FInt|DFInt|FString|DFString|FLog|DFLog)[A-Za-z0-9]+$")
# Roblox's official local FastFlag allowlist, announced on September 29, 2025:
# https://devforum.roblox.com/t/allowlist-for-local-client-configuration-via-fast-flags/3966569
OFFICIAL_ALLOWLISTED_FASTFLAG_NAMES = {
    "DFIntCSGLevelOfDetailSwitchingDistance",
    "DFIntCSGLevelOfDetailSwitchingDistanceL12",
    "DFIntCSGLevelOfDetailSwitchingDistanceL23",
    "DFIntCSGLevelOfDetailSwitchingDistanceL34",
    "FFlagHandleAltEnterFullscreenManually",
    "DFFlagTextureQualityOverrideEnabled",
    "DFIntTextureQualityOverride",
    "FIntDebugForceMSAASamples",
    "DFFlagDisableDPIScale",
    "FFlagDebugSkyGray",
    "DFFlagDebugPauseVoxelizer",
    "DFIntDebugFRMQualityLevelOverride",
    "FIntFRMMaxGrassDistance",
    "FIntFRMMinGrassDistance",
    "FFlagDebugGraphicsPreferD3D11",
    "FFlagDebugGraphicsPreferVulkan",
    "FFlagDebugGraphicsPreferOpenGL",
    "FIntGrassMovementReducedMotionFactor"
}
FASTFLAG_NAME_ALIASES = {
    "FFlagHandleAltEnterFullscreen": "FFlagHandleAltEnterFullscreenManually"
}
DEPRECATED_FASTFLAG_SETTING_KEYS = (
    "FPS Boost",
    "Graphics Opt",
    "Server Region",
    "Use Server Region",
    "Join Own Region"
)


class FastFlagImportValidationError(RuntimeError):
    def __init__(self, message, valid_flags=None, removed_count=0):
        super().__init__(message)
        self.valid_flags = valid_flags or {}
        self.removed_count = removed_count

# ==========================================
# EXTRA FUNCTIONS
# ==========================================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)
        
def extra_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_app_directory():
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))
    
def log_error(error_message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"error_log_{timestamp}.txt"
    error_folder = "Error Log"
    
    if not os.path.exists(error_folder):
        os.makedirs(error_folder)
    
    log_path = os.path.join(error_folder, log_file)
    with open(log_path, "w") as f:
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Error Message: {error_message}\n")
    print(f"Error logged to {log_path}")

# ==========================================
# UPDATE CHECKER LOGIC
# ==========================================
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False

def run_update_check():
    global OFFLINE_MODE
    if DEBUG_TEST:
        print("------------------------------------------------")
        print(f">>> DEBUGGING: {APP_NAME} <<<")
        print(f">>> App Version: {APP_VERSION} <<<")
        print(f">>> Debug Mode: {DEBUG_TEST} <<<")
        print("------------------------------------------------")
        return
        
    print(f"--- Checking updates for {APP_NAME} ---")
    if not check_internet():
        print("- NO INTERNET CONNECTION. Skipping Update Check.")
        OFFLINE_MODE = True
        return

    try:
        cache_buster = f"{VersionDetectionURL}&t={int(time.time())}&nocache={random.randint(1, 9999)}"
        response = requests.get(cache_buster, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            latest_version = None
            
            for vid in APP_IDS:
                if vid in data:
                    val = str(data[vid]).strip()
                    
                    if val == "USE_GLOBAL":
                        latest_version = str(data.get("GLOBAL_LATEST")).strip()
                    else:
                        latest_version = val
                    
                    print(f"- Update Check Matched ID: {vid} (Version: {latest_version})")
                    break 

            if latest_version and latest_version != APP_VERSION:
                print(f"Update Found! Local: {APP_VERSION} | Cloud: {latest_version}")
                webbrowser.open("https://newpythonx.itch.io/velostrap-npx")
                pass
                sys.exit()
            else:
                print("Everything matches! Launching...")
                
    except Exception as e:
        print(f"Update Checker Failed: {e}")
        log_error(str(e))
        
# ==========================================
# LOADING SCREEN (CTK)
# ==========================================
def show_text_loading_sequence():
    splash = ctk.CTk()
    
    window_width = 1024
    window_height = 576
    splash.overrideredirect(True)
    splash.geometry(f"{window_width}x{window_height}")
    splash.attributes("-topmost", True)
    splash.eval('tk::PlaceWindow . center')

    script_dir = os.path.dirname(os.path.abspath(__file__))
    bg_path = resource_path(os.path.join("assets", "background.png"))
    
    try:
        bg_image_data = Image.open(bg_path) 
        bg_image = ctk.CTkImage(light_image=bg_image_data, 
                                dark_image=bg_image_data, 
                                size=(window_width, window_height))
    except FileNotFoundError:
        print(f"Error: Could not find background image at {bg_path}")
        bg_image = None

    bg_label = None
    if bg_image:
        bg_label = ctk.CTkLabel(
            splash, 
            image=bg_image, 
            text="Starting VeloStrap...", 
            font=("Segoe UI", 32, "bold"),
            text_color="#FFFFFF",
            compound="center"
        )
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    splash.update()

    # Run the update check in a thread so the splash can animate
    threading.Thread(target=run_update_check, daemon=True).start()

    sequence = [
        ("VeloStrap - Checking for Updates..", 1000),
        ("Connecting to Github..", 800),
        ("Comparing Local Version..", 800),
        ("Comparing Server Version..", 800),
        ("Completed Update-Checker", 500)
    ]

    def update_text(idx=0):
        if idx < len(sequence):
            text, delay_ms = sequence[idx]
            if bg_label:
                bg_label.configure(text=text)
            splash.update()
            splash.after(delay_ms, update_text, idx + 1)
        else:
            # All texts shown – close the splash after a brief pause
            splash.after(300, close_splash)

    def close_splash():
        splash.withdraw()
        try:
            for after_id in splash.tk.eval('after info').split():
                splash.after_cancel(after_id)
        except:
            pass
        try:
            splash.quit()
            splash.destroy()
        except:
            pass

    update_text()
    splash.mainloop()   # starts the Tk event loop, runs until splash is destroyed
    
# ==========================================
# UI COMPONENTS (CUSTOMTKINTER)
# ==========================================
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# ==========================================
# MAIN APPLICATION CLASS
# ==========================================
class LauncherStyleUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configure(fg_color=self.get_window_bg_color())

        self.app_dir = get_app_directory()
        self.app_dir = get_app_directory()
        self.velo_root = self.app_dir
        self.local_versions_path = os.path.join(self.app_dir, "Roblox Download (SAFE TO DELETE)")
        self.roblox_versions_path = os.path.expandvars(r"%LOCALAPPDATA%\Roblox\Versions")
        self.last_known_live_version = None
        self.activity_window = None
        self.activity_title_label = None
        self.activity_message_label = None
        self.activity_progress = None
        self.activity_progress_mode = None
        self.custom_flags_path = os.path.join(self.velo_root, "Custom-Flags")
        self.custom_fastflags_file = os.path.join(self.custom_flags_path, "CustomFFs.json")
        self.custom_fast_flags = {}
        self.fastflag_editor_window = None
        self.fastflag_json_box = None
        self.active_flags_textbox = None
        self.editor_active_flags_textbox = None
        self.custom_flags_list_frame = None
        self.custom_flags_count_label = None
        self.active_fastflags_signature = None
        self.custom_fastflags_signature = None
        
        # Rate Limiting
        self.action_timestamps = []
        self.rate_limited_until = 0

        # --- V0.1.1 SETTINGS / JSON DATA ---

        # --- V0.1.1 SETTINGS / JSON DATA ---
        self.npx_config_file = os.path.join(self.app_dir, "Config.json")
        self.npx_data = self.get_default_launcher_settings()
        self.load_launcher_data()
        self.load_custom_fast_flags()
        self.appearance_var = ctk.StringVar(value=self.npx_data.get("Appearance Mode", "Device"))
        self.mods_root = os.path.join(self.app_dir, "Mods")
        self.me_lo_root = os.path.join(self.app_dir, "Me_Lo")
        self.builtin_mods_root = os.path.join(self.app_dir, "IMPORTANT", "Bundled Mods")
        self.ensure_mods_structure()
        self.ensure_me_lo_structure()
        self.ensure_builtin_mod_presets()

        # --- V0.1.3 PROFILES JSON DATA ---
        self.profiles_file = self.resolve_profiles_file()
        self.profiles_data = {}
        self.load_profiles_data()

        self.title("VeloStrap - NewPythonX Studio")
        self.geometry("760x560")
        self.resizable(False, False)
        self.settings_window = None
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # === SIDEBAR ===
        self.sidebar = ctk.CTkFrame(self, width=160, corner_radius=0, fg_color=self.get_surface_bg_color())
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(
            self.sidebar,
            text="VELO\nSTRAP",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.get_primary_text_color()
        )
        self.logo_label.pack(padx=20, pady=(20, 10))
        
        self.home_btn = ctk.CTkButton(self.sidebar, text="Home", fg_color="transparent", text_color=self.get_primary_text_color(), command=self.show_home)
        self.home_btn.pack(fill="x", padx=20, pady=5)

        self.integrations_btn = ctk.CTkButton(self.sidebar, text="Mods", fg_color="transparent", text_color=self.get_primary_text_color(), command=self.show_integrations)
        self.integrations_btn.pack(fill="x", padx=20, pady=5)

        self.flags_btn = ctk.CTkButton(self.sidebar, text="FastFlags", fg_color="transparent", text_color=self.get_primary_text_color(), command=self.show_flags)
        self.flags_btn.pack(fill="x", padx=20, pady=5)

        self.profiles_btn = ctk.CTkButton(self.sidebar, text="Profiles", fg_color="transparent", text_color=self.get_primary_text_color(), command=self.show_profiles)
        self.profiles_btn.pack(fill="x", padx=20, pady=5)

        self.about_btn = ctk.CTkButton(self.sidebar, text="About", fg_color="transparent", text_color=self.get_primary_text_color(), command=self.show_about)
        self.about_btn.pack(fill="x", padx=20, pady=5)

        self.discord_btn = ctk.CTkButton(self.sidebar, text="Discord", fg_color="#5865F2", hover_color="#4752C4", command=self.open_discord)
        self.discord_btn.pack(fill="x", padx=20, pady=(40, 10))

        self.settings_btn = ctk.CTkButton(
            self.sidebar,
            text="Settings",
            **self.get_neutral_button_style(),
            command=self.open_settings_window
        )
        self.settings_btn.pack(fill="x", padx=20, pady=(10, 20))

        # === INITIALIZE RPC ===
        self.init_rpc()

        # === FRAMES ===
        self.home_frame = ctk.CTkScrollableFrame(self, corner_radius=10, fg_color=self.get_window_bg_color())
        self.setup_home_ui()
 
        self.integrations_frame = ctk.CTkScrollableFrame(self, corner_radius=10, fg_color=self.get_window_bg_color())
        self.setup_integrations_ui()

        self.flags_frame = ctk.CTkScrollableFrame(self, corner_radius=12, fg_color=self.get_window_bg_color())
        self.setup_flags_ui()

        self.profiles_frame = ctk.CTkScrollableFrame(self, corner_radius=10, fg_color=self.get_window_bg_color())
        self.setup_profiles_ui()

        self.about_frame = ctk.CTkScrollableFrame(self, corner_radius=10, fg_color=self.get_window_bg_color())
        self.setup_about_ui()

        self.show_home()

    # ==========================================
    # DATA NORMALIZATION
    # ==========================================
    def get_default_launcher_settings(self):
        # Keeping defaults in one place makes the reset button safe and easy to update later.
        return {
            "Running_App_Version": APP_VERSION,
            "Rendering Mode": DEFAULT_RENDERING,
            "Alt Enter Fullscreen": False,
            "Texture Quality Mode": DEFAULT_TEXTURE_QUALITY_MODE,
            "MSAA Mode": DEFAULT_MSAA_MODE,
            "Mesh Quality Level": DEFAULT_MESH_QUALITY_LEVEL,
            "Graphics Quality Override": DEFAULT_GRAPHICS_QUALITY_OVERRIDE,
            "discord_rpc": False,
            "Multi_Instance": False,
            "Appearance Mode": "Device",
            "Mouse Cursor Preset": "Default",
            "Emulate Old Character Sounds": False,
            "Use Old Avatar Editor Background": False,
            "Custom Roblox Font Source": "",
            "Custom FastFlags": {}
        }

    def get_current_theme(self):
        if hasattr(self, 'npx_data') and isinstance(self.npx_data, dict):
            return self.npx_data.get("Appearance Mode", "Device")
        return "Device"

    def get_window_bg_color(self):
        theme = self.get_current_theme()
        if theme == "Midnight": return "#050505"
        return ("#F9FAFB", "#0F172A")

    def get_surface_bg_color(self):
        theme = self.get_current_theme()
        if theme == "Midnight": return "#0A0A0A"
        return ("#FFFFFF", "#1E293B")

    def get_secondary_bg_color(self):
        theme = self.get_current_theme()
        if theme == "Midnight": return "#121212"
        return ("#F1F5F9", "#334155")

    def get_border_color(self):
        theme = self.get_current_theme()
        if theme == "Midnight": return "#1A1A1A"
        return ("#E2E8F0", "#475569")

    def get_primary_text_color(self):
        theme = self.get_current_theme()
        if theme == "Midnight": return "#E5E5E5"
        return ("#0F172A", "#F8FAFC")

    def get_muted_text_color(self):
        theme = self.get_current_theme()
        if theme == "Midnight": return "#A3A3A3"
        return ("#64748B", "#94A3B8")

    def get_content_wraplength(self):
        return 500
        
    def show_notification(self, message, color="#DC2626"):
        notif = ctk.CTkLabel(
            self, text=message, fg_color=color, text_color="white", 
            corner_radius=8, padx=15, pady=8, font=ctk.CTkFont(weight="bold")
        )
        notif.place(relx=0.5, rely=0.08, anchor="center")
        self.after(3500, notif.destroy)

    def check_rate_limit(self):
        now = time.time()
        if now < self.rate_limited_until:
            return False
        
        self.action_timestamps = [t for t in self.action_timestamps if now - t < 60]
        self.action_timestamps.append(now)
        
        if len(self.action_timestamps) > 88:
            self.rate_limited_until = now + 60
            self.show_notification("Rate limited for 1 minute(s)! (Too many actions)", color="#991B1B")
            return False
        return True

    def show_home(self):
        if OFFLINE_MODE and not hasattr(self, "offline_notified"):
            self.show_notification("No Internet Connection Detected.", color="#DC2626")
            self.offline_notified = True
            
        self.hide_all_frames()
        self.home_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.home_btn.configure(fg_color=self.get_secondary_bg_color())

    def get_dialog_wraplength(self):
        return 440

    def get_neutral_button_style(self):
        return {
            "fg_color": self.get_secondary_bg_color(),
            "hover_color": ("#E4E4E4", "#1A1A1A"),
            "text_color": self.get_primary_text_color(),
            "border_width": 1,
            "border_color": self.get_border_color()
        }

    def center_toplevel_window(self, window, width=420, height=220):
        try:
            self.update_idletasks()
            root_x = self.winfo_rootx()
            root_y = self.winfo_rooty()
            root_width = max(self.winfo_width(), width)
            root_height = max(self.winfo_height(), height)
            x = root_x + max((root_width - width) // 2, 0)
            y = root_y + max((root_height - height) // 2, 0)
        except Exception:
            x = (self.winfo_screenwidth() - width) // 2
            y = (self.winfo_screenheight() - height) // 2

        window.geometry(f"{width}x{height}+{x}+{y}")

    def ensure_activity_window(self):
        if self.activity_window and self.activity_window.winfo_exists():
            return self.activity_window

        self.activity_window = ctk.CTkToplevel(self)
        self.activity_window.title("VeloStrap")
        self.activity_window.resizable(False, False)
        self.activity_window.protocol("WM_DELETE_WINDOW", lambda: None)
        self.activity_window.transient(self)

        outer_frame = ctk.CTkFrame(
            self.activity_window,
            corner_radius=18,
            fg_color=self.get_surface_bg_color(),
            border_width=1,
            border_color=self.get_border_color()
        )
        outer_frame.pack(fill="both", expand=True, padx=16, pady=16)

        self.activity_title_label = ctk.CTkLabel(
            outer_frame,
            text="",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=self.get_primary_text_color()
        )
        self.activity_title_label.pack(pady=(24, 12), padx=24)

        self.activity_message_label = ctk.CTkLabel(
            outer_frame,
            text="",
            font=ctk.CTkFont(size=12),
            text_color=self.get_muted_text_color(),
            justify="center",
            wraplength=self.get_dialog_wraplength()
        )
        self.activity_message_label.pack(padx=24)

        self.activity_progress = ctk.CTkProgressBar(outer_frame, width=320, mode="indeterminate")
        self.activity_progress.pack(pady=(18, 0), padx=24)
        self.activity_progress_mode = "indeterminate"
        self.activity_progress.start()

        window = self.activity_window
        self.center_toplevel_window(window)
        window.lift()
        window.attributes("-topmost", True)

        def clear_topmost(target=window):
            if target.winfo_exists():
                target.attributes("-topmost", False)

        window.after(250, clear_topmost)
        return window

    def pump_ui(self):
        try:
            self.update_idletasks()
            self.update()
        except Exception:
            pass

    def update_activity_window(self, title, message, mode="indeterminate", progress=None):
        window = self.ensure_activity_window()
        self.activity_title_label.configure(text=title)
        self.activity_message_label.configure(text=message)

        if mode != self.activity_progress_mode:
            self.activity_progress.stop()
            self.activity_progress.configure(mode=mode)
            self.activity_progress_mode = mode

        if mode == "determinate":
            self.activity_progress.stop()
            self.activity_progress.set(max(0.0, min(progress if progress is not None else 0.0, 1.0)))
        else:
            self.activity_progress.start()

        self.center_toplevel_window(window)
        window.deiconify()
        window.lift()
        self.pump_ui()

    def close_activity_window(self):
        if self.activity_progress:
            try:
                self.activity_progress.stop()
            except Exception:
                pass

        if self.activity_window and self.activity_window.winfo_exists():
            try:
                self.activity_window.destroy()
            except Exception:
                pass

        self.activity_window = None
        self.activity_title_label = None
        self.activity_message_label = None
        self.activity_progress = None
        self.activity_progress_mode = None

    def get_option_menu_style(self):
        return {
            "fg_color": self.get_surface_bg_color(),
            "button_color": self.get_secondary_bg_color(),
            "button_hover_color": ("#E4E4E4", "#1A1A1A"),
            "dropdown_fg_color": self.get_surface_bg_color(),
            "dropdown_hover_color": ("#EAEAEA", "#161616"),
            "dropdown_text_color": self.get_primary_text_color(),
            "text_color": self.get_primary_text_color()
        }

    def resolve_profiles_file(self):
        for file_name in ["Profile_Saves.json", "Profiles_Save.json", "Profiles_Saves.json"]:
            file_path = os.path.join(self.app_dir, file_name)
            if os.path.exists(file_path):
                return file_path

        return os.path.join(self.app_dir, "Profile_Saves.json")

    def normalize_appearance_mode(self, mode_value):
        if mode_value in APPEARANCE_OPTIONS:
            return mode_value

        if isinstance(mode_value, str):
            cleaned_value = mode_value.strip()
            if cleaned_value.lower() == "system":
                return "Device"

            for option in APPEARANCE_OPTIONS:
                if option.lower() == cleaned_value.lower():
                    return option

        return "Device"

    def normalize_mouse_cursor_preset(self, preset_value):
        if preset_value in MOUSE_CURSOR_PRESET_OPTIONS:
            return preset_value

        if isinstance(preset_value, str):
            cleaned_value = preset_value.strip()
            for option in MOUSE_CURSOR_PRESET_OPTIONS:
                if option.lower() == cleaned_value.lower():
                    return option

        return "Default"

    def coerce_bounded_int(self, raw_value, default_value, minimum, maximum):
        try:
            coerced_value = int(round(float(raw_value)))
        except (TypeError, ValueError):
            return default_value

        return max(minimum, min(maximum, coerced_value))

    def normalize_texture_quality_mode(self, mode_value):
        if mode_value in TEXTURE_QUALITY_OPTIONS:
            return mode_value

        if isinstance(mode_value, str):
            cleaned_value = mode_value.strip()
            for option in TEXTURE_QUALITY_OPTIONS:
                if option.lower() == cleaned_value.lower():
                    return option
            if cleaned_value == "1":
                return "Low"
            if cleaned_value == "2":
                return "Medium"
            if cleaned_value == "3":
                return "High"

        numeric_value = self.coerce_bounded_int(mode_value, 0, 0, 3)
        if numeric_value == 1:
            return "Low"
        if numeric_value == 2:
            return "Medium"
        if numeric_value >= 3:
            return "High"

        return DEFAULT_TEXTURE_QUALITY_MODE

    def normalize_msaa_mode(self, mode_value):
        if mode_value in MSAA_OPTIONS:
            return mode_value

        if isinstance(mode_value, str):
            cleaned_value = mode_value.strip()
            for option in MSAA_OPTIONS:
                if option.lower() == cleaned_value.lower():
                    return option

        numeric_value = self.coerce_bounded_int(mode_value, 0, 0, 4)
        if numeric_value == 2:
            return "2x"
        if numeric_value >= 4:
            return "4x"

        return DEFAULT_MSAA_MODE

    def normalize_mesh_quality_level(self, level_value):
        return self.coerce_bounded_int(level_value, DEFAULT_MESH_QUALITY_LEVEL, 0, len(MESH_QUALITY_LABELS) - 1)

    def normalize_graphics_quality_override(self, level_value):
        return self.coerce_bounded_int(level_value, DEFAULT_GRAPHICS_QUALITY_OVERRIDE, 0, 10)

    def refresh_mesh_quality_label(self, level_value=None):
        if not hasattr(self, "mesh_quality_value_label"):
            return

        mesh_level = self.normalize_mesh_quality_level(
            self.mesh_quality_slider.get() if level_value is None and hasattr(self, "mesh_quality_slider") else level_value
        )
        label = MESH_QUALITY_LABELS[mesh_level]
        if mesh_level == DEFAULT_MESH_QUALITY_LEVEL:
            label += " (Roblox default)"
        self.mesh_quality_value_label.configure(text=f"Mesh Quality: {label}")

    def refresh_graphics_quality_label(self, level_value=None):
        if not hasattr(self, "graphics_quality_value_label"):
            return

        quality_level = self.normalize_graphics_quality_override(
            self.graphics_quality_slider.get() if level_value is None and hasattr(self, "graphics_quality_slider") else level_value
        )
        if quality_level == 0:
            label = "Automatic"
        else:
            label = f"Forced Level {quality_level}"
        self.graphics_quality_value_label.configure(text=f"Graphics Quality Override: {label}")

    def handle_mesh_quality_slider_change(self, value):
        self.refresh_mesh_quality_label(value)
        self.handle_fastflag_control_change()

    def handle_graphics_quality_slider_change(self, value):
        self.refresh_graphics_quality_label(value)
        self.handle_fastflag_control_change()

    def apply_saved_appearance_mode(self, mode_value=None):
        appearance_mode = self.normalize_appearance_mode(
            self.npx_data.get("Appearance Mode") if mode_value is None else mode_value
        )
        if mode_value is None:
            self.npx_data["Appearance Mode"] = appearance_mode
            
        # Map custom modes to CustomTkinter's supported internal modes to prevent crashes
        if appearance_mode == "Device":
            ctk_mode = "System"
        elif appearance_mode == "Midnight":
            ctk_mode = "Dark"
        else:
            ctk_mode = appearance_mode
            
        ctk.set_appearance_mode(ctk_mode)

    def sync_launcher_controls_to_data(self):
        # Reset and profile actions reuse this so the UI always matches the saved data.
        if hasattr(self, "ren_var"):
            self.ren_var.set(self.npx_data.get("Rendering Mode", DEFAULT_RENDERING))
        if hasattr(self, "alt_enter_fullscreen_switch"):
            if self.npx_data.get("Alt Enter Fullscreen", False):
                self.alt_enter_fullscreen_switch.select()
            else:
                self.alt_enter_fullscreen_switch.deselect()
        if hasattr(self, "texture_quality_var"):
            self.texture_quality_var.set(self.npx_data.get("Texture Quality Mode", DEFAULT_TEXTURE_QUALITY_MODE))
        if hasattr(self, "msaa_var"):
            self.msaa_var.set(self.npx_data.get("MSAA Mode", DEFAULT_MSAA_MODE))
        if hasattr(self, "mesh_quality_slider"):
            self.mesh_quality_slider.set(self.npx_data.get("Mesh Quality Level", DEFAULT_MESH_QUALITY_LEVEL))
            self.refresh_mesh_quality_label()
        if hasattr(self, "graphics_quality_slider"):
            self.graphics_quality_slider.set(self.npx_data.get("Graphics Quality Override", DEFAULT_GRAPHICS_QUALITY_OVERRIDE))
            self.refresh_graphics_quality_label()
        if hasattr(self, "appearance_var"):
            self.appearance_var.set(self.npx_data.get("Appearance Mode", "Device"))
        if hasattr(self, "mouse_cursor_preset_var"):
            self.mouse_cursor_preset_var.set(self.npx_data.get("Mouse Cursor Preset", "Default"))

        if hasattr(self, "discord_switch"):
            if self.npx_data.get("discord_rpc", False):
                self.discord_switch.select()
            else:
                self.discord_switch.deselect()

        if hasattr(self, "multi_switch"):
            if self.npx_data.get("Multi_Instance", False):
                self.multi_switch.select()
            else:
                self.multi_switch.deselect()

        if hasattr(self, "old_character_sounds_switch"):
            if self.npx_data.get("Emulate Old Character Sounds", False):
                self.old_character_sounds_switch.select()
            else:
                self.old_character_sounds_switch.deselect()

        if hasattr(self, "old_avatar_background_switch"):
            if self.npx_data.get("Use Old Avatar Editor Background", False):
                self.old_avatar_background_switch.select()
            else:
                self.old_avatar_background_switch.deselect()

        self.refresh_custom_roblox_font_status()

        if hasattr(self, "profile_old_character_sounds_switch"):
            if self.npx_data.get("Emulate Old Character Sounds", False):
                self.profile_old_character_sounds_switch.select()
            else:
                self.profile_old_character_sounds_switch.deselect()

        if hasattr(self, "profile_old_avatar_background_switch"):
            if self.npx_data.get("Use Old Avatar Editor Background", False):
                self.profile_old_avatar_background_switch.select()
            else:
                self.profile_old_avatar_background_switch.deselect()

        self.refresh_fastflag_views(use_current_ui=True)
        self.refresh_custom_fastflag_list()

    def normalize_launcher_settings(self):
        self.npx_data["Running_App_Version"] = APP_VERSION
        self.npx_data["Rendering Mode"] = self.npx_data.get("Rendering Mode", self.npx_data.get("Rendering Modern", DEFAULT_RENDERING))
        self.npx_data["Alt Enter Fullscreen"] = bool(self.npx_data.get("Alt Enter Fullscreen", False))
        self.npx_data["Texture Quality Mode"] = self.normalize_texture_quality_mode(
            self.npx_data.get("Texture Quality Mode", DEFAULT_TEXTURE_QUALITY_MODE)
        )
        self.npx_data["MSAA Mode"] = self.normalize_msaa_mode(
            self.npx_data.get("MSAA Mode", DEFAULT_MSAA_MODE)
        )
        self.npx_data["Mesh Quality Level"] = self.normalize_mesh_quality_level(
            self.npx_data.get("Mesh Quality Level", DEFAULT_MESH_QUALITY_LEVEL)
        )
        self.npx_data["Graphics Quality Override"] = self.normalize_graphics_quality_override(
            self.npx_data.get("Graphics Quality Override", DEFAULT_GRAPHICS_QUALITY_OVERRIDE)
        )
        self.npx_data["discord_rpc"] = bool(self.npx_data.get("discord_rpc", False))
        self.npx_data["Multi_Instance"] = bool(self.npx_data.get("Multi_Instance", False))
        self.npx_data["Appearance Mode"] = self.normalize_appearance_mode(self.npx_data.get("Appearance Mode"))
        self.npx_data["Mouse Cursor Preset"] = self.normalize_mouse_cursor_preset(self.npx_data.get("Mouse Cursor Preset"))
        self.npx_data["Emulate Old Character Sounds"] = bool(self.npx_data.get("Emulate Old Character Sounds", False))
        self.npx_data["Use Old Avatar Editor Background"] = bool(self.npx_data.get("Use Old Avatar Editor Background", False))
        font_source = self.npx_data.get("Custom Roblox Font Source", "")
        self.npx_data["Custom Roblox Font Source"] = font_source.strip() if isinstance(font_source, str) else ""
        custom_fastflags = self.npx_data.get("Custom FastFlags", {})
        self.npx_data["Custom FastFlags"] = dict(custom_fastflags) if isinstance(custom_fastflags, dict) else {}

        for stale_key in DEPRECATED_FASTFLAG_SETTING_KEYS:
            self.npx_data.pop(stale_key, None)

        if self.npx_data["Rendering Mode"] not in RENDERING_OPTIONS:
            self.npx_data["Rendering Mode"] = DEFAULT_RENDERING

    def normalize_profile_settings(self, settings):
        profile_settings = dict(settings)
        profile_settings["Rendering Mode"] = profile_settings.get("Rendering Mode", DEFAULT_RENDERING)
        profile_settings["discord_rpc"] = bool(profile_settings.get("discord_rpc", False))
        profile_settings["MultiInstance"] = bool(profile_settings.get("MultiInstance", profile_settings.get("Multi_Instance", False)))
        profile_settings["Mouse Cursor Preset"] = self.normalize_mouse_cursor_preset(profile_settings.get("Mouse Cursor Preset"))
        profile_settings["Emulate Old Character Sounds"] = bool(profile_settings.get("Emulate Old Character Sounds", False))
        profile_settings["Use Old Avatar Editor Background"] = bool(profile_settings.get("Use Old Avatar Editor Background", False))

        for stale_key in DEPRECATED_FASTFLAG_SETTING_KEYS:
            profile_settings.pop(stale_key, None)

        if profile_settings["Rendering Mode"] not in RENDERING_OPTIONS:
            profile_settings["Rendering Mode"] = DEFAULT_RENDERING

        return profile_settings

    # ==========================================
    # V0.1.4 DISCORD RPC LOGIC
    # ==========================================
    def init_rpc(self):
        self.rpc = None
        if self.npx_data.get("discord_rpc", True):
            self.start_rpc()

    def start_rpc(self):
        if self.rpc is None:
            try:
                self.rpc = Presence(DISCORD_CLIENT_ID)
                self.rpc.connect()
                self.rpc.update(state="In menus", details=f"VeloStrap {APP_VERSION}", start=int(time.time()))
                print("- SUCCESS: Discord RPC Connected.")
            except Exception as e:
                print(f"- RPC Error: {e}")
                self.rpc = None

    def stop_rpc(self):
        if self.rpc:
            try:
                self.rpc.close()
                self.rpc = None
                print("- SUCCESS: Discord RPC Disconnected.")
            except Exception as e:
                print(f"- RPC Disconnect Error: {e}")

    def restore_idle_rpc(self):
        if self.rpc:
            try:
                self.rpc.update(state="In VeloStrap", details=f"VeloStrap {APP_VERSION}", start=int(time.time()))
            except Exception:
                pass

    def toggle_rpc(self):
        self.save_launcher_data()
        if self.discord_switch.get():
            self.start_rpc()
        else:
            self.stop_rpc()

    # ==========================================
    # DATA SAVING & LOADING
    # ==========================================
    def load_launcher_data(self):
        if os.path.exists(self.npx_config_file):
            try:
                with open(self.npx_config_file, "r", encoding="utf-8") as f:
                    saved_data = json.load(f)
                    self.npx_data.update(saved_data)
                print("- Config.json Memory loaded.")
            except Exception as e:
                print(f"- Could not read memory box: {e}")

        self.normalize_launcher_settings()
        self.apply_saved_appearance_mode()

    def save_launcher_data(self):
        if hasattr(self, "ren_var"):
            self.npx_data["Rendering Mode"] = self.ren_var.get()
        if hasattr(self, "alt_enter_fullscreen_switch"):
            self.npx_data["Alt Enter Fullscreen"] = bool(self.alt_enter_fullscreen_switch.get())
        if hasattr(self, "texture_quality_var"):
            self.npx_data["Texture Quality Mode"] = self.normalize_texture_quality_mode(self.texture_quality_var.get())
        if hasattr(self, "msaa_var"):
            self.npx_data["MSAA Mode"] = self.normalize_msaa_mode(self.msaa_var.get())
        if hasattr(self, "mesh_quality_slider"):
            self.npx_data["Mesh Quality Level"] = self.normalize_mesh_quality_level(self.mesh_quality_slider.get())
        if hasattr(self, "graphics_quality_slider"):
            self.npx_data["Graphics Quality Override"] = self.normalize_graphics_quality_override(self.graphics_quality_slider.get())
        if hasattr(self, "discord_switch"):
            self.npx_data["discord_rpc"] = bool(self.discord_switch.get())
        if hasattr(self, "multi_switch"):
            self.npx_data["Multi_Instance"] = bool(self.multi_switch.get())
        if hasattr(self, "appearance_var"):
            self.npx_data["Appearance Mode"] = self.normalize_appearance_mode(self.appearance_var.get())
        if hasattr(self, "mouse_cursor_preset_var"):
            self.npx_data["Mouse Cursor Preset"] = self.normalize_mouse_cursor_preset(self.mouse_cursor_preset_var.get())
        if hasattr(self, "old_character_sounds_switch"):
            self.npx_data["Emulate Old Character Sounds"] = bool(self.old_character_sounds_switch.get())
        if hasattr(self, "old_avatar_background_switch"):
            self.npx_data["Use Old Avatar Editor Background"] = bool(self.old_avatar_background_switch.get())
        self.npx_data["Custom FastFlags"] = dict(self.custom_fast_flags)

        for stale_key in DEPRECATED_FASTFLAG_SETTING_KEYS:
            self.npx_data.pop(stale_key, None)

        self.normalize_launcher_settings()
        self.apply_saved_appearance_mode()
        target_dir = os.path.dirname(os.path.abspath(self.npx_config_file))
        if DEBUG_TEST: print(f"DEBUG: Saving to folder: {target_dir}")

        try:
            os.makedirs(target_dir, exist_ok=True)
            with open(self.npx_config_file, "w", encoding="utf-8") as f:
                json.dump(self.npx_data, f, indent=4)
            print("- SUCCESS: Config.json updated.")

            if hasattr(self, "save_btn"):
                self.save_btn.configure(text="Saved. Changes apply on the next Roblox launch.", fg_color="green")
                self.after(2000, lambda: self.save_btn.configure(text="Save FastFlags", fg_color="#3B8ED0"))
        except Exception as e:
            print(f"- BUG: {e}")
            messagebox.showerror("Save Error:", f"Windows blocked the save!\nError: {e}")

    def get_profile_type(self, profile_settings):
        return str(profile_settings.get("Type", "CUSTOM-PROFILE")).upper()

    def is_separator_profile(self, profile_settings):
        return self.get_profile_type(profile_settings) == "LINE"

    def is_preset_profile(self, profile_settings):
        return self.get_profile_type(profile_settings) == "PRESET-PROFILE"

    def get_default_profiles_data(self):
        default_profiles = {}
        for profile_name, profile_settings in DEFAULT_PROFILE_PRESETS.items():
            default_profiles[profile_name] = self.normalize_profile_settings(profile_settings)
            default_profiles[profile_name]["Type"] = profile_settings.get("Type", "CUSTOM-PROFILE")
        return default_profiles

    def ensure_default_profiles(self):
        default_profiles = self.get_default_profiles_data()

        for profile_name, default_settings in default_profiles.items():
            existing_settings = self.profiles_data.get(profile_name, {})
            merged_settings = dict(default_settings)

            if isinstance(existing_settings, dict):
                for key, value in existing_settings.items():
                    if key != "Type":
                        merged_settings[key] = value

            normalized_settings = self.normalize_profile_settings(merged_settings)
            normalized_settings["Type"] = default_settings["Type"]
            self.profiles_data[profile_name] = normalized_settings

    def load_profiles_data(self):
        self.profiles_data = {}

        if os.path.exists(self.profiles_file):
            try:
                with open(self.profiles_file, "r", encoding="utf-8") as f:
                    raw_profiles = json.load(f)

                for profile_name, profile_settings in raw_profiles.items():
                    if isinstance(profile_settings, dict):
                        normalized_settings = self.normalize_profile_settings(profile_settings)
                        normalized_settings["Type"] = profile_settings.get("Type", "CUSTOM-PROFILE")
                        self.profiles_data[profile_name] = normalized_settings
            except Exception as e:
                print(f"- Could not read Profiles: {e}")

        self.ensure_default_profiles()
        self.save_profiles_data()

    def save_profiles_data(self):
        self.ensure_default_profiles()
        target_dir = os.path.dirname(os.path.abspath(self.profiles_file))
        try:
            os.makedirs(target_dir, exist_ok=True)
            with open(self.profiles_file, "w", encoding="utf-8") as f:
                json.dump(self.profiles_data, f, indent=4)
        except Exception as e:
            print(f"- Failed saving Profile_Saves.json: {e}")

    def handle_critical_fastflag_error(self, context_message, error=None, parent=None):
        if error is None:
            stack_trace = traceback.format_exc()
            if stack_trace.strip() == "NoneType: None":
                stack_trace = context_message
        else:
            stack_trace = "".join(traceback.format_exception(type(error), error, error.__traceback__))

        log_error(f"{context_message}\n\n{stack_trace}")

        try:
            messagebox.showerror(
                "Critical FastFlag Error",
                f"{context_message}\n\nVeloStrap will now close to prevent data corruption.",
                parent=parent or self
            )
        finally:
            try:
                self.destroy()
            finally:
                sys.exit(1)

    def get_fastflag_name_candidates(self):
        builtin_names = set()
        try:
            builtin_names = set(self.build_builtin_fast_flags(use_current_ui=False).keys())
        except Exception:
            builtin_names = set()

        return sorted(OFFICIAL_ALLOWLISTED_FASTFLAG_NAMES.union(builtin_names, set(self.custom_fast_flags.keys())))

    def suggest_fastflag_name(self, fastflag_name):
        matches = get_close_matches(fastflag_name, self.get_fastflag_name_candidates(), n=1, cutoff=0.82)
        return matches[0] if matches else None

    def normalize_fastflag_key(self, raw_key, parent=None, ask_for_suggestion=True):
        if not isinstance(raw_key, str) or not raw_key.strip():
            raise ValueError("A FastFlag entry is missing a key.")

        cleaned_key = FASTFLAG_NAME_ALIASES.get(raw_key.strip(), raw_key.strip())
        suggested_name = self.suggest_fastflag_name(cleaned_key)
        if ask_for_suggestion and suggested_name and suggested_name != cleaned_key:
            use_suggestion = messagebox.askyesno(
                "FastFlag Suggestion",
                f"Do you mean {suggested_name}?",
                parent=parent or self
            )
            if use_suggestion:
                cleaned_key = suggested_name

        if not FASTFLAG_NAME_PATTERN.match(cleaned_key):
            raise ValueError(f"'{cleaned_key}' is not a valid Roblox FastFlag name.")

        if cleaned_key not in OFFICIAL_ALLOWLISTED_FASTFLAG_NAMES:
            raise ValueError(f"'{cleaned_key}' is not on Roblox's current official FastFlag allowlist.")

        return cleaned_key

    def validate_fastflag_mapping(self, raw_flags, ask_for_suggestion=False, parent=None):
        validated_flags = {}
        removed_messages = []

        for raw_key, raw_value in raw_flags.items():
            try:
                normalized_key = self.normalize_fastflag_key(
                    raw_key,
                    parent=parent,
                    ask_for_suggestion=ask_for_suggestion
                )
                validated_flags[normalized_key] = self.normalize_fastflag_value(raw_value)
            except Exception as exc:
                removed_messages.append(str(exc))

        return validated_flags, removed_messages

    def normalize_fastflag_value(self, raw_value):
        if isinstance(raw_value, bool):
            return raw_value
        if isinstance(raw_value, int) and not isinstance(raw_value, bool):
            return raw_value
        if isinstance(raw_value, float):
            return raw_value
        if isinstance(raw_value, str):
            return raw_value

        raise ValueError("A FastFlag entry is missing a usable value.")

    def auto_fix_fastflag_json_text(self, raw_text):
        if not isinstance(raw_text, str) or not raw_text.strip():
            raise ValueError("The FastFlag JSON input is empty.")

        text = raw_text.replace("\ufeff", "").replace("\r\n", "\n").replace("\r", "\n").strip()
        text = re.sub(r"(?m)^\s*//.*$", "", text)
        text = re.sub(r"(?m)^\s*#.*$", "", text)
        text = re.sub(
            r"'([^'\\]*(?:\\.[^'\\]*)*)'",
            lambda match: '"' + match.group(1).replace('"', '\\"') + '"',
            text
        )
        text = re.sub(r"(?m)^(\s*)([A-Za-z_][A-Za-z0-9_]*)\s*=", r'\1"\2": ', text)
        text = re.sub(r"(?m)^(\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:", r'\1"\2": ', text)
        text = re.sub(r'([{\[,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*=', r'\1"\2": ', text)
        text = re.sub(r'([{\[,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:', r'\1"\2": ', text)

        if not re.match(r"^\s*[\{\[]", text):
            text = "{\n" + text + "\n}"

        stripped_text = text.lstrip()
        if stripped_text.startswith("{") and text.rstrip().endswith("}"):
            open_brace_index = text.find("{")
            close_brace_index = text.rfind("}")
            body = text[open_brace_index + 1:close_brace_index]
            cleaned_lines = []
            for line in body.splitlines():
                cleaned_line = re.sub(r",\s*$", "", line.strip())
                if cleaned_line:
                    cleaned_lines.append(cleaned_line)
            text = "{\n" + ",\n".join(cleaned_lines) + "\n}"

        text = re.sub(r",(\s*[}\]])", r"\1", text)
        return text

    def parse_fastflag_payload(self, raw_text, source_label="FastFlag JSON", parent=None):
        fixed_text = self.auto_fix_fastflag_json_text(raw_text)

        try:
            payload = json.loads(fixed_text)
        except Exception as exc:
            raise RuntimeError(f"{source_label} could not be parsed after auto-fixing the syntax.") from exc

        normalized_flags = {}
        removed_count = 0
        issues = []

        def store_flag(raw_key, raw_value):
            nonlocal removed_count
            try:
                normalized_key = self.normalize_fastflag_key(raw_key, parent=parent)
                normalized_flags[normalized_key] = self.normalize_fastflag_value(raw_value)
            except Exception as exc:
                removed_count += 1
                issues.append(str(exc))

        if isinstance(payload, dict):
            for raw_key, raw_value in payload.items():
                store_flag(raw_key, raw_value)
        elif isinstance(payload, list):
            for entry in payload:
                if not isinstance(entry, dict):
                    removed_count += 1
                    issues.append("A FastFlag list entry must be a JSON object.")
                    continue

                if "key" in entry and "value" in entry:
                    store_flag(entry.get("key"), entry.get("value"))
                    continue

                if len(entry) == 1:
                    raw_key, raw_value = next(iter(entry.items()))
                    store_flag(raw_key, raw_value)
                    continue

                removed_count += 1
                issues.append("A FastFlag entry is missing a key or value.")
        else:
            raise ValueError(f"{source_label} must be a JSON object or an array of FastFlags.")

        if not normalized_flags and removed_count == 0:
            raise ValueError(f"{source_label} did not contain any FastFlags to save.")

        if issues:
            raise FastFlagImportValidationError(
                "\n".join(issues),
                valid_flags=normalized_flags,
                removed_count=removed_count
            )

        return normalized_flags, fixed_text

    def load_custom_fast_flags(self):
        self.custom_fast_flags = {}
        fallback_flags = self.npx_data.get("Custom FastFlags", {})
        self.npx_data["Custom FastFlags"] = {}

        try:
            should_persist_clean_copy = False
            if not os.path.exists(self.custom_fastflags_file):
                if isinstance(fallback_flags, dict) and fallback_flags:
                    validated_flags, removed_messages = self.validate_fastflag_mapping(fallback_flags, ask_for_suggestion=False)
                    for removed_message in removed_messages:
                        print(f"- Removed unsupported custom FastFlag from launcher settings: {removed_message}")
                    self.persist_custom_fast_flags(validated_flags, sync_launcher=False, refresh_views=False)
                return

            with open(self.custom_fastflags_file, "r", encoding="utf-8") as file_handle:
                stored_flags = json.load(file_handle)

            if not isinstance(stored_flags, dict):
                raise ValueError("CustomFFs.json must contain a JSON object.")

            validated_flags, removed_messages = self.validate_fastflag_mapping(stored_flags, ask_for_suggestion=False)
            if removed_messages:
                should_persist_clean_copy = True
                for removed_message in removed_messages:
                    print(f"- Removed unsupported custom FastFlag from CustomFFs.json: {removed_message}")

            self.custom_fast_flags = dict(sorted(validated_flags.items(), key=lambda item: item[0].lower()))
            self.npx_data["Custom FastFlags"] = dict(self.custom_fast_flags)
            if should_persist_clean_copy:
                self.persist_custom_fast_flags(self.custom_fast_flags, sync_launcher=False, refresh_views=False)
        except Exception as exc:
            self.handle_critical_fastflag_error(
                "CustomFFs.json could not be loaded safely.",
                exc
            )

    def persist_custom_fast_flags(self, flags, sync_launcher=True, refresh_views=True):
        normalized_flags = dict(sorted(dict(flags).items(), key=lambda item: item[0].lower()))
        target_dir = os.path.dirname(os.path.abspath(self.custom_fastflags_file))

        try:
            os.makedirs(target_dir, exist_ok=True)
            with open(self.custom_fastflags_file, "w", encoding="utf-8") as file_handle:
                json.dump(normalized_flags, file_handle, indent=4)
        except Exception as exc:
            self.handle_critical_fastflag_error(
                "CustomFFs.json could not be saved safely.",
                exc,
                parent=self.fastflag_editor_window if self.fastflag_editor_window and self.fastflag_editor_window.winfo_exists() else self
            )

        self.custom_fast_flags = normalized_flags
        self.npx_data["Custom FastFlags"] = dict(self.custom_fast_flags)

        if sync_launcher:
            self.save_launcher_data()
        if refresh_views:
            self.refresh_fastflag_views(use_current_ui=True)
            self.refresh_custom_fastflag_list()

    def merge_fastflags_with_existing(self, imported_flags, parent=None):
        current_flags = self.build_fast_flags(use_current_ui=True)
        conflicts = {
            key: {"existing": current_flags[key], "new": value}
            for key, value in imported_flags.items()
            if key in current_flags and current_flags[key] != value
        }

        overwrite_conflicts = True
        if conflicts:
            overwrite_conflicts = self.prompt_fastflag_overwrite(conflicts, parent=parent)

        merged_custom_flags = dict(self.custom_fast_flags)
        for key, value in imported_flags.items():
            if key in conflicts and not overwrite_conflicts:
                continue
            merged_custom_flags[key] = value

        return merged_custom_flags

    def format_fastflag_value(self, flag_value):
        return json.dumps(flag_value, ensure_ascii=False)

    def format_active_fastflags(self, flags):
        if not flags:
            return "No active FastFlags yet."

        return "\n".join(
            f"{flag_name} = {self.format_fastflag_value(flag_value)}"
            for flag_name, flag_value in sorted(flags.items(), key=lambda item: item[0].lower())
        )

    def refresh_fastflag_views(self, use_current_ui=True, force=False):
        try:
            active_flags = self.build_fast_flags(use_current_ui=use_current_ui)
        except Exception:
            active_flags = self.build_fast_flags(use_current_ui=False)

        signature = json.dumps(active_flags, sort_keys=True, default=str)
        if not force and signature == self.active_fastflags_signature:
            return False

        self.active_fastflags_signature = signature
        formatted_flags = self.format_active_fastflags(active_flags)

        if hasattr(self, "active_flags_count_label") and self.active_flags_count_label:
            self.active_flags_count_label.configure(text=f"Current Active FastFlags ({len(active_flags)})")
        if hasattr(self, "editor_active_flags_count_label") and self.editor_active_flags_count_label:
            self.editor_active_flags_count_label.configure(text=f"Current Active FastFlags ({len(active_flags)})")

        for textbox in [self.active_flags_textbox, self.editor_active_flags_textbox]:
            if textbox and textbox.winfo_exists():
                textbox.configure(state="normal")
                textbox.delete("1.0", "end")
                textbox.insert("1.0", formatted_flags)
                textbox.configure(state="disabled")

        return True

    def refresh_custom_fastflag_list(self, force=False):
        signature = json.dumps(self.custom_fast_flags, sort_keys=True, default=str)
        if not force and signature == self.custom_fastflags_signature:
            return False

        self.custom_fastflags_signature = signature

        if self.custom_flags_count_label and self.custom_flags_count_label.winfo_exists():
            self.custom_flags_count_label.configure(text=f"Saved Custom FastFlags ({len(self.custom_fast_flags)})")

        if not self.custom_flags_list_frame or not self.custom_flags_list_frame.winfo_exists():
            return True

        for widget in self.custom_flags_list_frame.winfo_children():
            widget.destroy()

        if not self.custom_fast_flags:
            ctk.CTkLabel(
                self.custom_flags_list_frame,
                text="No custom FastFlags saved yet.",
                text_color=self.get_muted_text_color(),
                wraplength=self.get_content_wraplength(),
                justify="center"
            ).pack(pady=10)
            return True

        for flag_name, flag_value in sorted(self.custom_fast_flags.items(), key=lambda item: item[0].lower()):
            row = ctk.CTkFrame(
                self.custom_flags_list_frame,
                corner_radius=8,
                fg_color=self.get_surface_bg_color(),
                border_width=1,
                border_color=self.get_border_color()
            )
            row.pack(fill="x", padx=4, pady=4)
            row.grid_columnconfigure(0, weight=1)

            ctk.CTkLabel(
                row,
                text=flag_name,
                font=ctk.CTkFont(size=13, weight="bold"),
                anchor="w",
                justify="left",
                wraplength=420,
                text_color=self.get_primary_text_color()
            ).grid(row=0, column=0, sticky="w", padx=(12, 8), pady=(8, 0))

            ctk.CTkLabel(
                row,
                text=self.format_fastflag_value(flag_value),
                anchor="w",
                justify="left",
                wraplength=420,
                text_color=self.get_muted_text_color()
            ).grid(row=1, column=0, sticky="w", padx=(12, 8), pady=(0, 8))

            ctk.CTkButton(
                row,
                text="Delete",
                width=70,
                fg_color="#D9534F",
                hover_color="#C9302C",
                command=lambda current_flag=flag_name: self.delete_custom_fastflag(current_flag)
            ).grid(row=0, column=1, rowspan=2, padx=(0, 10), pady=10)

        return True

    def open_discord(self):
        webbrowser.open("https://discord.gg/CxGzGWmyNz")

    def preview_appearance_mode(self, selected_mode):
        # Preview only changes the live look of the window until the user presses Save.
        self.apply_saved_appearance_mode(self.normalize_appearance_mode(selected_mode))

    def reset_installed_fast_flags(self):
        installed_folder = self.get_current_installed_roblox_folder()
        if not installed_folder:
            return False

        settings_file = os.path.join(installed_folder, "ClientSettings", "ClientAppSettings.json")
        if not os.path.exists(settings_file):
            return False

        try:
            os.remove(settings_file)
        except OSError:
            with open(settings_file, "w", encoding="utf-8") as file_handle:
                json.dump({}, file_handle, indent=4)

        print(f"- SUCCESS: Reset FastFlags to default at {settings_file}")
        return True

    def reset_everything_to_default(self):
        if not messagebox.askyesno(
            "Reset Everything",
            "Reset everything back to default?",
            parent=self.settings_window
        ):
            return

        deleted_items = []

        for profile_file_name in ["Profile_Saves.json", "Profiles_Save.json", "Profiles_Saves.json"]:
            profile_file_path = os.path.join(self.app_dir, profile_file_name)
            if os.path.exists(profile_file_path):
                os.remove(profile_file_path)
                deleted_items.append(profile_file_name)

        if os.path.exists(self.npx_config_file):
            os.remove(self.npx_config_file)
            deleted_items.append(os.path.basename(self.npx_config_file))

        if os.path.isdir(self.custom_flags_path):
            shutil.rmtree(self.custom_flags_path)
            deleted_items.append("Custom-Flags")

        self.custom_fast_flags = {}
        self.npx_data = self.get_default_launcher_settings()
        self.normalize_launcher_settings()
        self.apply_saved_appearance_mode()
        self.stop_rpc()
        self.profiles_data = self.get_default_profiles_data()
        self.sync_launcher_controls_to_data()
        self.refresh_profiles_list()
        self.refresh_fastflag_views(use_current_ui=True, force=True)
        self.refresh_custom_fastflag_list(force=True)
        fastflags_reset = self.reset_installed_fast_flags()

        if self.settings_window and self.settings_window.winfo_exists():
            self.settings_saved_appearance = self.npx_data.get("Appearance Mode", "Device")

        reset_message = "Launcher settings were reset to default."
        if fastflags_reset:
            reset_message += "\nInstalled Roblox FastFlags were cleared."
        else:
            reset_message += "\nNo installed Roblox FastFlags file was found to clear."

        if deleted_items:
            reset_message += "\nDeleted: " + ", ".join(deleted_items)
        else:
            reset_message += "\nNo launcher save files were present to delete."

        messagebox.showinfo("Defaults Restored", reset_message, parent=self.settings_window)

    def open_settings_window(self):
        if self.settings_window and self.settings_window.winfo_exists():
            self.settings_window.focus()
            return

        self.settings_saved_appearance = self.normalize_appearance_mode(self.npx_data.get("Appearance Mode", "Device"))
        self.appearance_var.set(self.settings_saved_appearance)

        self.settings_window = ctk.CTkToplevel(self)
        self.settings_window.title("VeloStrap Settings")
        self.settings_window.geometry("520x420")
        self.settings_window.resizable(False, False)
        self.settings_window.configure(fg_color=self.get_window_bg_color())
        self.settings_window.grab_set()

        def close_settings(revert_preview=True):
            # Closing without saving restores the theme the user had before opening settings.
            if revert_preview:
                self.appearance_var.set(self.settings_saved_appearance)
                self.apply_saved_appearance_mode(self.settings_saved_appearance)

            if self.settings_window and self.settings_window.winfo_exists():
                self.settings_window.destroy()
            self.settings_window = None

        self.settings_window.protocol("WM_DELETE_WINDOW", close_settings)

        container = ctk.CTkFrame(self.settings_window, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=20)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            container,
            text="Settings",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=self.get_primary_text_color()
        ).grid(row=0, column=0, sticky="w", pady=(0, 12))

        tabs = ctk.CTkTabview(container, segmented_button_selected_color="#2563EB", segmented_button_selected_hover_color="#1D4ED8")
        tabs.grid(row=1, column=0, sticky="nsew")

        appearance_tab = tabs.add("Appearance")
        general_tab = tabs.add("General Settings")

        ctk.CTkLabel(
            appearance_tab,
            text="Appearance Mode",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.get_primary_text_color()
        ).pack(anchor="w", padx=10, pady=(12, 6))

        appearance_menu = ctk.CTkOptionMenu(
            appearance_tab,
            variable=self.appearance_var,
            values=APPEARANCE_OPTIONS,
            width=260,
            command=self.preview_appearance_mode,
            **self.get_option_menu_style()
        )
        appearance_menu.pack(anchor="w", padx=10, pady=(0, 10))

        ctk.CTkLabel(
            general_tab,
            text="General Settings",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.get_primary_text_color()
        ).pack(anchor="w", padx=10, pady=(12, 10))

        ctk.CTkButton(
            general_tab,
            text="RESET EVERYTHING TO DEFAULT",
            fg_color="#B91C1C",
            hover_color="#991B1B",
            command=self.reset_everything_to_default
        ).pack(anchor="w", padx=10, pady=(0, 10))

        def save_settings():
            self.save_launcher_data()
            self.settings_saved_appearance = self.normalize_appearance_mode(self.appearance_var.get())
            close_settings(revert_preview=False)

        actions = ctk.CTkFrame(container, fg_color="transparent")
        actions.grid(row=2, column=0, sticky="ew", pady=(14, 0))

        ctk.CTkButton(
            actions,
            text="Cancel",
            **self.get_neutral_button_style(),
            command=close_settings
        ).pack(side="left")

        ctk.CTkButton(
            actions,
            text="Save Settings",
            command=save_settings
        ).pack(side="right")

    # ==========================================
    # MODS
    # ==========================================
    def ensure_mods_structure(self):
        os.makedirs(self.mods_root, exist_ok=True)
        os.makedirs(os.path.join(self.mods_root, "content", "textures", "Cursors", "KeyboardMouse"), exist_ok=True)
        os.makedirs(os.path.join(self.mods_root, "content", "fonts"), exist_ok=True)
        os.makedirs(os.path.join(self.mods_root, "content", "sounds"), exist_ok=True)
        os.makedirs(os.path.join(self.mods_root, "ExtraContent", "places"), exist_ok=True)
        os.makedirs(self.builtin_mods_root, exist_ok=True)

    def ensure_me_lo_structure(self):
        os.makedirs(os.path.join(self.me_lo_root, "Sound", "Old"), exist_ok=True)
        os.makedirs(os.path.join(self.me_lo_root, "Background", "Old"), exist_ok=True)
        os.makedirs(os.path.join(self.me_lo_root, "Cursor", "Angular_2013", "KeyboardMouse"), exist_ok=True)
        os.makedirs(os.path.join(self.me_lo_root, "Cursor", "Cartoony_2006", "KeyboardMouse"), exist_ok=True)

    def get_old_character_sounds_preset_root(self):
        return os.path.join(self.builtin_mods_root, "OldCharacterSounds")

    def get_old_avatar_background_preset_root(self):
        return os.path.join(self.builtin_mods_root, "OldAvatarEditorBackground")

    def get_default_ui_font_backup_root(self):
        return os.path.join(self.builtin_mods_root, "DefaultUIFontBackup", "content", "fonts")

    def get_custom_roblox_font_mod_root(self):
        return os.path.join(self.mods_root, "content", "fonts")

    def get_me_lo_sound_old_root(self):
        return os.path.join(self.me_lo_root, "Sound", "Old")

    def get_me_lo_background_old_root(self):
        return os.path.join(self.me_lo_root, "Background", "Old")

    def get_mouse_cursor_preset_root(self, preset_name):
        preset_folder_map = {
            "Angular (2013)": "Angular_2013",
            "2006 (Cartoony)": "Cartoony_2006"
        }
        folder_name = preset_folder_map.get(preset_name)
        if not folder_name:
            return None

        return os.path.join(self.me_lo_root, "Cursor", folder_name)

    def directory_contains_files(self, folder_path):
        for _, _, files in os.walk(folder_path):
            if files:
                return True
        return False

    def seed_old_character_sounds_preset(self, installed_folder):
        source_dir = os.path.join(installed_folder, "content", "sounds")
        target_dir = os.path.join(self.get_old_character_sounds_preset_root(), "content", "sounds")
        os.makedirs(target_dir, exist_ok=True)

        if self.directory_contains_files(target_dir):
            return

        if not os.path.isdir(source_dir):
            log_error("Could not seed old character sound preset because Roblox's content\\sounds folder was not found.")
            return

        # The preset starts as a snapshot of the local Roblox files so it's immediately usable.
        # If you later find a preferred legacy pack, replacing the files inside this preset folder is enough.
        for file_name in os.listdir(source_dir):
            source_file = os.path.join(source_dir, file_name)
            if os.path.isfile(source_file):
                shutil.copy2(source_file, os.path.join(target_dir, file_name))

    def seed_old_avatar_background_preset(self, installed_folder):
        source_file = os.path.join(installed_folder, "ExtraContent", "places", "Mobile.rbxl")
        target_dir = os.path.join(self.get_old_avatar_background_preset_root(), "ExtraContent", "places")
        target_file = os.path.join(target_dir, "Mobile.rbxl")
        os.makedirs(target_dir, exist_ok=True)

        if os.path.exists(target_file):
            return

        if not os.path.exists(source_file):
            log_error("Could not seed old avatar editor background preset because Roblox's ExtraContent\\places\\Mobile.rbxl file was not found.")
            return

        # This preset is also initialized from the local Roblox install so you can swap in a different Mobile.rbxl later.
        shutil.copy2(source_file, target_file)

    def seed_default_ui_font_backup(self, installed_folder):
        source_dir = os.path.join(installed_folder, "content", "fonts")
        target_dir = self.get_default_ui_font_backup_root()
        os.makedirs(target_dir, exist_ok=True)

        if not os.path.isdir(source_dir):
            log_error("Could not seed the default Roblox UI font backup because Roblox's content\\fonts folder was not found.")
            return

        missing_source_files = []
        for file_name in ROBLOX_UI_FONT_TARGET_FILES:
            source_file = os.path.join(source_dir, file_name)
            target_file = os.path.join(target_dir, file_name)
            if not os.path.exists(source_file):
                missing_source_files.append(file_name)
                continue
            if not os.path.exists(target_file):
                shutil.copy2(source_file, target_file)

        if missing_source_files:
            log_error(
                "Could not seed every default Roblox UI font file because these BuilderSans files were not found: "
                + ", ".join(missing_source_files)
            )

    def ensure_builtin_mod_presets(self, installed_folder=None):
        if installed_folder is None:
            installed_folder = self.get_current_installed_roblox_folder()

        if not installed_folder:
            return

        self.seed_old_character_sounds_preset(installed_folder)
        self.seed_old_avatar_background_preset(installed_folder)
        self.seed_default_ui_font_backup(installed_folder)
        self.seed_me_lo_presets()

    def seed_me_lo_presets(self):
        sound_target_root = self.get_me_lo_sound_old_root()
        background_target_root = self.get_me_lo_background_old_root()
        bundled_sound_root = os.path.join(self.get_old_character_sounds_preset_root(), "content", "sounds")
        bundled_background_file = os.path.join(self.get_old_avatar_background_preset_root(), "ExtraContent", "places", "Mobile.rbxl")

        if not self.directory_contains_files(sound_target_root) and os.path.isdir(bundled_sound_root):
            for file_name in os.listdir(bundled_sound_root):
                source_file = os.path.join(bundled_sound_root, file_name)
                if os.path.isfile(source_file):
                    shutil.copy2(source_file, os.path.join(sound_target_root, file_name))

        background_target_file = os.path.join(background_target_root, "Mobile.rbxl")
        if not os.path.exists(background_target_file) and os.path.exists(bundled_background_file):
            shutil.copy2(bundled_background_file, background_target_file)

    def handle_mod_setting_toggle(self):
        if not self.check_rate_limit(): return
        self.ensure_builtin_mod_presets()
        self.save_launcher_data()
        self.apply_mod_settings_if_available()

    def handle_mouse_cursor_preset_change(self, _=None):
        self.ensure_builtin_mod_presets()
        self.save_launcher_data()
        self.apply_mod_settings_if_available()

    def apply_mod_settings_if_available(self):
        installed_folder = self.get_current_installed_roblox_folder()
        if not installed_folder:
            return

        try:
            self.apply_selected_mods(installed_folder)
        except Exception as e:
            log_error(f"Could not apply mod settings immediately: {e}")

    def open_mods_folder(self):
        self.ensure_mods_structure()
        try:
            os.startfile(self.mods_root)
        except Exception as e:
            log_error(f"Could not open Mods folder: {e}")
            messagebox.showerror("Mods Folder", f"Could not open the Mods folder.\n{e}")

    def validate_custom_mod_file(self, relative_path):
        path_parts = relative_path.replace("/", os.sep).split(os.sep)
        lower_parts = [part.lower() for part in path_parts]

        if lower_parts[:2] == ["content", "textures"] and len(path_parts) == 3 and path_parts[-1] == SHIFTLOCK_CURSOR_FILE:
            return True

        if lower_parts[:4] == ["content", "textures", "cursors", "keyboardmouse"] and len(path_parts) == 5:
            file_name = path_parts[-1]
            if file_name not in CURSOR_KEYBOARD_MOUSE_FILES:
                log_error(
                    f"Skipped invalid cursor filename '{file_name}'. "
                    f"Valid files in KeyboardMouse are: {', '.join(sorted(CURSOR_KEYBOARD_MOUSE_FILES))}."
                )
                return False

        return True

    def is_cursor_mod_file(self, relative_path):
        path_parts = relative_path.replace("/", os.sep).split(os.sep)
        lower_parts = [part.lower() for part in path_parts]
        return (
            lower_parts[:2] == ["content", "textures"] and len(path_parts) == 3 and path_parts[-1] == SHIFTLOCK_CURSOR_FILE
        ) or (
            lower_parts[:4] == ["content", "textures", "cursors", "keyboardmouse"] and len(path_parts) == 5
        )

    def copy_mod_overlay(self, source_root, destination_root, validate_custom_files=False, skip_cursor_files=False):
        if not os.path.isdir(source_root):
            return

        for current_root, _, file_names in os.walk(source_root):
            for file_name in file_names:
                source_file = os.path.join(current_root, file_name)
                relative_path = os.path.relpath(source_file, source_root)

                if skip_cursor_files and self.is_cursor_mod_file(relative_path):
                    continue

                if validate_custom_files and not self.validate_custom_mod_file(relative_path):
                    continue

                target_file = os.path.join(destination_root, relative_path)
                os.makedirs(os.path.dirname(target_file), exist_ok=True)
                shutil.copy2(source_file, target_file)

    def apply_old_character_sounds_preset(self, installed_folder):
        me_lo_sound_root = self.get_me_lo_sound_old_root()
        target_root = os.path.join(installed_folder, "content", "sounds")
        os.makedirs(target_root, exist_ok=True)

        if self.directory_contains_files(me_lo_sound_root):
            for file_name in os.listdir(me_lo_sound_root):
                source_file = os.path.join(me_lo_sound_root, file_name)
                if os.path.isfile(source_file):
                    shutil.copy2(source_file, os.path.join(target_root, file_name))
            return

        self.copy_mod_overlay(self.get_old_character_sounds_preset_root(), installed_folder)

    def apply_old_avatar_background_preset(self, installed_folder):
        me_lo_background_file = os.path.join(self.get_me_lo_background_old_root(), "Mobile.rbxl")
        if os.path.exists(me_lo_background_file):
            target_file = os.path.join(installed_folder, "ExtraContent", "places", "Mobile.rbxl")
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            shutil.copy2(me_lo_background_file, target_file)
            return

        self.copy_mod_overlay(self.get_old_avatar_background_preset_root(), installed_folder)

    def apply_mouse_cursor_preset(self, installed_folder):
        cursor_preset = self.normalize_mouse_cursor_preset(self.npx_data.get("Mouse Cursor Preset"))
        if cursor_preset == "Default":
            return False

        preset_root = self.get_mouse_cursor_preset_root(cursor_preset)
        if not preset_root or not os.path.isdir(preset_root):
            log_error(f"Mouse cursor preset '{cursor_preset}' could not be applied because its folder was not found in Me_Lo\\Cursor.")
            return True

        keyboard_mouse_root = os.path.join(preset_root, "KeyboardMouse")
        if not os.path.isdir(keyboard_mouse_root):
            log_error(f"Mouse cursor preset '{cursor_preset}' is missing its KeyboardMouse folder.")
            return True

        required_cursor_files = [os.path.join(keyboard_mouse_root, file_name) for file_name in sorted(CURSOR_KEYBOARD_MOUSE_FILES)]
        shiftlock_file = os.path.join(preset_root, SHIFTLOCK_CURSOR_FILE)
        missing_files = [file_path for file_path in required_cursor_files if not os.path.exists(file_path)]
        if not os.path.exists(shiftlock_file):
            missing_files.append(shiftlock_file)

        if missing_files:
            log_error(
                f"Mouse cursor preset '{cursor_preset}' is missing required files: "
                + ", ".join(os.path.basename(file_path) for file_path in missing_files)
            )
            return True

        target_keyboard_mouse_root = os.path.join(installed_folder, "content", "textures", "Cursors", "KeyboardMouse")
        target_textures_root = os.path.join(installed_folder, "content", "textures")
        os.makedirs(target_keyboard_mouse_root, exist_ok=True)
        os.makedirs(target_textures_root, exist_ok=True)

        for source_file in required_cursor_files:
            shutil.copy2(source_file, os.path.join(target_keyboard_mouse_root, os.path.basename(source_file)))

        shutil.copy2(shiftlock_file, os.path.join(target_textures_root, SHIFTLOCK_CURSOR_FILE))
        return True

    def count_custom_roblox_font_files(self):
        font_root = self.get_custom_roblox_font_mod_root()
        return sum(
            1 for file_name in ROBLOX_UI_FONT_TARGET_FILES
            if os.path.exists(os.path.join(font_root, file_name))
        )

    def refresh_custom_roblox_font_status(self):
        if not hasattr(self, "custom_roblox_font_status_label"):
            return

        file_count = self.count_custom_roblox_font_files()
        saved_source = self.npx_data.get("Custom Roblox Font Source", "")
        source_name = os.path.basename(saved_source) if saved_source else ""

        if file_count >= len(ROBLOX_UI_FONT_TARGET_FILES):
            status_text = f"Active font file: {source_name}" if source_name else "A custom Roblox UI font is active."
        elif file_count > 0:
            status_text = f"Custom font override detected ({file_count}/{len(ROBLOX_UI_FONT_TARGET_FILES)} BuilderSans files)."
        else:
            status_text = "Using Roblox's default BuilderSans UI font."

        self.custom_roblox_font_status_label.configure(text=status_text)

        if hasattr(self, "custom_roblox_font_reset_btn"):
            self.custom_roblox_font_reset_btn.configure(state="normal" if file_count > 0 else "disabled")

    def import_custom_roblox_font(self):
        selected_file = filedialog.askopenfilename(
            title="Select a Roblox UI font file",
            filetypes=[("Font files", "*.otf *.ttf"), ("OpenType fonts", "*.otf"), ("TrueType fonts", "*.ttf"), ("All files", "*.*")]
        )
        if not selected_file:
            return

        extension = os.path.splitext(selected_file)[1].lower()
        if extension not in SUPPORTED_CUSTOM_FONT_EXTENSIONS:
            messagebox.showerror(
                "Unsupported Font",
                "Please choose a .otf or .ttf font file.",
                parent=self
            )
            return

        try:
            installed_folder = self.get_current_installed_roblox_folder()
            if installed_folder:
                self.seed_default_ui_font_backup(installed_folder)

            font_root = self.get_custom_roblox_font_mod_root()
            os.makedirs(font_root, exist_ok=True)
            source_path = os.path.abspath(selected_file)

            for file_name in ROBLOX_UI_FONT_TARGET_FILES:
                target_file = os.path.join(font_root, file_name)
                if os.path.abspath(target_file) == source_path:
                    continue
                shutil.copy2(source_path, target_file)

            self.npx_data["Custom Roblox Font Source"] = source_path
            self.save_launcher_data()
            self.refresh_custom_roblox_font_status()
            self.apply_mod_settings_if_available()

            messagebox.showinfo(
                "Roblox Font Saved",
                (
                    f"{os.path.basename(source_path)} was copied into Roblox's BuilderSans UI font slots.\n"
                    "Launch Roblox through VeloStrap to see the change."
                ),
                parent=self
            )
        except Exception as e:
            log_error(f"Could not import the Roblox font file: {e}")
            messagebox.showerror("Roblox Font", f"Could not import that font file.\n{e}", parent=self)

    def restore_default_roblox_ui_font(self, installed_folder):
        backup_root = self.get_default_ui_font_backup_root()
        if not os.path.isdir(backup_root):
            return False

        target_root = os.path.join(installed_folder, "content", "fonts")
        os.makedirs(target_root, exist_ok=True)
        restored_any = False

        for file_name in ROBLOX_UI_FONT_TARGET_FILES:
            source_file = os.path.join(backup_root, file_name)
            if not os.path.exists(source_file):
                continue
            shutil.copy2(source_file, os.path.join(target_root, file_name))
            restored_any = True

        return restored_any

    def clear_custom_roblox_font(self):
        active_font_files = self.count_custom_roblox_font_files()
        if active_font_files <= 0:
            self.npx_data["Custom Roblox Font Source"] = ""
            self.save_launcher_data()
            self.refresh_custom_roblox_font_status()
            return

        should_clear = messagebox.askyesno(
            "Reset Roblox Font",
            "Remove the custom Roblox UI font and restore the saved default BuilderSans files when available?",
            parent=self
        )
        if not should_clear:
            return

        try:
            font_root = self.get_custom_roblox_font_mod_root()
            for file_name in ROBLOX_UI_FONT_TARGET_FILES:
                target_file = os.path.join(font_root, file_name)
                if os.path.exists(target_file):
                    os.remove(target_file)

            self.npx_data["Custom Roblox Font Source"] = ""
            self.save_launcher_data()

            installed_folder = self.get_current_installed_roblox_folder()
            restored_now = False
            if installed_folder:
                restored_now = self.restore_default_roblox_ui_font(installed_folder)

            self.refresh_custom_roblox_font_status()

            message = "The custom Roblox UI font files were removed."
            if restored_now:
                message += "\nDefault BuilderSans files were restored in the current Roblox install."
            else:
                message += "\nIf Roblox still shows the old font, launch or update Roblox once to refresh its files."

            messagebox.showinfo("Roblox Font Reset", message, parent=self)
        except Exception as e:
            log_error(f"Could not clear the Roblox font override: {e}")
            messagebox.showerror("Roblox Font", f"Could not reset the custom font.\n{e}", parent=self)

    def apply_selected_mods(self, installed_folder):
        self.ensure_mods_structure()
        self.ensure_builtin_mod_presets(installed_folder)

        if self.npx_data.get("Emulate Old Character Sounds", False):
            self.apply_old_character_sounds_preset(installed_folder)

        if self.npx_data.get("Use Old Avatar Editor Background", False):
            self.apply_old_avatar_background_preset(installed_folder)

        use_cursor_preset = self.apply_mouse_cursor_preset(installed_folder)

        # Custom files are copied last so your own mod files override the built-in presets when both touch the same file.
        self.copy_mod_overlay(
            self.mods_root,
            installed_folder,
            validate_custom_files=True,
            skip_cursor_files=use_cursor_preset
        )

    # ==========================================
    # UI SETUP: HOME
    # ==========================================
    def setup_home_ui(self):
        try:
            light_logo_file = resource_path(os.path.join("assets", "VLight.png"))
            dark_logo_file = resource_path(os.path.join("assets", "VDark.png"))
            
            img_light = Image.open(light_logo_file)
            
            # Try to load the dark logo; fallback to light logo if VDark.png is missing
            try:
                img_dark = Image.open(dark_logo_file)
            except Exception:
                img_dark = img_light 
                
            # Automatically switch between these based on the Logos based via theme
            App_Logo_img = ctk.CTkImage(light_image=img_light, dark_image=img_dark, size=(125, 125))
            self.img_label = ctk.CTkLabel(self.home_frame, image=App_Logo_img, text="")
            self.img_label.pack(pady=10)
        except Exception as e: 
            print("Logo not found, please check if its in the 'assets' Folder.", e)
            
        ctk.CTkLabel(
            self.home_frame,
            text="HOME",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.get_primary_text_color()
        ).pack(pady=10)

        self.label = ctk.CTkLabel(
            self.home_frame,
            text="Welcome to VeloStrap, thank you for using it!",
            font=ctk.CTkFont(size=12),
            text_color=self.get_primary_text_color(),
            wraplength=self.get_content_wraplength(),
            justify="center"
        )
        self.label.pack(pady=12)

        self.launch_btn = ctk.CTkButton(self.home_frame, text="Launch Roblox", command=self.start_launch, width=200, height=40, font=ctk.CTkFont(size=14, weight="bold"))
        self.launch_btn.pack(pady=20)

    # ==========================================
    # UI SETUP: MODS
    # ==========================================
    def create_labeled_separator(self, parent, text):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(20, 10), padx=10)
        
        # 1. Let the grid manager handle the resizing automatically
        frame.columnconfigure(0, weight=1)  # Left line stretches
        frame.columnconfigure(1, weight=0)  # Text stays exact size
        frame.columnconfigure(2, weight=1)  # Right line stretches
        
        # 2. Left Line
        left_line = ctk.CTkFrame(frame, height=2, fg_color=self.get_border_color())
        left_line.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        
        # 3. The Text
        label = ctk.CTkLabel(
            frame, 
            text=text.upper(), 
            font=ctk.CTkFont(size=12, weight="bold"), 
            text_color=self.get_muted_text_color()
        )
        label.grid(row=0, column=1)
        
        # 4. Right Line
        right_line = ctk.CTkFrame(frame, height=2, fg_color=self.get_border_color())
        right_line.grid(row=0, column=2, sticky="ew", padx=(10, 0))

        return frame

    def setup_integrations_ui(self):
        ctk.CTkLabel(
            self.integrations_frame,
            text="MODS",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.get_primary_text_color()
        ).pack(pady=10)

        ctk.CTkLabel(
            self.integrations_frame,
            text="Choose the Roblox look you want, then VeloStrap copies those files into the current Roblox version for you.",
            font=ctk.CTkFont(size=12),
            text_color=self.get_muted_text_color(),
            wraplength=self.get_content_wraplength(),
            justify="center"
        ).pack(padx=10, pady=(0, 10))
        
        ctk.CTkButton(
            self.integrations_frame,
            text="Open Mods Folder",
            width=220,
            command=self.open_mods_folder
        ).pack(pady=(0, 8))

        ctk.CTkLabel(
            self.integrations_frame,
            text="Advanced tip: anything you place in the Mods folder can override Roblox files on the next launch.",
            font=ctk.CTkFont(size=11),
            text_color=self.get_muted_text_color(),
            wraplength=self.get_content_wraplength(),
            justify="center"
        ).pack(padx=10, pady=(0, 16))

        self.create_labeled_separator(self.integrations_frame, "Presets")

        ctk.CTkLabel(
            self.integrations_frame,
            text="Mouse Cursor:",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.get_primary_text_color()
        ).pack(pady=(4, 0))
        self.mouse_cursor_preset_var = ctk.StringVar(value=self.npx_data.get("Mouse Cursor Preset", "Default"))
        self.mouse_cursor_preset_dropdown = ctk.CTkOptionMenu(
            self.integrations_frame,
            variable=self.mouse_cursor_preset_var,
            values=MOUSE_CURSOR_PRESET_OPTIONS,
            width=260,
            command=self.handle_mouse_cursor_preset_change,
            **self.get_option_menu_style()
        )
        self.mouse_cursor_preset_dropdown.pack(pady=(6, 10))

        ctk.CTkLabel(
            self.integrations_frame,
            text="Default leaves Roblox untouched. The other presets replace the mouse cursor art with classic styles.",
            font=ctk.CTkFont(size=11),
            text_color=self.get_muted_text_color(),
            wraplength=self.get_content_wraplength(),
            justify="center"
        ).pack(padx=10, pady=(0, 8))

        self.old_character_sounds_switch = ctk.CTkSwitch(
            self.integrations_frame,
            text="Emulate old character sounds",
            command=self.handle_mod_setting_toggle
        )
        self.old_character_sounds_switch.pack(pady=10)
        if self.npx_data.get("Emulate Old Character Sounds", False):
            self.old_character_sounds_switch.select()
        else:
            self.old_character_sounds_switch.deselect()

        self.old_avatar_background_switch = ctk.CTkSwitch(
            self.integrations_frame,
            text="Use old avatar editor background",
            command=self.handle_mod_setting_toggle
        )
        self.old_avatar_background_switch.pack(pady=10)
        if self.npx_data.get("Use Old Avatar Editor Background", False):
            self.old_avatar_background_switch.select()
        else:
            self.old_avatar_background_switch.deselect()

        ctk.CTkLabel(
            self.integrations_frame,
            text="These preset switches are applied automatically before Roblox launches, so you do not need to move files around by hand.",
            font=ctk.CTkFont(size=11),
            text_color=self.get_muted_text_color(),
            wraplength=self.get_content_wraplength(),
            justify="center"
        ).pack(padx=10, pady=(4, 6))

        self.create_labeled_separator(self.integrations_frame, "Miscellaneous")

        self.discord_switch = ctk.CTkSwitch(self.integrations_frame, text="Discord Rich Presence", command=self.toggle_rpc)
        self.discord_switch.pack(pady=10)
        if self.npx_data.get("discord_rpc", True):
            self.discord_switch.select()
        else:
            self.discord_switch.deselect()

        self.multi_switch = ctk.CTkSwitch(self.integrations_frame, text="Multi-Instance", command=self.save_launcher_data)
        self.multi_switch.pack(pady=10)
        if self.npx_data.get("Multi_Instance", False):
            self.multi_switch.select()
        else:
            self.multi_switch.deselect()

        self.create_labeled_separator(self.integrations_frame, "Roblox Font")

        font_card = ctk.CTkFrame(
            self.integrations_frame,
            corner_radius=14,
            fg_color=self.get_surface_bg_color(),
            border_width=1,
            border_color=self.get_border_color()
        )
        font_card.pack(fill="x", padx=10, pady=(0, 20))

        ctk.CTkLabel(
            font_card,
            text="Custom UI Font",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.get_primary_text_color()
        ).pack(anchor="w", padx=14, pady=(14, 4))

        ctk.CTkLabel(
            font_card,
            text="Pick one .otf or .ttf file and VeloStrap will clone it into Roblox's main BuilderSans UI fonts.",
            font=ctk.CTkFont(size=11),
            text_color=self.get_muted_text_color(),
            wraplength=self.get_content_wraplength() - 40,
            justify="left"
        ).pack(anchor="w", padx=14, pady=(0, 8))

        self.custom_roblox_font_status_label = ctk.CTkLabel(
            font_card,
            text="Using Roblox's default BuilderSans UI font.",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=self.get_primary_text_color(),
            wraplength=self.get_content_wraplength() - 40,
            justify="left"
        )
        self.custom_roblox_font_status_label.pack(anchor="w", padx=14, pady=(0, 10))

        font_button_row = ctk.CTkFrame(font_card, fg_color="transparent")
        font_button_row.pack(fill="x", padx=14, pady=(0, 8))

        ctk.CTkButton(
            font_button_row,
            text="Choose Font File",
            width=155,
            command=self.import_custom_roblox_font
        ).pack(side="left")

        self.custom_roblox_font_reset_btn = ctk.CTkButton(
            font_button_row,
            text="Reset Font",
            width=120,
            command=self.clear_custom_roblox_font,
            **self.get_neutral_button_style()
        )
        self.custom_roblox_font_reset_btn.pack(side="left", padx=(10, 0))

        ctk.CTkLabel(
            font_card,
            text="Best results usually come from readable sans-serif fonts. This mainly changes Roblox's modern UI text.",
            font=ctk.CTkFont(size=11),
            text_color=self.get_muted_text_color(),
            wraplength=self.get_content_wraplength() - 40,
            justify="left"
        ).pack(anchor="w", padx=14, pady=(0, 14))

        self.refresh_custom_roblox_font_status()

    # ==========================================
    # UI SETUP: FASTFLAGS
    # ==========================================
    def setup_flags_ui(self):
        ctk.CTkLabel(
            self.flags_frame,
            text="FastFlags",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.get_primary_text_color()
        ).pack(pady=(10, 6))

        ctk.CTkLabel(
            self.flags_frame,
            text="\u26A0 ONLY ROBLOX'S OFFICIAL FASTFLAG ALLOWLIST IS SAVED.",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.get_primary_text_color(),
            wraplength=self.get_content_wraplength(),
            justify="center"
        ).pack(pady=(0, 8))

        ctk.CTkButton(
            self.flags_frame,
            text="Open FastFlag Editor",
            height=40,
            command=self.open_fastflag_editor
        ).pack(fill="x", padx=10, pady=(0, 8))

        ctk.CTkLabel(
            self.flags_frame,
            text="Open the editor window to add allowlisted FastFlags by file or paste raw JSON.",
            justify="center",
            wraplength=self.get_content_wraplength(),
            text_color=self.get_muted_text_color()
        ).pack(padx=10, pady=(0, 8))

        self.active_flags_count_label = ctk.CTkLabel(
            self.flags_frame,
            text="Current Active FastFlags (0)",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=self.get_primary_text_color()
        )
        self.active_flags_count_label.pack(pady=(0, 6))

        self.active_flags_textbox = ctk.CTkTextbox(self.flags_frame, width=400, height=170)
        self.active_flags_textbox.pack(fill="x", padx=10, pady=(0, 8))
        self.active_flags_textbox.configure(state="disabled")

        self.create_labeled_separator(self.flags_frame, "Built-In FastFlags")

        ctk.CTkLabel(
            self.flags_frame,
            text="Graphics Engine Preference",
            font=("Arial", 12),
            text_color=self.get_primary_text_color()
        ).pack(pady=(5, 0))
        self.ren_var = ctk.StringVar(value=self.npx_data.get("Rendering Mode", DEFAULT_RENDERING))
        self.dx_dropdown = ctk.CTkOptionMenu(
            self.flags_frame,
            variable=self.ren_var,
            values=RENDERING_OPTIONS,
            width=260,
            command=self.handle_fastflag_control_change,
            **self.get_option_menu_style()
        )
        self.dx_dropdown.pack(pady=5)

        self.alt_enter_fullscreen_switch = ctk.CTkSwitch(
            self.flags_frame,
            text="Enable true Alt+Enter fullscreen",
            command=self.handle_fastflag_control_change
        )
        self.alt_enter_fullscreen_switch.pack(pady=(10, 8))
        if self.npx_data.get("Alt Enter Fullscreen", False):
            self.alt_enter_fullscreen_switch.select()
        else:
            self.alt_enter_fullscreen_switch.deselect()

        ctk.CTkLabel(
            self.flags_frame,
            text="Texture Quality Override",
            font=("Arial", 12),
            text_color=self.get_primary_text_color()
        ).pack(pady=(8, 0))
        self.texture_quality_var = ctk.StringVar(
            value=self.npx_data.get("Texture Quality Mode", DEFAULT_TEXTURE_QUALITY_MODE)
        )
        self.texture_quality_dropdown = ctk.CTkOptionMenu(
            self.flags_frame,
            variable=self.texture_quality_var,
            values=TEXTURE_QUALITY_OPTIONS,
            width=260,
            command=self.handle_fastflag_control_change,
            **self.get_option_menu_style()
        )
        self.texture_quality_dropdown.pack(pady=5)

        ctk.CTkLabel(
            self.flags_frame,
            text="Anti-Aliasing",
            font=("Arial", 12),
            text_color=self.get_primary_text_color()
        ).pack(pady=(8, 0))
        self.msaa_var = ctk.StringVar(value=self.npx_data.get("MSAA Mode", DEFAULT_MSAA_MODE))
        self.msaa_dropdown = ctk.CTkOptionMenu(
            self.flags_frame,
            variable=self.msaa_var,
            values=MSAA_OPTIONS,
            width=260,
            command=self.handle_fastflag_control_change,
            **self.get_option_menu_style()
        )
        self.msaa_dropdown.pack(pady=5)

        self.mesh_quality_value_label = ctk.CTkLabel(
            self.flags_frame,
            text="Mesh Quality: Normal (Roblox default)",
            font=("Arial", 12),
            text_color=self.get_primary_text_color()
        )
        self.mesh_quality_value_label.pack(pady=(10, 2))
        self.mesh_quality_slider = ctk.CTkSlider(
            self.flags_frame,
            from_=0,
            to=len(MESH_QUALITY_LABELS) - 1,
            number_of_steps=len(MESH_QUALITY_LABELS) - 1,
            width=280,
            command=self.handle_mesh_quality_slider_change
        )
        self.mesh_quality_slider.pack(pady=(0, 2))
        self.mesh_quality_slider.set(self.npx_data.get("Mesh Quality Level", DEFAULT_MESH_QUALITY_LEVEL))
        self.refresh_mesh_quality_label()

        ctk.CTkLabel(
            self.flags_frame,
            text="Normal mesh quality uses Roblox's built-in default distances.",
            justify="center",
            wraplength=self.get_content_wraplength(),
            text_color=self.get_muted_text_color()
        ).pack(padx=10, pady=(0, 8))

        self.graphics_quality_value_label = ctk.CTkLabel(
            self.flags_frame,
            text="Graphics Quality Override: Automatic",
            font=("Arial", 12),
            text_color=self.get_primary_text_color()
        )
        self.graphics_quality_value_label.pack(pady=(8, 2))
        self.graphics_quality_slider = ctk.CTkSlider(
            self.flags_frame,
            from_=0,
            to=10,
            number_of_steps=10,
            width=280,
            command=self.handle_graphics_quality_slider_change
        )
        self.graphics_quality_slider.pack(pady=(0, 2))
        self.graphics_quality_slider.set(
            self.npx_data.get("Graphics Quality Override", DEFAULT_GRAPHICS_QUALITY_OVERRIDE)
        )
        self.refresh_graphics_quality_label()

        ctk.CTkLabel(
            self.flags_frame,
            text="Automatic leaves Roblox's graphics slider behavior untouched.",
            justify="center",
            wraplength=self.get_content_wraplength(),
            text_color=self.get_muted_text_color()
        ).pack(padx=10, pady=(0, 8))

        self.save_btn = ctk.CTkButton(self.flags_frame, text="Save FastFlags", width=420, command=self.save_fast_flags)
        self.save_btn.pack(pady=30)
        self.refresh_fastflag_views(use_current_ui=True, force=True)

    def handle_fastflag_control_change(self, _=None):
        if not self.check_rate_limit(): return
        self.refresh_fastflag_views(use_current_ui=True)

    def prompt_fastflag_overwrite(self, conflicts, parent=None):
        dialog_parent = parent or self
        overwrite_dialog = ctk.CTkToplevel(self)
        overwrite_dialog.title("Overwrite FastFlags?")
        overwrite_dialog.geometry("560x360")
        overwrite_dialog.resizable(False, False)
        overwrite_dialog.configure(fg_color=self.get_window_bg_color())
        overwrite_dialog.transient(dialog_parent)
        overwrite_dialog.grab_set()

        result = {"overwrite": False}

        ctk.CTkLabel(
            overwrite_dialog,
            text="Do you want to overwrite these fastflag(s)?",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.get_primary_text_color(),
            wraplength=self.get_dialog_wraplength(),
            justify="left"
        ).pack(anchor="w", padx=20, pady=(18, 8))

        comparison_box = ctk.CTkTextbox(overwrite_dialog, width=500, height=220)
        comparison_box.pack(fill="both", expand=True, padx=20, pady=(0, 12))

        comparison_lines = []
        for flag_name, values in sorted(conflicts.items(), key=lambda item: item[0].lower()):
            comparison_lines.append(
                f"{flag_name}\n"
                f"Existing Flag: {self.format_fastflag_value(values['existing'])}\n"
                f"New Flag: {self.format_fastflag_value(values['new'])}\n"
            )

        comparison_box.insert("1.0", "\n".join(comparison_lines).strip())
        comparison_box.configure(state="disabled")

        button_row = ctk.CTkFrame(overwrite_dialog, fg_color="transparent")
        button_row.pack(fill="x", padx=20, pady=(0, 18))

        def save_and_close():
            result["overwrite"] = True
            overwrite_dialog.destroy()

        ctk.CTkButton(button_row, text="Save", width=120, command=save_and_close).pack(side="right", padx=(8, 0))
        ctk.CTkButton(
            button_row,
            text="No",
            width=120,
            **self.get_neutral_button_style(),
            command=overwrite_dialog.destroy
        ).pack(side="right")

        overwrite_dialog.wait_window()
        return result["overwrite"]

    def open_fastflag_editor(self):
        if self.fastflag_editor_window and self.fastflag_editor_window.winfo_exists():
            self.fastflag_editor_window.focus()
            return

        # Modern, smaller, semi-transparent grey layout
        self.fastflag_editor_window = ctk.CTkToplevel(self)
        self.fastflag_editor_window.title("FastFlag Editor")
        self.fastflag_editor_window.geometry("540x650")
        self.fastflag_editor_window.resizable(False, False)
        # Deep grey/transparent look
        self.fastflag_editor_window.configure(fg_color="#18181B" if self.get_current_theme() in ["Dark", "Midnight"] else "#E4E4E7") 
        self.fastflag_editor_window.transient(self)
        self.fastflag_editor_window.grab_set()
        
        # Ensure Custom-Flags folder exists only when editor is opened
        os.makedirs(self.custom_flags_path, exist_ok=True)

        def close_editor():
            if self.fastflag_editor_window and self.fastflag_editor_window.winfo_exists():
                self.fastflag_editor_window.destroy()
            self.fastflag_editor_window = None

        self.fastflag_editor_window.protocol("WM_DELETE_WINDOW", close_editor)

        container = ctk.CTkScrollableFrame(self.fastflag_editor_window, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=15, pady=15)

        # === ADD SINGLE FLAG SECTION ===
        ctk.CTkLabel(container, text="Add Single FastFlag", font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", pady=(0, 10))
        
        single_frame = ctk.CTkFrame(container, fg_color=self.get_surface_bg_color(), corner_radius=8)
        single_frame.pack(fill="x", pady=(0, 20), ipady=10)
        
        ctk.CTkLabel(single_frame, text="Key:").grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")
        self.single_key_entry = ctk.CTkEntry(single_frame, width=380, placeholder_text="e.g. FFlagHandleAltEnterFullscreenManually")
        self.single_key_entry.grid(row=0, column=1, padx=10, pady=(10, 5))
        
        ctk.CTkLabel(single_frame, text="Value:").grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")
        self.single_val_entry = ctk.CTkEntry(single_frame, width=380, placeholder_text="e.g. False")
        self.single_val_entry.grid(row=1, column=1, padx=10, pady=(0, 10))

        def add_single_flag():
            if not self.check_rate_limit(): return
            k = self.single_key_entry.get().strip()
            v = self.single_val_entry.get().strip()
            if not k or not v: return
            
            # Basic type conversion
            if v.lower() == "true": v = True
            elif v.lower() == "false": v = False
            elif v.isdigit(): v = int(v)
            
            try:
                imported_flags, _ = self.parse_fastflag_payload(json.dumps({k: v}), parent=self.fastflag_editor_window)
                self.apply_imported_fastflags(imported_flags, parent=self.fastflag_editor_window)
                self.single_key_entry.delete(0, "end")
                self.single_val_entry.delete(0, "end")
            except Exception as e:
                messagebox.showerror("Error", str(e), parent=self.fastflag_editor_window)

        ctk.CTkButton(single_frame, text="Add Flag", command=add_single_flag, width=120).grid(row=2, column=1, sticky="e", padx=10)

        # === ADD JSON SECTION ===
        ctk.CTkLabel(container, text="Add JSON", font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", pady=(0, 10))
        
        json_frame = ctk.CTkFrame(container, fg_color=self.get_surface_bg_color(), corner_radius=8)
        json_frame.pack(fill="x", pady=(0, 20), ipady=10)

        self.fastflag_json_box = ctk.CTkTextbox(json_frame, width=460, height=150, wrap="word", fg_color=self.get_secondary_bg_color())
        self.fastflag_json_box.pack(padx=10, pady=(10, 10))

        btn_row = ctk.CTkFrame(json_frame, fg_color="transparent")
        btn_row.pack(fill="x", padx=10)
        
        ctk.CTkButton(btn_row, text="Add File", command=self.import_fastflags_from_file, width=100).pack(side="left")
        ctk.CTkButton(btn_row, text="Save JSON", command=self.save_fastflags_from_json_box, width=100).pack(side="right")

        # === SAVED FLAGS LIST ===
        self.custom_flags_count_label = ctk.CTkLabel(container, text="Saved Custom FastFlags (0)", font=ctk.CTkFont(size=14, weight="bold"))
        self.custom_flags_count_label.pack(anchor="w", pady=(0, 10))

        self.custom_flags_list_frame = ctk.CTkScrollableFrame(container, width=480, height=180, fg_color=self.get_surface_bg_color())
        self.custom_flags_list_frame.pack(fill="x")

        self.refresh_fastflag_views(use_current_ui=True, force=True)
        self.refresh_custom_fastflag_list(force=True)

    def handle_partial_fastflag_import(self, validation_error, parent=None):
        parent_window = parent or self
        merged_custom_flags = self.merge_fastflags_with_existing(validation_error.valid_flags, parent=parent_window)
        self.persist_custom_fast_flags(merged_custom_flags)

        saved_count = sum(
            1 for key, value in validation_error.valid_flags.items()
            if self.custom_fast_flags.get(key) == value
        )
        total_fastflags = len(self.build_fast_flags(use_current_ui=True))

        messagebox.showinfo(
            "FastFlag Cleanup",
            f"Saved {saved_count} Fastflags and removed {validation_error.removed_count} Fastflags, total fastflags {total_fastflags}",
            parent=parent_window
        )

        self.handle_critical_fastflag_error(
            "Some FastFlag entries were missing a key or value and had to be removed.",
            validation_error,
            parent=parent_window
        )

    def apply_imported_fastflags(self, imported_flags, parent=None):
        parent_window = parent or self
        merged_custom_flags = self.merge_fastflags_with_existing(imported_flags, parent=parent_window)
        self.persist_custom_fast_flags(merged_custom_flags)

        saved_count = sum(
            1 for key, value in imported_flags.items()
            if self.custom_fast_flags.get(key) == value
        )
        total_fastflags = len(self.build_fast_flags(use_current_ui=True))

        messagebox.showinfo(
            "FastFlags Saved",
            f"Saved {saved_count} Fastflags. Total fastflags {total_fastflags}",
            parent=parent_window
        )

    def import_fastflags_from_file(self):
        selected_file = filedialog.askopenfilename(
            title="Select a FastFlag JSON file",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if not selected_file:
            return

        try:
            with open(selected_file, "r", encoding="utf-8") as file_handle:
                raw_text = file_handle.read()
        except Exception as exc:
            self.handle_critical_fastflag_error(
                f"VeloStrap could not read '{os.path.basename(selected_file)}'.",
                exc,
                parent=self.fastflag_editor_window or self
            )

        try:
            imported_flags, _ = self.parse_fastflag_payload(
                raw_text,
                source_label=os.path.basename(selected_file),
                parent=self.fastflag_editor_window
            )
            self.apply_imported_fastflags(imported_flags, parent=self.fastflag_editor_window)
        except FastFlagImportValidationError as exc:
            self.handle_partial_fastflag_import(exc, parent=self.fastflag_editor_window)
        except Exception as exc:
            self.handle_critical_fastflag_error(
                f"{os.path.basename(selected_file)} could not be imported safely.",
                exc,
                parent=self.fastflag_editor_window or self
            )

    def save_fastflags_from_json_box(self):
        if not self.fastflag_json_box or not self.fastflag_json_box.winfo_exists():
            return

        raw_text = self.fastflag_json_box.get("1.0", "end").strip()
        if not raw_text:
            messagebox.showerror("FastFlag JSON", "Paste some FastFlag JSON before saving.", parent=self.fastflag_editor_window or self)
            return

        try:
            imported_flags, fixed_text = self.parse_fastflag_payload(
                raw_text,
                source_label="FastFlag JSON",
                parent=self.fastflag_editor_window
            )
            self.apply_imported_fastflags(imported_flags, parent=self.fastflag_editor_window)
            self.fastflag_json_box.delete("1.0", "end")
            self.fastflag_json_box.insert("1.0", fixed_text)
        except FastFlagImportValidationError as exc:
            self.handle_partial_fastflag_import(exc, parent=self.fastflag_editor_window)
        except Exception as exc:
            self.handle_critical_fastflag_error(
                "The FastFlag JSON box could not be imported safely.",
                exc,
                parent=self.fastflag_editor_window or self
            )

    def delete_custom_fastflag(self, flag_name):
        if flag_name not in self.custom_fast_flags:
            return

        if not messagebox.askyesno(
            "Delete FastFlag",
            f"Delete '{flag_name}' from CustomFFs.json?",
            parent=self.fastflag_editor_window or self
        ):
            return

        updated_custom_flags = dict(self.custom_fast_flags)
        del updated_custom_flags[flag_name]
        self.persist_custom_fast_flags(updated_custom_flags)

    # ==========================================
    # V0.1.3 UI SETUP: PROFILES
    # ==========================================
    def setup_profiles_ui(self):
        header_frame = ctk.CTkFrame(self.profiles_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(
            header_frame,
            text="Profiles",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.get_primary_text_color()
        ).pack(side="left")
        
        add_btn = ctk.CTkButton(header_frame, text="+", width=40, font=ctk.CTkFont(size=18, weight="bold"), command=lambda: self.open_profile_editor())
        add_btn.pack(side="right")

        self.profiles_list_frame = ctk.CTkFrame(self.profiles_frame, fg_color="transparent")
        self.profiles_list_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.refresh_profiles_list()

    def refresh_profiles_list(self):
        for widget in self.profiles_list_frame.winfo_children():
            widget.destroy()

        if not self.profiles_data:
            ctk.CTkLabel(
                self.profiles_list_frame,
                text="No profiles saved yet.\nClick '+' to create one!",
                text_color=self.get_muted_text_color(),
                wraplength=self.get_content_wraplength(),
                justify="center"
            ).pack(pady=20)
            return

        for p_name, p_settings in self.profiles_data.items():
            if self.is_separator_profile(p_settings):
                separator = ctk.CTkFrame(self.profiles_list_frame, height=2, fg_color=self.get_border_color())
                separator.pack(fill="x", padx=10, pady=10)
                continue

            card = ctk.CTkFrame(
                self.profiles_list_frame,
                corner_radius=8,
                fg_color=self.get_surface_bg_color(),
                border_width=1,
                border_color=self.get_border_color()
            )
            card.pack(fill="x", pady=5, padx=5, ipady=5)
            card.grid_columnconfigure(0, weight=1)

            ctk.CTkLabel(
                card,
                text=p_name,
                font=ctk.CTkFont(size=14, weight="bold"),
                justify="left",
                wraplength=250,
                text_color=self.get_primary_text_color()
            ).grid(row=0, column=0, sticky="w", padx=(15, 10), pady=10)

            if not self.is_preset_profile(p_settings):
                del_btn = ctk.CTkButton(card, text="Delete", width=60, fg_color="#D9534F", hover_color="#C9302C", 
                                        command=lambda n=p_name: self.delete_profile(n))
                del_btn.grid(row=0, column=3, padx=(5, 10), pady=10)

            edit_btn = ctk.CTkButton(card, text="Edit", width=60, **self.get_neutral_button_style(),
                                     command=lambda n=p_name: self.open_profile_editor(n))
            edit_btn.grid(row=0, column=2, padx=5, pady=10)

            use_btn = ctk.CTkButton(card, text="Use", width=90, 
                                    command=lambda s=p_settings: self.use_profile(s))
            use_btn.grid(row=0, column=1, padx=5, pady=10)

    def use_profile(self, settings):
        if self.is_separator_profile(settings):
            return

        normalized_settings = self.normalize_profile_settings(settings)
        self.npx_data.update(
            {
                "Rendering Mode": normalized_settings.get("Rendering Mode", DEFAULT_RENDERING),
                "discord_rpc": normalized_settings.get("discord_rpc", False),
                "Multi_Instance": normalized_settings.get("MultiInstance", False),
                "Mouse Cursor Preset": normalized_settings.get("Mouse Cursor Preset", "Default"),
                "Emulate Old Character Sounds": normalized_settings.get("Emulate Old Character Sounds", False),
                "Use Old Avatar Editor Background": normalized_settings.get("Use Old Avatar Editor Background", False)
            }
        )

        for stale_key in DEPRECATED_FASTFLAG_SETTING_KEYS:
            self.npx_data.pop(stale_key, None)

        self.ren_var.set(self.npx_data.get("Rendering Mode", DEFAULT_RENDERING))
        self.mouse_cursor_preset_var.set(self.npx_data.get("Mouse Cursor Preset", "Default"))

        multi_status = self.npx_data.get("Multi_Instance", False)
        if multi_status: 
            self.multi_switch.select()
        else: 
            self.multi_switch.deselect()
        
        rpc_status = self.npx_data.get("discord_rpc", False)
        if rpc_status: 
            self.discord_switch.select()
            self.start_rpc()
        else: 
            self.discord_switch.deselect()
            self.stop_rpc()

        if self.npx_data.get("Emulate Old Character Sounds", False):
            self.old_character_sounds_switch.select()
        else:
            self.old_character_sounds_switch.deselect()

        if self.npx_data.get("Use Old Avatar Editor Background", False):
            self.old_avatar_background_switch.select()
        else:
            self.old_avatar_background_switch.deselect()
        
        self.save_launcher_data()
        self.refresh_fastflag_views(use_current_ui=True, force=True)
        self.apply_mod_settings_if_available()
        messagebox.showinfo("Profile Applied", "Profile settings have been applied successfully.")

    def delete_profile(self, profile_name):
        profile_settings = self.profiles_data.get(profile_name, {})
        if self.is_preset_profile(profile_settings) or self.is_separator_profile(profile_settings):
            messagebox.showinfo("Preset Locked", f"'{profile_name}' is a built-in preset and cannot be deleted.")
            return

        confirm = messagebox.askyesno("Delete Profile", f"Are you sure you want to delete '{profile_name}'?")
        if confirm:
            if profile_name in self.profiles_data:
                del self.profiles_data[profile_name]
                self.save_profiles_data()
                self.refresh_profiles_list()

    def open_profile_editor(self, edit_name=None):
        existing_profile = self.profiles_data.get(edit_name, {})
        if self.is_separator_profile(existing_profile):
            messagebox.showinfo("Locked", "That separator line cannot be edited.")
            return

        editor = ctk.CTkToplevel(self)
        editor.title("Edit Profile" if edit_name else "Add Profile")
        editor.geometry("480x620")
        editor.grab_set()
        editor.resizable(False, False)
        editor.configure(fg_color=self.get_window_bg_color())

        p_data = self.normalize_profile_settings(self.profiles_data.get(edit_name, {
            "Rendering Mode": DEFAULT_RENDERING,
            "discord_rpc": False,
            "MultiInstance": False
        }))

        ctk.CTkLabel(editor, text="Profile Name:", text_color=self.get_primary_text_color()).pack(pady=(15, 2))
        name_entry = ctk.CTkEntry(editor, width=320)
        name_entry.pack(pady=5)
        if edit_name:
            name_entry.insert(0, edit_name)
            if self.is_preset_profile(existing_profile):
                name_entry.configure(state="disabled")
            
        rpc_val = ctk.BooleanVar(value=p_data.get("discord_rpc", False))
        ctk.CTkSwitch(editor, text="Discord Rich Presence", variable=rpc_val).pack(pady=(10, 5))
            
        scroll_area = ctk.CTkScrollableFrame(editor, fg_color=self.get_window_bg_color())
        scroll_area.pack(fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(scroll_area, text="Rendering Mode:", text_color=self.get_primary_text_color()).pack(pady=(5, 2))
        ren_val = ctk.StringVar(value=p_data.get("Rendering Mode", DEFAULT_RENDERING))
        ctk.CTkOptionMenu(
            scroll_area,
            variable=ren_val,
            values=RENDERING_OPTIONS,
            width=250,
            **self.get_option_menu_style()
        ).pack(pady=5)
        
        multi_val = ctk.BooleanVar(value=p_data.get("MultiInstance", False))
        ctk.CTkSwitch(scroll_area, text="Multi-Instance", variable=multi_val).pack(pady=10)

        ctk.CTkLabel(scroll_area, text="Mouse Cursor:", text_color=self.get_primary_text_color()).pack(pady=(10, 2))
        cursor_preset_val = ctk.StringVar(value=p_data.get("Mouse Cursor Preset", "Default"))
        ctk.CTkOptionMenu(
            scroll_area,
            variable=cursor_preset_val,
            values=MOUSE_CURSOR_PRESET_OPTIONS,
            width=250,
            **self.get_option_menu_style()
        ).pack(pady=5)

        self.profile_old_character_sounds_switch = ctk.CTkSwitch(
            scroll_area,
            text="Emulate old character sounds"
        )
        self.profile_old_character_sounds_switch.pack(pady=10)
        if p_data.get("Emulate Old Character Sounds", False):
            self.profile_old_character_sounds_switch.select()
        else:
            self.profile_old_character_sounds_switch.deselect()

        self.profile_old_avatar_background_switch = ctk.CTkSwitch(
            scroll_area,
            text="Use old avatar editor background"
        )
        self.profile_old_avatar_background_switch.pack(pady=10)
        if p_data.get("Use Old Avatar Editor Background", False):
            self.profile_old_avatar_background_switch.select()
        else:
            self.profile_old_avatar_background_switch.deselect()

        def save_current_profile():
            new_name = name_entry.get().strip()
            if not new_name:
                messagebox.showerror("Error", "Profile name cannot be empty.", parent=editor)
                return

            if edit_name and edit_name != new_name and edit_name in self.profiles_data:
                del self.profiles_data[edit_name]

            profile_type = self.get_profile_type(existing_profile) if edit_name else "CUSTOM-PROFILE"
            self.profiles_data[new_name] = self.normalize_profile_settings({
                "Type": profile_type,
                "Rendering Mode": ren_val.get(),
                "discord_rpc": rpc_val.get(),
                "MultiInstance": multi_val.get(),
                "Mouse Cursor Preset": cursor_preset_val.get(),
                "Emulate Old Character Sounds": self.profile_old_character_sounds_switch.get(),
                "Use Old Avatar Editor Background": self.profile_old_avatar_background_switch.get()
            })
            
            self.save_profiles_data()
            self.refresh_profiles_list()
            editor.destroy()

        ctk.CTkButton(editor, text="Save Profile", command=save_current_profile).pack(pady=15)


    # ==========================================
    # UI SETUP: ABOUT
    # ==========================================
    def setup_about_ui(self):
        ctk.CTkLabel(
            self.about_frame,
            text=f"About {APP_NAME}",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.get_primary_text_color()
        ).pack(pady=20)
        
        if DEBUG_TEST:
            credits_text = (
                "Founder of NewPythonX:\n"
                "@horimiya_lover8053 on Discord\n\n"
                "Business Email:\n"
                "NewPythonX_Studios@proton.me\n\n"
                "----------------------------------------------------------------------\n\n"
                f"Version: {APP_VERSION}\n"
                "Debug Mode: ON"
            )
        else:
            credits_text = (
                "Founder of NewPythonX:\n"
                "@horimiya_lover8053 on Discord\n\n"
                "Business Email:\n"
                "NewPythonX_Studios@proton.me\n\n"
                "----------------------------------------------------------------------\n\n"
                f"Version: {APP_VERSION}"
            )
        
        self.info_label = ctk.CTkLabel(
            self.about_frame,
            text=credits_text,
            font=ctk.CTkFont(size=14),
            justify="center",
            wraplength=self.get_content_wraplength(),
            text_color=self.get_primary_text_color()
        )
        self.info_label.pack(pady=10)

    # ==========================================
    # NAVIGATION HANDLERS
    # ==========================================
    def hide_all_frames(self):
        self.home_frame.grid_forget()
        self.integrations_frame.grid_forget()
        self.flags_frame.grid_forget()
        self.profiles_frame.grid_forget()
        self.about_frame.grid_forget()
        
        self.home_btn.configure(fg_color="transparent")
        self.integrations_btn.configure(fg_color="transparent")
        self.flags_btn.configure(fg_color="transparent")
        self.profiles_btn.configure(fg_color="transparent")
        self.about_btn.configure(fg_color="transparent")

    def show_home(self):
        self.hide_all_frames()
        self.home_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.home_btn.configure(fg_color=self.get_secondary_bg_color())

    def show_integrations(self):
        self.hide_all_frames()
        self.integrations_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.integrations_btn.configure(fg_color=self.get_secondary_bg_color())

    def show_flags(self):
        self.hide_all_frames()
        self.flags_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.flags_btn.configure(fg_color=self.get_secondary_bg_color())
        self.refresh_fastflag_views(use_current_ui=True)

    def show_profiles(self):
        self.hide_all_frames()
        self.profiles_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.profiles_btn.configure(fg_color=self.get_secondary_bg_color())

    def show_mods(self):
        self.show_integrations()

    def show_about(self):
        self.hide_all_frames()
        self.about_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.about_btn.configure(fg_color=self.get_secondary_bg_color())

    # ==========================================
    # ROBLOX VERSION / INSTALL MANAGEMENT
    # ==========================================
    def ensure_local_versions_root(self):
        os.makedirs(self.local_versions_path, exist_ok=True)
        return self.local_versions_path

    def get_hidden_process_kwargs(self):
        if os.name != "nt":
            return {}

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0

        hidden_kwargs = {"startupinfo": startupinfo}
        create_no_window = getattr(subprocess, "CREATE_NO_WINDOW", 0)
        if create_no_window:
            hidden_kwargs["creationflags"] = create_no_window

        return hidden_kwargs

    def find_installed_roblox_folder(self, version_id):
        if not version_id:
            return None

        version_id = str(version_id).strip()
        exact_folder = os.path.join(self.roblox_versions_path, version_id)
        exact_exe = os.path.join(exact_folder, "RobloxPlayerBeta.exe")
        if os.path.exists(exact_exe):
            return exact_folder

        return None

    def get_version_folder_sort_key(self, folder_path):
        # VeloStrap writes FastFlags and mod files into Roblox version folders, so
        # modification time can make an older install look newer than the real one.
        creation_times = []
        modification_times = []

        for candidate_path in [folder_path, os.path.join(folder_path, "RobloxPlayerBeta.exe")]:
            if not os.path.exists(candidate_path):
                continue

            try:
                creation_times.append(os.path.getctime(candidate_path))
            except OSError:
                pass

            try:
                modification_times.append(os.path.getmtime(candidate_path))
            except OSError:
                pass

        latest_creation_time = max(creation_times) if creation_times else 0
        latest_modification_time = max(modification_times) if modification_times else 0
        return (latest_creation_time, latest_modification_time, folder_path.lower())

    def get_version_folders(self, root_path):
        if not os.path.exists(root_path):
            return []

        folders = [os.path.join(root_path, folder_name) for folder_name in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, folder_name))]
        folders.sort(key=self.get_version_folder_sort_key, reverse=True)
        return folders

    def get_installed_roblox_folder(self, expected_version=None):
        if expected_version:
            exact_folder = self.find_installed_roblox_folder(expected_version)
            if exact_folder:
                return exact_folder

        for folder in self.get_version_folders(self.roblox_versions_path):
            exe_path = os.path.join(folder, "RobloxPlayerBeta.exe")
            if os.path.exists(exe_path):
                return folder

        return None

    def get_current_installed_roblox_folder(self):
        if self.last_known_live_version:
            exact_folder = self.find_installed_roblox_folder(self.last_known_live_version)
            if exact_folder:
                return exact_folder

        return self.get_installed_roblox_folder()

    def get_live_roblox_version(self):
        response = requests.get(ROBLOX_LIVE_VERSION_API, timeout=15)
        response.raise_for_status()
        payload = response.json()

        version_id = payload.get("clientVersionUpload") or payload.get("version")
        if not version_id:
            raise RuntimeError("Roblox did not return a usable live version id.")

        self.last_known_live_version = str(version_id).strip()
        return self.last_known_live_version

    def cleanup_cached_versions(self, keep_version):
        root_path = os.path.abspath(self.ensure_local_versions_root())
        keep_path = os.path.abspath(os.path.join(root_path, keep_version))

        for entry in os.listdir(root_path):
            full_path = os.path.abspath(os.path.join(root_path, entry))
            if full_path == keep_path:
                continue

            if os.path.isdir(full_path) and os.path.commonpath([root_path, full_path]) == root_path:
                try:
                    shutil.rmtree(full_path)
                    print(f"- Removed old cached Roblox version folder: {full_path}")
                except Exception as e:
                    print(f"- Could not remove old cached version folder {full_path}: {e}")

    def download_roblox_installer(self, version_id, status_callback=None):
        cache_root = self.ensure_local_versions_root()
        version_cache_folder = os.path.join(cache_root, version_id)
        os.makedirs(version_cache_folder, exist_ok=True)

        download_candidates = [
            (f"https://setup.rbxcdn.com/{version_id}-RobloxPlayerInstaller.exe", "RobloxPlayerInstaller.exe"),
            (f"https://setup.rbxcdn.com/{version_id}-Roblox.exe", "Roblox.exe"),
            ("https://setup.rbxcdn.com/RobloxPlayerLauncher.exe", "RobloxPlayerLauncher.exe")
        ]

        for url, filename in download_candidates:
            destination = os.path.join(version_cache_folder, filename)
            if os.path.exists(destination) and os.path.getsize(destination) > 0:
                if status_callback:
                    status_callback("Downloading Roblox", "Using the cached Roblox installer...", "indeterminate")
                print(f"- Reusing cached installer: {destination}")
                self.cleanup_cached_versions(version_id)
                return destination

            try:
                if status_callback:
                    status_callback("Downloading Roblox", "Downloading the latest Roblox build...", "indeterminate")
                print(f"- Downloading Roblox from {url}")
                with requests.get(url, stream=True, timeout=(15, 60)) as response:
                    if response.status_code != 200:
                        print(f"- Download candidate skipped ({response.status_code}): {url}")
                        continue

                    total_bytes = int(response.headers.get("content-length", "0") or 0)
                    downloaded_bytes = 0
                    with open(destination, "wb") as file_handle:
                        for chunk in response.iter_content(chunk_size=DOWNLOAD_CHUNK_SIZE):
                            if chunk:
                                file_handle.write(chunk)
                                downloaded_bytes += len(chunk)
                                if status_callback:
                                    if total_bytes > 0:
                                        progress_value = min(downloaded_bytes / total_bytes, 1.0)
                                        status_callback(
                                            "Downloading Roblox latest build",
                                            f"Downloading Roblox.. {progress_value:.0%}",
                                            "determinate",
                                            progress_value
                                        )
                                    else:
                                        status_callback("Downloading Roblox", "Downloading the latest Roblox build...", "indeterminate")

                if os.path.exists(destination) and os.path.getsize(destination) > 0:
                    print(f"- SUCCESS: Roblox installer cached at {destination}")
                    self.cleanup_cached_versions(version_id)
                    return destination
            except Exception as e:
                print(f"- Roblox download candidate failed: {e}")
                if os.path.exists(destination):
                    try:
                        os.remove(destination)
                    except OSError:
                        pass

        raise RuntimeError("Could not download a Roblox installer from Roblox's CDN.")

    def wait_for_roblox_install(self, expected_version, status_callback=None):
        deadline = time.time() + INSTALL_WAIT_SECONDS
        while time.time() < deadline:
            installed_folder = self.get_installed_roblox_folder(expected_version)
            if installed_folder:
                return installed_folder

            if status_callback:
                status_callback("Installing Roblox", "Installing Roblox quietly in the background...", "indeterminate")

            time.sleep(0.25)
            self.pump_ui()

        return self.get_installed_roblox_folder()

    def run_roblox_installer(self, installer_path, expected_version, silent=False, status_callback=None):
        try:
            popen_kwargs = {}
            if silent:
                popen_kwargs.update(self.get_hidden_process_kwargs())

            subprocess.Popen([installer_path], cwd=os.path.dirname(installer_path), **popen_kwargs)
        except Exception as e:
            raise RuntimeError(f"Could not start the Roblox installer.\n{e}") from e

        if status_callback:
            status_callback("Installing Roblox", "Installing Roblox..", "indeterminate")

        print("- Waiting for Roblox installation/update to finish...")
        installed_folder = self.wait_for_roblox_install(expected_version, status_callback=status_callback)
        
        if os.path.exists(self.local_versions_path):
            try:
                import shutil
                shutil.rmtree(self.local_versions_path)
                print("- Cleaned up Roblox Download folder.")
            except Exception as e:
                print(f"- Could not clean up Download folder: {e}")

        if not installed_folder:
            raise RuntimeError("The Roblox installer ran, but VeloStrap could not find RobloxPlayerBeta.exe afterward.")

        return installed_folder

    def ensure_roblox_installation(self, allow_download=True, show_errors=True, status_callback=None, silent_install=False):
        installed_folder = self.get_installed_roblox_folder()

        if status_callback:
            status_callback("Checking Roblox", "Checking for the latest Roblox version...", "indeterminate")

        try:
            live_version = self.get_live_roblox_version()
            print(f"- Roblox live version detected: {live_version}")
        except Exception as e:
            print(f"- Could not check Roblox live version: {e}")
            if installed_folder:
                if status_callback:
                    status_callback("Launching Roblox", "Could not check Roblox's live version. Launching the installed build...", "indeterminate")
                return installed_folder

            if show_errors:
                self.close_activity_window()
                messagebox.showerror("Roblox Missing", "VeloStrap could not find Roblox and also could not reach Roblox's version API.")
            return None

        exact_live_folder = self.find_installed_roblox_folder(live_version)
        if exact_live_folder:
            return exact_live_folder

        if not installed_folder:
            installed_folder = self.get_current_installed_roblox_folder()

        if installed_folder and os.path.basename(installed_folder).lower() == live_version.lower():
            return installed_folder

        if not allow_download and installed_folder:
            return installed_folder

        try:
            installer_path = self.download_roblox_installer(live_version, status_callback=status_callback)
            return self.run_roblox_installer(installer_path, live_version, silent=silent_install, status_callback=status_callback)
        except Exception as e:
            print(f"- Roblox auto-download/update failed: {e}")
            if installed_folder:
                print("- Falling back to the currently installed Roblox build.")
                if status_callback:
                    status_callback("Launching Roblox", "Roblox could not update cleanly, so VeloStrap is launching the installed build...", "indeterminate")
                return installed_folder

            if show_errors:
                self.close_activity_window()
                messagebox.showerror("Roblox Download Failed", str(e))
            return None

    # ==========================================
    # LAUNCH LOGIC
    # ==========================================
    def save_fast_flags(self):
        self.save_launcher_data()
        self.refresh_fastflag_views(use_current_ui=True)

        installed_folder = self.ensure_roblox_installation(allow_download=True, show_errors=True)
        if not installed_folder:
            return

        try:
            self.write_fast_flags(installed_folder, use_current_ui=True)
        except Exception as e:
            print(f"- FastFlag save failed: {e}")
            messagebox.showerror("Error", f"Could not save FastFlags.\n{e}")
            return

        try:
            self.apply_selected_mods(installed_folder)
        except Exception as e:
            log_error(f"Could not apply selected mods while saving FastFlags: {e}")
            messagebox.showerror("Mods Error", f"FastFlags saved, but some mods could not be applied.\n{e}")

    def build_builtin_fast_flags(self, use_current_ui=False):
        if use_current_ui:
            render = self.ren_var.get()
            alt_enter_fullscreen = bool(self.alt_enter_fullscreen_switch.get()) if hasattr(self, "alt_enter_fullscreen_switch") else False
            texture_quality_mode = self.normalize_texture_quality_mode(
                self.texture_quality_var.get() if hasattr(self, "texture_quality_var") else DEFAULT_TEXTURE_QUALITY_MODE
            )
            msaa_mode = self.normalize_msaa_mode(
                self.msaa_var.get() if hasattr(self, "msaa_var") else DEFAULT_MSAA_MODE
            )
            mesh_quality_level = self.normalize_mesh_quality_level(
                self.mesh_quality_slider.get() if hasattr(self, "mesh_quality_slider") else DEFAULT_MESH_QUALITY_LEVEL
            )
            graphics_quality_override = self.normalize_graphics_quality_override(
                self.graphics_quality_slider.get() if hasattr(self, "graphics_quality_slider") else DEFAULT_GRAPHICS_QUALITY_OVERRIDE
            )
        else:
            render = self.npx_data.get("Rendering Mode", DEFAULT_RENDERING)
            alt_enter_fullscreen = bool(self.npx_data.get("Alt Enter Fullscreen", False))
            texture_quality_mode = self.normalize_texture_quality_mode(
                self.npx_data.get("Texture Quality Mode", DEFAULT_TEXTURE_QUALITY_MODE)
            )
            msaa_mode = self.normalize_msaa_mode(
                self.npx_data.get("MSAA Mode", DEFAULT_MSAA_MODE)
            )
            mesh_quality_level = self.normalize_mesh_quality_level(
                self.npx_data.get("Mesh Quality Level", DEFAULT_MESH_QUALITY_LEVEL)
            )
            graphics_quality_override = self.normalize_graphics_quality_override(
                self.npx_data.get("Graphics Quality Override", DEFAULT_GRAPHICS_QUALITY_OVERRIDE)
            )

        flags = {}
            
        if "Vulkan" in render:
            flags["FFlagDebugGraphicsPreferD3D11"] = False
            flags["FFlagDebugGraphicsPreferVulkan"] = True
            flags["FFlagDebugGraphicsPreferOpenGL"] = False
        elif "OpenGL" in render:
            flags["FFlagDebugGraphicsPreferD3D11"] = False
            flags["FFlagDebugGraphicsPreferVulkan"] = False
            flags["FFlagDebugGraphicsPreferOpenGL"] = True
        else:
            flags["FFlagDebugGraphicsPreferD3D11"] = True
            flags["FFlagDebugGraphicsPreferVulkan"] = False
            flags["FFlagDebugGraphicsPreferOpenGL"] = False

        if alt_enter_fullscreen:
            # Roblox's Alt+Enter fullscreen behavior is enabled by setting this flag to false.
            flags["FFlagHandleAltEnterFullscreenManually"] = False

        texture_quality_value = TEXTURE_QUALITY_FLAG_VALUES.get(texture_quality_mode)
        if texture_quality_value is not None:
            flags["DFFlagTextureQualityOverrideEnabled"] = True
            flags["DFIntTextureQualityOverride"] = texture_quality_value

        msaa_value = MSAA_FLAG_VALUES.get(msaa_mode)
        if msaa_value is not None:
            flags["FIntDebugForceMSAASamples"] = msaa_value

        if graphics_quality_override > 0:
            flags["DFIntDebugFRMQualityLevelOverride"] = graphics_quality_override

        flags.update(MESH_QUALITY_FLAG_PRESETS.get(mesh_quality_level, {}))

        return flags

    def build_fast_flags(self, use_current_ui=False):
        flags = self.build_builtin_fast_flags(use_current_ui=use_current_ui)
        flags.update(self.custom_fast_flags)
        flags = dict(sorted(flags.items(), key=lambda item: item[0].lower()))
        return flags

    def write_fast_flags(self, version_folder, use_current_ui=False):
        target_dir = os.path.join(version_folder, "ClientSettings")
        os.makedirs(target_dir, exist_ok=True)
        settings_file = os.path.join(target_dir, "ClientAppSettings.json")

        with open(settings_file, "w", encoding="utf-8") as file_handle:
            json.dump(self.build_fast_flags(use_current_ui=use_current_ui), file_handle, indent=4)

        print(f"- SUCCESS: Flags applied to {settings_file}")
        return settings_file

    def start_launch(self):
        self.save_launcher_data()
        self.launch_btn.configure(state="disabled", text="Preparing Roblox...")
        self.update_activity_window("Checking for Roblox", "Checking for the latest Roblox version...", "indeterminate")

        if self.rpc:
            try:
                self.rpc.update(state="With VeloStrap", details="Playing Roblox", start=int(time.time()))
            except:
                pass

        self.voidstrap_based_installer_but_its_a_launching_sequence_instead_downloading_roblox(0)
        
    def voidstrap_based_installer_but_its_a_launching_sequence_instead_downloading_roblox(self, value):
        self.final_launch()

    def final_launch(self):
        if self.npx_data.get("Multi_Instance", False):
            try:
                ctypes.windll.kernel32.CreateMutexW(None, True, ROBLOX_MUTEX_NAME)
                print("- SUCCESS: Multi-Instance Mutex Created!")
            except Exception as e:
                print(f"- Mutex Error: {e}")

        installed_folder = self.ensure_roblox_installation(
            allow_download=True,
            show_errors=True,
            status_callback=self.update_activity_window,
            silent_install=True
        )
        if not installed_folder:
            self.reset_launch_state()
            return

        self.update_activity_window("Launching Roblox..", "Applying FFastflags and Mods..", "indeterminate")

        try:
            self.write_fast_flags(installed_folder, use_current_ui=False)
        except Exception as e:
            self.close_activity_window()
            messagebox.showerror("Error", f"Could not apply FastFlags before launch.\n{e}")
            self.reset_launch_state()
            return

        try:
            self.apply_selected_mods(installed_folder)
        except Exception as e:
            log_error(f"Could not apply selected mods before launch: {e}")
            self.close_activity_window()
            messagebox.showerror("Mods Error", f"Roblox will still launch, but some mods could not be applied.\n{e}")

        self.update_activity_window("Launching Roblox", "Starting Roblox..", "indeterminate")

        exe = os.path.join(installed_folder, "RobloxPlayerBeta.exe")
        if not os.path.exists(exe):
            self.close_activity_window()
            messagebox.showerror("Error", "RobloxPlayerBeta.exe was not found after the install/update completed.")
            self.reset_launch_state()
            return

        try:
            print(f"- SUCCESS: Found executable at {exe}. Launching...")
            subprocess.Popen([exe])
            print("Taking a few seconds to launch Roblox..")
            self.pump_ui()
            time.sleep(0.5)
            self.safe_close()
        except Exception as e:
            self.close_activity_window()
            messagebox.showerror("Launch Error", str(e))
            self.reset_launch_state()

    def reset_launch_state(self):
        self.close_activity_window()
        self.launch_btn.configure(state="normal", text="Launch Roblox")
        self.restore_idle_rpc()

    def monitor_and_close(self, proc):
        proc.wait()
        time.sleep(0.5)
        self.after(0, self.safe_close)
        
    def safe_close(self):
        self.stop_rpc()
        self.close_activity_window()
        self.destroy() 
        sys.exit()
        
# ==========================================
# Run Application
# ==========================================
if __name__ == "__main__":
    show_text_loading_sequence()
    app = LauncherStyleUI()
    app.mainloop()
