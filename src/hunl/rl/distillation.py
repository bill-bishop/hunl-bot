import torch
import torch.nn.functional as F

class PolicyDistiller:
    """
    Distill policies from league into a single student.
    """
    def __init__(self, student, teacher_policies, lr=1e-3, device="cpu"):
        self.student = student.to(device)
        self.teachers = [t.to(device) for t in teacher_policies]
        self.optimizer = torch.optim.Adam(self.student.parameters(), lr=lr)
        self.device = device

    def step(self, obs):
        with torch.no_grad():
            teacher_probs = [torch.softmax(t(obs)[0], dim=-1) for t in self.teachers]
            target = torch.mean(torch.stack(teacher_probs), dim=0)

        student_logits, _, _ = self.student(obs)
        student_log_probs = torch.log_softmax(student_logits, dim=-1)
        loss = F.kl_div(student_log_probs, target, reduction="batchmean")

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return loss.item()
