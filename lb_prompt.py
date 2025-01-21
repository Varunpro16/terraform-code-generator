lb_prompt.py = """
    Load Balancer Listener:

    Listens for incoming traffic on specified ports (HTTP/HTTPS) and forwards it to the target group.
    Target Group:

    Defines the backend targets (EC2 instances or containers).
    Configures health checks to monitor target health.
    Target Group Attachment:

    Registers targets (EC2 instances or containers) with the target group.
    Security Group:

    Allows HTTP/HTTPS traffic to the Load Balancer.
    Optionally allows specific ports to targets for backend communication.
    Outputs:

    Outputs the ALB DNS name or ARN for easy reference.

"""