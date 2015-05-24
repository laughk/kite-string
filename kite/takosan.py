#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

class Tako(object):
    def __init__(self, takosan_url, channels, payload_base={}):
        self.takosan_url  = '{0}/privmsg'.format(takosan_url)
        self.channels = channels
        self.payload_base = payload_base

        self._claen_payload()
        self.payloads = self._make_payload()

    def _claen_payload(self):
        for key, value in self.payload_base.copy().items():
            if value == None:
                del self.payload_base[key]

    def _make_payload(self):
        _payloads = []
        for channel in self.channels:
            _payload = {'channel': channel }
            _payload.update(self.payload_base)
            _payloads.append(_payload)
        return _payloads

    def post_payloads(self):
        for payload in self.payloads:
            res = requests.post(url=self.takosan_url, data=payload)

    def flying(self):
        self.post_payloads()
