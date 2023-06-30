from aws_cdk import (
    # Duration,
    Stack,
    App,
    aws_s3 as s3,
    RemovalPolicy
    # aws_sqs as sqs,
)
from constructs import Construct

class HelloCdkStack(Stack):

    def __init__(self, scope: App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "HelloCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        bucket = s3.Bucket(self, "MyFirstBucket", 
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )
