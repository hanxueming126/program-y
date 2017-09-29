"""
Copyright (c) 2016-17 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import logging
import xml.etree.ElementTree as ET

from programy.oob.oob import OutOfBandProcessor


class DialOutOfBandProcessor(OutOfBandProcessor):
    """
    <oob>
        <dial>07777777777</dial>
    </oob>
    """

    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._number = None

    def parse_oob_xml(self, oob: ET.Element):
        if oob is not None and oob.text is not None:
            self._number = oob.text
            return True
        else:
            if logging.getLogger().isEnabledFor(logging.ERROR):
                logging.error("Unvalid dial oob command - missing dial text!")
            return False

    def execute_oob_command(self, bot, clientid):
        if logging.getLogger().isEnabledFor(logging.INFO):
            logging.info("DialOutOfBandProcessor: Dialing=%s", self._number)
        return "DIAL"
