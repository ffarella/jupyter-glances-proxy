import os

def setup_glances():
    name = 'glances'
    def _get_glances_cmd(port):
        return ["glances", "--enable-process-extended", "--enable-irq", "-w", f"-p {port}"]
    return {
        'command': _get_glances_cmd,
        'launcher_entry': {
            'title': 'Glances',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'glances.png')
        }
    }
