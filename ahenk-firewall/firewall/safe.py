#!/usr/bin/python3
# -*- coding: utf-8 -*-

from base.plugin.abstract_plugin import AbstractPlugin


class Safe(AbstractPlugin):
    def __init__(self, context):
        super(Safe, self).__init__()
        self.context = context
        self.username = str(context.get_username())
        self.logger = self.get_logger()

        self.initial_rules_file_path = '/etc/ahenk/iptables.rules'
        self.logger.debug('[FIREWALL - safe] Parameters were initialized.')


    def handle_safe_mode(self):
        self.logger.debug('[FIREWALL - safe] Adding initial rules temp file to iptables-restore as parameter...')
        self.execute('/sbin/iptables-restore < {}'.format(self.initial_rules_file_path))

        self.logger.debug('[FIREWALL - safe] Save the rules...')
        self.execute('service netfilter-persistent save')

        self.logger.debug('[FIREWALL - safe] Restart the service...')
        self.execute('service netfilter-persistent restart')


def handle_mode(context):
    safe = Safe(context)
    safe.handle_safe_mode()
