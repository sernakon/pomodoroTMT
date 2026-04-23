import asyncio
import threading

from desktop_notifier import DesktopNotifier, DEFAULT_SOUND


class NotificationManager:
    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(target=self._run_loop, daemon=True)
        self.thread.start()
    
    def _run_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    async def _send_notification(self, title, message):
        notifier = DesktopNotifier(app_name='PomodoroTMT')

        await notifier.send(
            title=title,
            message=message,
            sound=DEFAULT_SOUND,
        )
    
    def send_notification(self, title, message):
        asyncio.run_coroutine_threadsafe(
            self._send_notification(title, message),
            self.loop,
        )

    def stop(self):
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.thread.join(timeout=1)

notifier = NotificationManager()