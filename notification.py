import asyncio

from desktop_notifier import DesktopNotifier, Button, DEFAULT_SOUND


async def _send_notification(title, message):
    notifier = DesktopNotifier(app_name="PomodoroTMT")

    await notifier.send(
        title=title,
        message=message,
        buttons = [Button(
                title="Stop/start",
                on_pressed=lambda: print("stopstart"),
            )],
        on_dispatched=lambda: print("Notification showing"),
        on_clicked=lambda: print("Notification clicked"),
        on_dismissed=lambda: print("Notification dismissed"),
        sound=DEFAULT_SOUND,
    )

    await asyncio.sleep(5)

def send_notification(title, message):
    asyncio.run(_send_notification(title, message))

send_notification("PomodoroTMT", "PomodoroTMT")
