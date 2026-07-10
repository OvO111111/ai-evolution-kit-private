import argparse
import subprocess
import sys
import time

import pyautogui
import win32con
import win32gui


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.08


def visible_windows():
    items = []

    def callback(hwnd, _):
        if not win32gui.IsWindowVisible(hwnd):
            return
        title = win32gui.GetWindowText(hwnd).strip()
        if not title:
            return
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        if right <= left or bottom <= top:
            return
        items.append(
            {
                "hwnd": hwnd,
                "title": title,
                "rect": [left, top, right, bottom],
            }
        )

    win32gui.EnumWindows(callback, None)
    return items


def find_window(title_substring):
    needle = title_substring.lower()
    for item in visible_windows():
        if needle in item["title"].lower():
            return item
    return None


def cmd_screenshot(args):
    img = pyautogui.screenshot()
    img.save(args.out)
    print(f"saved {args.out} {img.size[0]}x{img.size[1]}")


def cmd_windows(_args):
    for item in visible_windows():
        left, top, right, bottom = item["rect"]
        print(f'{item["hwnd"]}\t{left},{top},{right},{bottom}\t{item["title"]}')


def cmd_activate(args):
    item = find_window(args.title)
    if not item:
        print(f"window not found: {args.title}", file=sys.stderr)
        sys.exit(2)
    hwnd = item["hwnd"]
    try:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
    except Exception as exc:
        print(f"activate failed: {exc}", file=sys.stderr)
        sys.exit(3)
    print(f'activated {hwnd} {item["title"]}')


def cmd_open(args):
    subprocess.Popen(args.app, shell=True)
    if args.wait:
        time.sleep(args.wait)
    print(f"opened {args.app}")


def cmd_click(args):
    pyautogui.click(args.x, args.y, button=args.button)
    print(f"clicked {args.x},{args.y} {args.button}")


def cmd_doubleclick(args):
    pyautogui.doubleClick(args.x, args.y, button=args.button)
    print(f"doubleclicked {args.x},{args.y} {args.button}")


def cmd_move(args):
    pyautogui.moveTo(args.x, args.y, duration=args.duration)
    print(f"moved {args.x},{args.y}")


def cmd_type(args):
    pyautogui.write(args.text, interval=args.interval)
    print(f"typed {len(args.text)} chars")


def cmd_press(args):
    pyautogui.press(args.key)
    print(f"pressed {args.key}")


def cmd_hotkey(args):
    pyautogui.hotkey(*args.keys)
    print("hotkey " + " ".join(args.keys))


def cmd_scroll(args):
    pyautogui.scroll(args.clicks, x=args.x, y=args.y)
    print(f"scrolled {args.clicks}")


def cmd_pos(_args):
    pos = pyautogui.position()
    size = pyautogui.size()
    print(f"mouse {pos.x},{pos.y} screen {size.width}x{size.height}")


def build_parser():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("screenshot")
    p.add_argument("--out", required=True)
    p.set_defaults(func=cmd_screenshot)

    p = sub.add_parser("windows")
    p.set_defaults(func=cmd_windows)

    p = sub.add_parser("activate")
    p.add_argument("--title", required=True)
    p.set_defaults(func=cmd_activate)

    p = sub.add_parser("open")
    p.add_argument("--app", required=True)
    p.add_argument("--wait", type=float, default=1.0)
    p.set_defaults(func=cmd_open)

    p = sub.add_parser("click")
    p.add_argument("--x", type=int, required=True)
    p.add_argument("--y", type=int, required=True)
    p.add_argument("--button", default="left")
    p.set_defaults(func=cmd_click)

    p = sub.add_parser("doubleclick")
    p.add_argument("--x", type=int, required=True)
    p.add_argument("--y", type=int, required=True)
    p.add_argument("--button", default="left")
    p.set_defaults(func=cmd_doubleclick)

    p = sub.add_parser("move")
    p.add_argument("--x", type=int, required=True)
    p.add_argument("--y", type=int, required=True)
    p.add_argument("--duration", type=float, default=0.0)
    p.set_defaults(func=cmd_move)

    p = sub.add_parser("type")
    p.add_argument("--text", required=True)
    p.add_argument("--interval", type=float, default=0.01)
    p.set_defaults(func=cmd_type)

    p = sub.add_parser("press")
    p.add_argument("--key", required=True)
    p.set_defaults(func=cmd_press)

    p = sub.add_parser("hotkey")
    p.add_argument("--keys", nargs="+", required=True)
    p.set_defaults(func=cmd_hotkey)

    p = sub.add_parser("scroll")
    p.add_argument("--clicks", type=int, required=True)
    p.add_argument("--x", type=int)
    p.add_argument("--y", type=int)
    p.set_defaults(func=cmd_scroll)

    p = sub.add_parser("pos")
    p.set_defaults(func=cmd_pos)

    return parser


def main():
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
