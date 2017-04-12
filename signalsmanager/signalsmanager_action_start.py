from .signalsmanagerImp import SignalsManagerActionStartImp


class ISignalsManagerActionStart(SignalsManagerActionStartImp):
    """Summary

    Returns:
        TYPE: Description
    """

    def start(self, qobject, interval=0.0):
        """Summary
        Args:
            qobject (TYPE): Description
            interval (float, optional): Description
        Returns:
            TYPE: Description
        """
        return self._start_with_key_(
            self._build_key_(qobject, 'timeout ()'), interval
        )

    def start_all(self, interval=0.0):
        """Summary
        Args:
            interval (float, optional): Description
        Returns:
            TYPE: Description
        """
        self._action_for_all_(
            {
                'action_for_all': self._start_with_key_,
                'interval': interval
            }
        )

    def start_group(self, interval=0.0, s_group="all"):
        """Summary
        Args:
            interval (float, optional): Description
            s_group (str, optional): Description
        Returns:
            TYPE: Description
        """
        return self._action_for_group_with_test_(
            {
                'action_for_all': self.start_all,
                'action_with_key_test': self.start_with_key_test,
                's_group': s_group,
                'interval': interval
            }
        )