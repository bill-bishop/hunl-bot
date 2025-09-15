import torch

class PolicyExporter:
    """
    Exports trained policy networks to TorchScript or ONNX for inference.
    """

    @staticmethod
    def to_torchscript(model, path="policy.pt"):
        traced = torch.jit.trace(model, torch.randn(1, model.model[0].in_features))
        traced.save(path)
        print(f"Saved TorchScript policy to {path}")

    @staticmethod
    def to_onnx(model, path="policy.onnx"):
        dummy = torch.randn(1, model.model[0].in_features)
        torch.onnx.export(model, dummy, path, input_names=["obs"], output_names=["policy"])
        print(f"Saved ONNX policy to {path}")
