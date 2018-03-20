"""
Copyright (c) 2016-2018 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import logging

from programy.clients.client import BotClient


class PollingBotClient(BotClient):

    def __init__(self, id, argument_parser=None):
        BotClient.__init__(self, id, argument_parser=argument_parser)

    def connect(self):
        return True

    def poll_and_answer(self):
        raise NotImplementedError("You must override this and implement the logic poll for messages and send answers back")

    def sleep(self, time):
        time.sleep(time)

    def run(self):
        if self.connect():
            self.display_connected_message()

            self._running = True
            while self._running:
                self._running = self.poll_and_answer()

            if logging.getLogger().isEnabledFor(logging.DEBUG):
                logging.debug("Exiting gracefully...")

        else:
            print("Connection failed. Exception traceback printed above.")

