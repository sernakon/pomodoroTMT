import asyncio
import signal

from desktop_notifier import DesktopNotifier, Urgency, Button, ReplyField, DEFAULT_SOUND


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

    stop_event = asyncio.Event()
    loop = asyncio.get_running_loop()

    loop.add_signal_handler(signal.SIGINT, stop_event.set)
    loop.add_signal_handler(signal.SIGTERM, stop_event.set)

    await stop_event.wait()

def send_notification(title, message):    
    asyncio.run(_send_notification(title, message))