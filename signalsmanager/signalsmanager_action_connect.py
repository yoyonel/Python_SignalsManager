from .signalsmanagerImp import SignalsManagerActionConnectImp


class ISignalsManagerActionConnect(SignalsManagerActionConnectImp):
    """Summary

    Returns:
        TYPE: Description
    """

    def connect(self, qobject, signal_signature):
        """Summary
        Args:
            qobject (TYPE): Description
            signal_signature (TYPE): Description
        Returns:
            TYPE: Description
        """
        return self._connect_with_key_test_(
            self._build_key_(qobject, signal_signature)
        )

    def connect_all(self):
        """Summary
        Returns:
            TYPE: Description
        """
        self._action_for_all_(
            {
                'action_for_all': self._connect_with_key_test_
            }
        )

    def connect_group(self, s_group="all"):
        """Summary
        Args:
            s_group (str, optional): Description
        Returns:
            TYPE: Description
        """
        return self._action_for_group_with_test_(
            {
                'action_for_all': self.connect_all,
                'action_with_key_test': self._connect_with_key_test_,
                's_group': s_group
            }
        )
