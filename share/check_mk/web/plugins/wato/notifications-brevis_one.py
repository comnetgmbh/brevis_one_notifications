#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Copyright 2021 Fabian Binder, comNET GmbH <fabian.binder@comnetgmbh.com>
#
# This file is part of Brevis_one_notifications.
#
# Brevis_one_notifications is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Brevis_one_notifications is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Brevis_one_notifications.  If not, see <http://www.gnu.org/licenses/>.
#

from cmk.gui.i18n import _

from cmk.gui.valuespec import (
    Checkbox,
    Dictionary,
    ListOfStrings,
    Password,
    TextAscii,
)

from cmk.gui.plugins.wato import (
    notification_parameter_registry,
    NotificationParameter,
)

@notification_parameter_registry.register
class NotificationParameterBrevisOne(NotificationParameter):
    @property
    def ident(self):
        return "brevis_one"

    @property
    def spec(self):
        return Dictionary(
            title=_("Create notification with the following parameters"),
            required_keys = ['host'],
            elements = [
                ( 'host',
                    ListOfStrings(
                        title = _('Brevis.one gateways'),
                        help = _('Hostname, IPv4 or IPv6 address of the Brevis.one systems. '
                                 'If the connection to the first gateway fails, the notification'
                                 'script will try to send the notification using the next gateway.'),
                        size = 40,
                        allow_empty = False,
                    )
                ),
                ( 'username',
                    TextAscii(
                        title = _('Username'),
                        help = _('Username used for authentication at the Brevis.one Web-API'),
                        default_value = 'brevis_one',
                        size = 40,
                        allow_empty = False,
                    )
                ),
                ( 'password',
                    Password(
                        title = _('Password'),
                        help = _('Password used for authentication at the Brevis.one Web-API'),
                        default_value = 'brevis_one',
                        size = 40,
                        allow_empty = False,
                    )
                ),
                ( 'ignore_missing',
                    Checkbox(
                        title = _("Ignore missing pager number"),
                        help = _('If this option is set, the plugin will not exit with an error '
                                 'code. The result will still show the "missing number" message, '
                                 'but the state will be OK.'),
                        label = 'Ignore missing pager number',
                        true_label = 'Ignoring missing pager numbers',
                        false_label = 'In case of missing pager number, show warning',
                )),
            ]
        )
