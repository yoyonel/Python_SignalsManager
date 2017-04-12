from PyQt4.QtCore import QObject
from .signalsmanagerAbstract import AbstractSignalsManagerWithSingletonPattern

from .signalsmanagerImp_action_connect import SignalsManagerActionConnectImp


class SignalsManagerActionDisconnectImp(AbstractSignalsManagerWithSingletonPattern):
    """

    """
    AbstractSignalsManagerWithSingletonPattern.dict_actions['disconnect'] = {
        'func_test_action': lambda x: not x['dict_values'].setdefault(
            SignalsManagerActionConnectImp.id_str_signal_is_connected, False),
        'func_perform_action': lambda x: [
            QObject.disconnect(x['key'].qobject, x['dict_values']['Signal'], x['dict_values']['Slot']),
            x['dict_values'].__setitem__(SignalsManagerActionConnectImp.id_str_signal_is_connected, False)
        ]
    }

    # ##############################################
    def _disconnect_with_key_test_(self, key):
        """

        :param key:
        :return:
        """
        action_disconnect = self.dict_actions['disconnect']
        return self._action_with_test_({'key': key,
                                        'func_test_action': action_disconnect['func_test_action'],
                                        'func_perform_action': action_disconnect['func_perform_action']})
