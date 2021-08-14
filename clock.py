from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.plugins as plugins
import pwnagotchi.ui.fonts as fonts
from datetime import datetime
import logging
import toml
import yaml
import os


class PwnClock(plugins.Plugin):
    __author__ = 'https://github.com/LoganMD'
    __version__ = '1.0.4'
    __license__ = 'GPL3'
    __description__ = 'Clock/Calendar for Pwnagotchi.'
    __defaults__ = {
        'enabled': False,
    }

    def on_loaded(self):
        if 'date_format' in self.options:
            self.date_format = self.options["date_format"]
        else:
            self.date_format = '%m/%d/%y'

        if 'time_format' in self.options:
            self.time_format = self.options["time_format"]
        else:
            self.time_format = '%I:%M %p'

        logging.info('Pwnagotchi Clock Plugin loaded.')

    def on_ui_setup(self, ui):
        mem_enabled = False
        config_is_toml = True if os.path.exists('/etc/pwnagotchi/config.toml') else False
        config_path = '/etc/pwnagotchi/config.toml' if config_is_toml else '/etc/pwnagotchi/config.yml'
        with open(config_path) as f:
            data = toml.load(f) if config_is_toml else yaml.load(f, Loader=yaml.FullLoader)

            if 'memtemp' in data["main"]["plugins"]:
                if 'enabled' in data["main"]["plugins"]["memtemp"]:
                    mem_enabled = data["main"]["plugins"]["memtemp"]["enabled"]
                    if mem_enabled:
                        logging.info('Pwnagotchi Clock Plugin: memtemp is enabled.')
        if ui.is_waveshare_v2():
            pos = (130, 80) if mem_enabled else (200, 80)
            ui.add_element(
                'clock',
                LabeledValue(
                    color=BLACK,
                    label='',
                    value='-/-/-\n-:--',
                    position=pos,
                    label_font=fonts.Small,
                    text_font=fonts.Small
                )
            )

    def on_ui_update(self, ui):
        now = datetime.now()
        current_time = now.strftime(f'{self.date_format}\n{self.time_format}')
        ui.set('clock', current_time)
