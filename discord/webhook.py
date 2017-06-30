# -*- coding: utf-8 -*-

"""
The MIT License (MIT)
Copyright (c) 2017 EndenDragon
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from .mixins import Hashable

class Webhook(Hashable):
    """Represents a Discord webhook in a :class:`Server`.
    
    Supported Operations:
    
    +-----------+------------------------------------------------------------------+
    | Operation |                           Description                            |
    +===========+==================================================================+
    | x == y    | Checks if two webhooks are equal.                                |
    +-----------+------------------------------------------------------------------+
    | x != y    | Checks if two webhooks are not equal.                            |
    +-----------+------------------------------------------------------------------+
    | hash(x)   | Return the webhook's hash.                                       |
    +-----------+------------------------------------------------------------------+
    | str(x)    | Returns the webhook's name.                                      |
    +-----------+------------------------------------------------------------------+
    
    Attributes
    ----------
    id : str
        The ID for the webhook.
    name : str
        The name of the webhook.
    server : :class:`Server`
        The server the webhook belongs to.
    channel : :class:`Channel`
        The channel the webhook belongs to.
    token : str
        The secret token to the webhook.
    """
    
    __slots__ = ['id', 'name', 'server', 'channel', 'token']
    
    def __init__(self, **kwargs):
        self._update(**kwargs)
    
    def _update(self, **kwargs):
        self.name = kwargs.get('name')
        self.server = kwargs.get('server')
        self.channel = kwargs.get('channel')
        self.id = kwargs.get('id')
        self.token = kwargs.get('token')
    
    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return isinstance(other, Webhook) and other.id == self.id
        
    def __hash__(self):
        return hash(self.id)
    
    @property
    def url(self):
        """Returns a friendly URL version of the webhook"""
        url = "https://discordapp.com/api/webhooks/{0.id}/{0.token}"
        return url.format(self)