from .signalsmanagerAbstract import AbstractSignalsManagerWithSingletonPattern


class SignalsManagerActionStopImp(AbstractSignalsManagerWithSingletonPattern):
    """

    """
    AbstractSignalsManagerWithSingletonPattern.dict_actions['stop'] = {
        'func_test_action': lambda x: not x['key'].qobject.isActive(),
        'func_perform_action': lambda x: x['key'].qobject.stop()
    }

    # ###############################################
    def _stop_with_key_test_(self, key):
        """

        :param key:
        :return:
        """
        action = self.dict_actions['stop']
        return self._action_with_test_({'key': key,
                                        'func_test_action': action['func_test_action'],
                                        'func_perform_action': action['func_perform_action']})
