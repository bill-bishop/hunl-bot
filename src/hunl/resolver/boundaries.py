class BoundaryValues:
    """
    Provides blueprint boundary values for re-solving.
    """
    def __init__(self, blueprint):
        self.blueprint = blueprint

    def get_boundary(self, state):
        """
        Estimate boundary value from blueprint policy.
        """
        info_tensor = state.information_state_tensor(state.current_player())
        # Placeholder: in practice, query blueprint policy/value net
        return 0.0
