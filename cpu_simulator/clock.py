class HardwareClock:
    def __init__(self):
        self.state = 0  # Starts LOW (0)
        
    def toggle(self):
        """Toggles the clock state between 0 and 1."""
        self.state = 1 if self.state == 0 else 0
        return self.state
        
    def is_rising_edge(self, old_state):
        """Returns True if the clock just transitioned from 0 to 1."""
        return old_state == 0 and self.state == 1