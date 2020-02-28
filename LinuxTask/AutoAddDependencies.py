import logging
import time

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

# Create and configure logger
logging.basicConfig(filename="DependencyChange.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class DependencyHandler(PatternMatchingEventHandler):
    patterns = ["requirements.json"]

    @staticmethod
    def process(event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False-
        event.src_path
            path/to/observed/file
        """
        try:
            if event.event_type == "created":
                pass
            if event.event_type == "modified":
                pass
        except Exception as e_one:
            logger.error(f"Error while changing video title: {str(e_one)}")

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)


if __name__ == '__main__':
    observer = Observer()
    observer.schedule(DependencyHandler(), path='..')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt as KI:
        observer.stop()
    except Exception as e:
        logger.error(f"Unexpected exception: {str(e)}")
    observer.join()
