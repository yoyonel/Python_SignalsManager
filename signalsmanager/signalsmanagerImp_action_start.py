from .signalsmanagerAbstract import AbstractSignalsManagerWithSingletonPattern

# ##################################################################################################
class SignalsManagerActionStartImp(AbstractSignalsManagerWithSingletonPattern):
    """

    """
    AbstractSignalsManagerWithSingletonPattern.dict_actions['start'] = {
        'func_test_action': lambda x: False,  # no condition to start a thread (?)
        'func_perform_action': lambda x: x['key'].qobject.start(x['interval'])
    }

    ################################################
    def _start_with_key_(self, key, interval):
        """

        :param key:
        :return:
        """
        action = self.dict_actions['start']
        return self._action_with_test_({'key': key,
                                        'func_test_action': action['func_test_action'],
                                        'func_perform_action': action['func_perform_action'],
                                        'interval': interval})
