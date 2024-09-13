import numpy as np

class DEXEnvironment:
    def __init__(self):
        self.state = self._get_initial_state()

    def _get_initial_state(self):
        # Initialize state
        return np.zeros(100)

    def reset(self):
        self.state = self._get_initial_state()
        return self.state

    def step(self, action):
        # Simulate environment step
        next_state = self.state + np.random.randn(100) * 0.01
        reward = self._calculate_reward(action)
        done = False  # Define termination condition
        return next_state, reward, done, {}

    def _calculate_reward(self, action):
        # Define reward function
        return np.random.randn()
