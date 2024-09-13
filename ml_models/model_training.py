import torch
import torch.nn as nn
import torch.optim as optim
from reinforcement_env import DEXEnvironment
from data_pipeline import DataLoader

class MarketMakerModel(nn.Module):
    def __init__(self):
        super(MarketMakerModel, self).__init__()
        self.fc1 = nn.Linear(100, 256)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(256, 3)  # Buy, Sell, Hold

    def forward(self, x):
        x = self.relu(self.fc1(x))
        return self.fc2(x)

def train_model():
    env = DEXEnvironment()
    model = MarketMakerModel().cuda()
    optimizer = optim.Adam(model.parameters(), lr=1e-4)
    criterion = nn.MSELoss()
    data_loader = DataLoader()

    for epoch in range(1000):
        state = env.reset()
        done = False
        while not done:
            state_tensor = torch.tensor(state, dtype=torch.float32).cuda()
            action_probs = model(state_tensor)
            action = torch.argmax(action_probs).item()
            next_state, reward, done, _ = env.step(action)
            target = reward + 0.99 * torch.max(model(torch.tensor(next_state, dtype=torch.float32).cuda()))
            loss = criterion(action_probs[action], target)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            state = next_state
        print(f"Epoch {epoch} completed.")

    torch.save(model.state_dict(), 'model_weights.pth')

if __name__ == "__main__":
    train_model()
