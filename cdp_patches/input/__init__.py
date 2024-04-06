from dataclasses import dataclass

from cdp_patches import is_windows

from .async_input import AsyncInput
from .sync_input import SyncInput


# From: https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
@dataclass
class WinKeyboardCodes:
    SPACE: str = "{SPACE}"
    TAB: str = "{TAB}"
    ENTER: str = "{ENTER}"
    BACKSPACE: str = "{BACKSPACE}"
    DELETE: str = "{DELETE}"
    ESCAPE: str = "{ESC}"
    LEFT_ARROW: str = "{LEFT}"
    RIGHT_ARROW: str = "{RIGHT}"
    UP_ARROW: str = "{UP}"
    DOWN_ARROW: str = "{DOWN}"
    HOME: str = "{HOME}"
    END: str = "{END}"
    PAGE_UP: str = "{PGUP}"
    PAGE_DOWN: str = "{PGDN}"
    PRINT_SCREEN: str = "{PRTSC}"
    SCROLLLOCK: str = "{SCROLLLOCK}"
    CAPSLOCK: str = "{CAPSLOCK}"
    NUMLOCK: str = "{NUMLOCK}"
    F1: str = "{F1}"
    F2: str = "{F2}"
    F3: str = "{F3}"
    F4: str = "{F4}"
    F5: str = "{F5}"
    F6: str = "{F6}"
    F7: str = "{F7}"
    F8: str = "{F8}"
    F9: str = "{F9}"
    F10: str = "{F10}"
    F11: str = "{F11}"
    F12: str = "{F12}"
    F13: str = "{F13}"
    F14: str = "{F14}"
    F15: str = "{F15}"
    F16: str = "{F16}"
    F17: str = "{F17}"
    F18: str = "{F18}"
    F19: str = "{F19}"
    F20: str = "{F20}"
    F21: str = "{F21}"
    F22: str = "{F22}"
    F23: str = "{F23}"
    F24: str = "{F24}"
    INSERT: str = "{INSERT}"
    WIN_LEFT: str = "{LWIN}"
    WIN_RIGHT: str = "{RWIN}"
    CONTROL: str = "{VK_CONTROL}"
    SHIFT: str = "{VK_SHIFT}"
    ALT: str = "{VK_MENU}"
    CANCEL: str = "{VK_CANCEL}"
    CLEAR: str = "{VK_CLEAR}"
    EXECUTE: str = "{VK_EXECUTE}"
    KANA: str = "{VK_KANA}"
    KANJI: str = "{VK_KANJI}"
    LCONTROL: str = "{VK_LCONTROL}"
    LMENU: str = "{VK_LMENU}"
    LSHIFT: str = "{VK_LSHIFT}"
    NEXT: str = "{VK_NEXT}"
    PAUSE: str = "{VK_PAUSE}"
    PRIOR: str = "{VK_PRIOR}"
    RCONTROL: str = "{VK_RCONTROL}"
    RETURN: str = "{VK_RETURN}"
    RSHIFT: str = "{VK_RSHIFT}"
    SELECT: str = "{VK_SELECT}"
    MENU_RIGHT: str = "{RMENU}"
    ADD: str = "{VK_ADD}"
    SUBTRACT: str = "{VK_SUBTRACT}"
    DECIMAL: str = "{VK_DECIMAL}"
    MULTIPLY: str = "{VK_MULTIPLY}"
    DIVIDE: str = "{VK_DIVIDE}"
    SEPARATOR: str = "{VK_SEPARATOR}"
    NUMPAD0: str = "{VK_NUMPAD0}"
    NUMPAD1: str = "{VK_NUMPAD1}"
    NUMPAD2: str = "{VK_NUMPAD2}"
    NUMPAD3: str = "{VK_NUMPAD3}"
    NUMPAD4: str = "{VK_NUMPAD4}"
    NUMPAD5: str = "{VK_NUMPAD5}"
    NUMPAD6: str = "{VK_NUMPAD6}"
    NUMPAD7: str = "{VK_NUMPAD7}"
    NUMPAD8: str = "{VK_NUMPAD8}"
    NUMPAD9: str = "{VK_NUMPAD9}"


# From: https://github.com/python-xlib/python-xlib/blob/4e8bbf8fc4941e5da301a8b3db8d27e98de68666/Xlib/keysymdef/miscellany.py
@dataclass
class LinuxKeyboardCodes:
    SPACE: str = "space"
    TAB: str = "Tab"
    ENTER: str = "Return"
    BACKSPACE: str = "BackSpace"
    DELETE: str = "Delete"
    ESCAPE: str = "Escape"
    LEFT_ARROW: str = "Left"
    RIGHT_ARROW: str = "Right"
    UP_ARROW: str = "Up"
    DOWN_ARROW: str = "Down"
    HOME: str = "Home"
    END: str = "End"
    PAGE_UP: str = "Page_Up"
    PAGE_DOWN: str = "Page_Down"
    PRINT_SCREEN: str = "Print"
    SCROLLLOCK: str = "Scroll_Lock"
    CAPSLOCK: str = "Caps_Lock"
    NUMLOCK: str = "Num_Lock"
    F1: str = "F1"
    F2: str = "F2"
    F3: str = "F3"
    F4: str = "F4"
    F5: str = "F5"
    F6: str = "F6"
    F7: str = "F7"
    F8: str = "F8"
    F9: str = "F9"
    F10: str = "F10"
    F11: str = "F11"
    F12: str = "F12"
    F13: str = "F13"
    F14: str = "F14"
    F15: str = "F15"
    F16: str = "F16"
    F17: str = "F17"
    F18: str = "F18"
    F19: str = "F19"
    F20: str = "F20"
    F21: str = "F21"
    F22: str = "F22"
    F23: str = "F23"
    F24: str = "F24"
    INSERT: str = "Insert"
    CONTROL: str = "Control_L"  # No normal Control -> Alias
    SHIFT: str = "Shift_L"  # No normal Shift -> Alias
    ALT: str = "Alt_L"  # No normal Alt -> Alias
    CANCEL: str = "Cancel"
    CLEAR: str = "Clear"
    EXECUTE: str = "Execute"
    KANA: str = "Kana_Lock"
    KANJI: str = "Kanji"
    LCONTROL: str = "Control_L"
    LMENU: str = "Menu"
    LSHIFT: str = "Shift_L"
    NEXT: str = "Next"
    PAUSE: str = "Pause"
    PRIOR: str = "Prior"
    RCONTROL: str = "Control_R"
    RETURN: str = "Return"
    RSHIFT: str = "Shift_R"
    SELECT: str = "Select"
    MENU_RIGHT: str = "Menu"  # No right Menu -> Alias
    ADD: str = "KP_Add"
    SUBTRACT: str = "KP_Subtract"
    DECIMAL: str = "KP_Decimal"
    MULTIPLY: str = "KP_Multiply"
    DIVIDE: str = "KP_Divide"
    SEPARATOR: str = "KP_Separator"
    NUMPAD0: str = "KP_0"
    NUMPAD1: str = "KP_1"
    NUMPAD2: str = "KP_2"
    NUMPAD3: str = "KP_3"
    NUMPAD4: str = "KP_4"
    NUMPAD5: str = "KP_5"
    NUMPAD6: str = "KP_6"
    NUMPAD7: str = "KP_7"
    NUMPAD8: str = "KP_8"
    NUMPAD9: str = "KP_9"


KeyboardCodes = WinKeyboardCodes if is_windows else LinuxKeyboardCodes
__all__ = ["SyncInput", "AsyncInput", "KeyboardCodes", "WinKeyboardCodes", "LinuxKeyboardCodes", "is_windows"]
