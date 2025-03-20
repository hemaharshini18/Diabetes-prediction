import torch
import torch.nn as nn
import torch.nn.functional as F

# Define the ANN model class (same as in training)
class ANN_Model(nn.Module):
    def __init__(self, input_features=8, hidden1=20, hidden2=20, out_features=2):
        super().__init__()
        self.f_connected1 = nn.Linear(input_features, hidden1)
        self.f_connected2 = nn.Linear(hidden1, hidden2)
        self.out = nn.Linear(hidden2, out_features)

    def forward(self, x):
        x = F.relu(self.f_connected1(x))
        x = F.relu(self.f_connected2(x))
        x = self.out(x)
        return x

# Function to load the trained model
import torch

def load_model():
    # Load the entire model directly
    model = torch.load(r'C:\Users\hai\Documents\disease-prediction\model\diabetes.pt', 
                      map_location=torch.device('cpu'),weights_only=False)
    model.eval()  # Set the model to evaluation mode
    return model


# Function to make predictions
def predict(model, input_data):
    # Convert list to tensor
    input_tensor = torch.tensor(input_data, dtype=torch.float32).unsqueeze(0)  # Reshape for batch processing

    # Make a prediction
    with torch.no_grad():
        output = model(input_tensor)
        return output.argmax().item()  # Return predicted class (0 or 1)
