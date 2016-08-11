#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Mine DOGAN <mine.dogan@agem.com.tr>

from base.plugin.abstract_plugin import AbstractPlugin


class Shutdown(AbstractPlugin):
    def __init__(self, context):
        super(Shutdown, self).__init__()
        self.context = context
        self.logger = self.get_logger()

        self.initial_rules_file_path = '/etc/ahenk/iptables.rules'
        self.logger.debug('[FIREWALL - shutdown] Parameters were initialized.')

    def handle_shutdown_mode(self):
        try:
            self.logger.debug('[FIREWALL - shutdown] Adding initial rules temp file to iptables-restore as parameter...')
            self.execute('/sbin/iptables-restore < {}'.format(self.initial_rules_file_path))

            self.logger.debug('[FIREWALL - shutdown] Save the rules...')
            self.execute('service netfilter-persistent save')

            self.logger.debug('[FIREWALL - shutdown] Restart the service...')
            self.execute('service netfilter-persistent restart')

        except Exception as e:
            self.logger.error('[FIREWALL - shutdown] A problem occured while handling Firewall shutdown.py: {0}'.format(str(e)))


def handle_mode(context):
    shutdown = Shutdown(context)
    shutdown.handle_shutdown_mode()