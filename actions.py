import os
import re
import time
import webbrowser
import subprocess
from urllib.parse import quote_plus

import pyautogui


# ============================================================
# J.A.R.V.I.S. ACTIONS
# ============================================================

HOME = os.path.expanduser("~")


# ============================================================
# WEBSITES
# ============================================================

WEBSITES = {
    "youtube": "https://www.youtube.com/",
    "google": "https://www.google.com/",
    "gmail": "https://mail.google.com/",
    "github": "https://github.com/",
    "chatgpt": "https://chatgpt.com/",
    "facebook": "https://www.facebook.com/",
    "instagram": "https://www.instagram.com/",
    "whatsapp": "https://web.whatsapp.com/",
    "spotify": "https://open.spotify.com/",
    "discord": "https://discord.com/app",
    "reddit": "https://www.reddit.com/",
    "netflix": "https://www.netflix.com/",
    "amazon": "https://www.amazon.com/",
    "wikipedia": "https://www.wikipedia.org/",
    "tiktok": "https://www.tiktok.com/",
    "twitter": "https://x.com/",
    "x": "https://x.com/",
    "google drive": "https://drive.google.com/",
    "google maps": "https://maps.google.com/",
    "google docs": "https://docs.google.com/",
    "google sheets": "https://sheets.google.com/",
    "google classroom": "https://classroom.google.com/",
}


# ============================================================
# WINDOWS APPLICATIONS
# ============================================================

WINDOWS_APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "calc": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "command prompt": "cmd.exe",
    "explorer": "explorer.exe",
    "file explorer": "explorer.exe",
    "task manager": "taskmgr.exe",
    "control panel": "control.exe",
    "snipping tool": "snippingtool.exe",
}


# ============================================================
# WINDOWS FOLDERS
# ============================================================

WINDOWS_FOLDERS = {
    "desktop": os.path.join(HOME, "Desktop"),
    "downloads": os.path.join(HOME, "Downloads"),
    "documents": os.path.join(HOME, "Documents"),
    "pictures": os.path.join(HOME, "Pictures"),
    "videos": os.path.join(HOME, "Videos"),
    "music": os.path.join(HOME, "Music"),
}


# ============================================================
# OPEN URL
# ============================================================

def open_url(url):

    try:

        webbrowser.open(url)

        return True

    except Exception as e:

        print(
            "URL ERROR:",
            e
        )

        return False


# ============================================================
# OPEN WEBSITE
# ============================================================

def open_website(name):

    name = name.lower().strip()

    if name in WEBSITES:

        open_url(
            WEBSITES[name]
        )

        return True

    return False


# ============================================================
# OPEN WINDOWS APP
# ============================================================

def open_windows_app(name):

    name = name.lower().strip()

    if name in WINDOWS_APPS:

        try:

            subprocess.Popen(
                WINDOWS_APPS[name],
                shell=True
            )

            return True

        except Exception as e:

            print(
                "APP ERROR:",
                e
            )

    return False


# ============================================================
# OPEN WINDOWS FOLDER
# ============================================================

def open_windows_folder(name):

    name = name.lower().strip()

    if name in WINDOWS_FOLDERS:

        path = WINDOWS_FOLDERS[name]

        if os.path.exists(path):

            try:

                os.startfile(path)

                return True

            except Exception as e:

                print(
                    "FOLDER ERROR:",
                    e
                )

    return False


# ============================================================
# YOUTUBE SEARCH
# ============================================================

def youtube_search(query):

    query = query.strip()

    if not query:

        return (
            True,
            "Please tell me what to search on YouTube, Sir."
        )

    url = (
        "https://www.youtube.com/results?search_query="
        + quote_plus(query)
    )

    open_url(url)

    return (
        True,
        f"Searching YouTube for {query}, Sir."
    )


# ============================================================
# GOOGLE SEARCH
# ============================================================

def google_search(query):

    query = query.strip()

    if not query:

        return (
            True,
            "Please tell me what to search for, Sir."
        )

    url = (
        "https://www.google.com/search?q="
        + quote_plus(query)
    )

    open_url(url)

    return (
        True,
        f"Searching for {query}, Sir."
    )


# ============================================================
# OPEN MULTIPLE APPS
# ============================================================

def open_multiple_apps(apps):

    opened = []

    for app in apps:

        app = app.strip()

        if not app:

            continue

        if open_windows_app(app):

            opened.append(app)

            time.sleep(1)

            continue

        if open_windows_folder(app):

            opened.append(app)

            time.sleep(1)

            continue

        if open_website(app):

            opened.append(app)

            time.sleep(1)

            continue

        url = (
            "https://www.google.com/search?q="
            + quote_plus(app)
        )

        open_url(url)

        opened.append(app)

        time.sleep(1)

    if opened:

        return (
            True,
            "I opened the requested applications, Sir."
        )

    return (
        True,
        "I could not open the requested applications."
    )


# ============================================================
# UNIVERSAL OPEN
# ============================================================

def universal_open(target):

    target = target.strip()

    if not target:

        return (
            True,
            "What would you like me to open, Sir?"
        )

    lower_target = target.lower()

    # --------------------------------------------------------
    # WINDOWS APP
    # --------------------------------------------------------

    if open_windows_app(lower_target):

        return (
            True,
            f"Opening {target}, Sir."
        )

    # --------------------------------------------------------
    # WINDOWS FOLDER
    # --------------------------------------------------------

    if open_windows_folder(lower_target):

        return (
            True,
            f"Opening {target}, Sir."
        )

    # --------------------------------------------------------
    # WEBSITE
    # --------------------------------------------------------

    if open_website(lower_target):

        return (
            True,
            f"Opening {target}, Sir."
        )

    # --------------------------------------------------------
    # DIRECT URL
    # --------------------------------------------------------

    if (
        lower_target.startswith("http://")
        or lower_target.startswith("https://")
    ):

        open_url(target)

        return (
            True,
            f"Opening {target}, Sir."
        )

    # --------------------------------------------------------
    # GOOGLE SEARCH FALLBACK
    # --------------------------------------------------------

    url = (
        "https://www.google.com/search?q="
        + quote_plus(target)
    )

    open_url(url)

    return (
        True,
        f"Searching for {target}, Sir."
    )


# ============================================================
# SCREENSHOT
# ============================================================

def take_screenshot():

    try:

        folder = os.path.join(
            WINDOWS_FOLDERS["pictures"],
            "JARVIS Screenshots"
        )

        os.makedirs(
            folder,
            exist_ok=True
        )

        filename = time.strftime(
            "screenshot_%Y%m%d_%H%M%S.png"
        )

        path = os.path.join(
            folder,
            filename
        )

        image = pyautogui.screenshot()

        image.save(path)

        return (
            True,
            "Screenshot saved, Sir."
        )

    except Exception as e:

        print(
            "SCREENSHOT ERROR:",
            e
        )

        return (
            True,
            "I could not take the screenshot."
        )


# ============================================================
# TIME
# ============================================================

def tell_time():

    current_time = time.strftime(
        "%I:%M %p"
    )

    return (
        True,
        f"The time is {current_time}, Sir."
    )


# ============================================================
# DATE
# ============================================================

def tell_date():

    current_date = time.strftime(
        "%A, %B %d, %Y"
    )

    return (
        True,
        f"Today is {current_date}, Sir."
    )


# ============================================================
# SHUTDOWN COMPUTER
# ============================================================

def shutdown_computer():

    print(
        "Shutting down computer in 5 seconds..."
    )

    subprocess.Popen(
        "shutdown /s /t 5",
        shell=True
    )

    return (
        False,
        "Shutting down the computer in 5 seconds, Sir."
    )


# ============================================================
# RESTART COMPUTER
# ============================================================

def restart_computer():

    print(
        "Restarting computer in 5 seconds..."
    )

    subprocess.Popen(
        "shutdown /r /t 5",
        shell=True
    )

    return (
        False,
        "Restarting the computer in 5 seconds, Sir."
    )


# ============================================================
# CANCEL SHUTDOWN / RESTART
# ============================================================

def cancel_shutdown():

    subprocess.Popen(
        "shutdown /a",
        shell=True
    )

    return (
        True,
        "The scheduled shutdown has been cancelled, Sir."
    )


# ============================================================
# LOCK COMPUTER
# ============================================================

def lock_computer():

    subprocess.Popen(
        "rundll32.exe user32.dll,LockWorkStation",
        shell=True
    )

    return (
        False,
        "Locking the computer, Sir."
    )


# ============================================================
# MAIN COMMAND HANDLER
# ============================================================

def handle_basic_command(command):

    if not command:

        return True, ""

    command = command.strip()

    lower = command.lower()


    # ========================================================
    # SHUTDOWN
    # ========================================================

    if lower in [
        "shutdown",
        "shutdown computer",
        "shutdown pc",
        "shut down",
        "shut down computer",
        "shut down pc",
        "shut down my computer",
        "shutdown my computer",
        "power off computer",
        "power off pc",
        "turn off computer",
        "turn off pc",
    ]:

        return shutdown_computer()


    # ========================================================
    # RESTART
    # ========================================================

    if lower in [
        "restart",
        "restart computer",
        "restart pc",
        "reboot",
        "reboot computer",
        "reboot pc",
    ]:

        return restart_computer()


    # ========================================================
    # CANCEL SHUTDOWN
    # ========================================================

    if lower in [
        "cancel shutdown",
        "cancel restart",
        "abort shutdown",
        "abort restart",
        "stop shutdown",
    ]:

        return cancel_shutdown()


    # ========================================================
    # LOCK COMPUTER
    # ========================================================

    if lower in [
        "lock computer",
        "lock pc",
        "lock my computer",
        "lock my pc",
    ]:

        return lock_computer()


    # ========================================================
    # EXIT JARVIS
    # ========================================================

    if lower in [
        "exit",
        "quit",
        "close jarvis",
        "shutdown jarvis",
    ]:

        return (
            False,
            "Goodbye, Sir."
        )


    # ========================================================
    # TIME
    # ========================================================

    if lower in [
        "time",
        "what time is it",
        "tell me the time",
        "current time",
    ]:

        return tell_time()


    # ========================================================
    # DATE
    # ========================================================

    if lower in [
        "date",
        "what is the date",
        "what is today's date",
        "tell me the date",
        "today's date",
    ]:

        return tell_date()


    # ========================================================
    # SCREENSHOT
    # ========================================================

    if lower in [
        "screenshot",
        "take screenshot",
        "take a screenshot",
        "capture screen",
    ]:

        return take_screenshot()


    # ========================================================
    # YOUTUBE
    # ========================================================

    youtube_patterns = [

        r"^search\s+youtube\s+for\s+(.+)$",

        r"^search\s+youtube\s+(.+)$",

        r"^youtube\s+search\s+(.+)$",

        r"^youtube\s+(.+)$",
    ]

    for pattern in youtube_patterns:

        match = re.match(
            pattern,
            command,
            flags=re.IGNORECASE
        )

        if match:

            return youtube_search(
                match.group(1).strip()
            )


    # ========================================================
    # GOOGLE
    # ========================================================

    google_patterns = [

        r"^search\s+google\s+for\s+(.+)$",

        r"^search\s+google\s+(.+)$",

        r"^google\s+search\s+(.+)$",
    ]

    for pattern in google_patterns:

        match = re.match(
            pattern,
            command,
            flags=re.IGNORECASE
        )

        if match:

            return google_search(
                match.group(1).strip()
            )


    # ========================================================
    # MULTIPLE APPS
    # ========================================================

    if (
        lower.startswith("open ")
        and " and " in lower
    ):

        targets = command[
            len("open "):
        ].strip()

        apps = re.split(
            r"\s+and\s+",
            targets,
            flags=re.IGNORECASE
        )

        return open_multiple_apps(
            apps
        )


    # ========================================================
    # OPEN
    # ========================================================

    if lower.startswith("open "):

        target = command[
            len("open "):
        ].strip()

        return universal_open(
            target
        )


    # ========================================================
    # SEARCH
    # ========================================================

    if lower.startswith("search "):

        query = command[
            len("search "):
        ].strip()

        return google_search(
            query
        )


    # ========================================================
    # FALLBACK
    # ========================================================

    return universal_open(
        command
    )


# ============================================================
# TEST MODE
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("J.A.R.V.I.S. ACTIONS TEST")
    print("=" * 60)
    print()

    print("Website examples:")
    print()

    print("open instagram")
    print("open whatsapp")
    print("open youtube")
    print("open google")
    print("open gmail")
    print("open github")
    print("open spotify")

    print()

    print("PC commands:")
    print()

    print("shutdown computer")
    print("restart computer")
    print("lock computer")
    print("cancel shutdown")
    print("cancel restart")

    print()

    while True:

        try:

            command = input(
                "You: "
            ).strip()

            if not command:

                continue

            running, answer = (
                handle_basic_command(
                    command
                )
            )

            print(
                "JARVIS:",
                answer
            )

            if not running:

                break

        except KeyboardInterrupt:

            print()

            print(
                "JARVIS stopped."
            )

            break

        except Exception as e:

            print()

            print(
                "ERROR:",
                e
            )

            print()