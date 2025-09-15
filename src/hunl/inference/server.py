from flask import Flask, request, jsonify
import torch

class InferenceServer:
    def __init__(self, model, device="cpu"):
        self.app = Flask(__name__)
        self.model = model.to(device)
        self.device = device

        @self.app.route("/act", methods=["POST"])
        def act():
            data = request.json
            obs = torch.tensor(data["obs"], dtype=torch.float32).to(self.device)
            with torch.no_grad():
                logits, value, _ = self.model(obs)
                probs = torch.softmax(logits, dim=-1).cpu().numpy().tolist()
            return jsonify({"probs": probs})

    def run(self, host="0.0.0.0", port=5000):
        self.app.run(host=host, port=port)

if __name__ == "__main__":
    # Placeholder: you would load a trained model here
    from hunl.rl.agents.networks import ActorCritic
    model = ActorCritic(input_dim=10, hidden_sizes=[64,64], num_actions=5)
    server = InferenceServer(model)
    server.run()
