from .signalsmanagerImp import SignalsManagerActionStopImp


class ISignalsManagerActionStop(SignalsManagerActionStopImp):
    """Summary

    Returns:
        TYPE: Description
    """

    def stop(self, qobject):
        """Summary
        Args:
            qobject (TYPE): Description
        Returns:
            TYPE: Description
        """
        return self._stop_with_key_test_(
            self._build_key_(qobject, 'timeout ()')
        )

    def stop_all(self):
        """Summary
        Returns:
            TYPE: Description
        """
        self._action_for_all_(
            {
                'action_for_all': self._stop_with_key_test_
            }
        )

    def stop_group(self, s_group="all"):
        """Summary
        Args:
            s_group (str, optional): Description
        Returns:
            TYPE: Description
        """
        return self._action_for_group_with_test_(
            {
                'action_for_all': self.stop_all,
                'action_with_key_test': self._stop_with_key_test_,
                's_group': s_group
            }
        )