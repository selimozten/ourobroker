import torch
from model_training import MarketMakerModel

class InferenceEngine:
    def __init__(self):
        self.model = MarketMakerModel().cuda()
        self.model.load_state_dict(torch.load('model_weights.pth'))
        self.model.eval()

    def predict(self, market_data):
        with torch.no_grad():
            data_tensor = torch.tensor(market_data, dtype=torch.float32).cuda()
            action_probs = self.model(data_tensor)
            action = torch.argmax(action_probs).item()
            return action  # 0: Buy, 1: Sell, 2: Hold
