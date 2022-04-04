#!/usr/bin/env python3
import os

import aws_cdk as cdk

from rms_vpc.rms_vpc_stack import RmsVpcStack


app = cdk.App()
env_ME = cdk.Environment(account="<12_digit_account_no>", region="me-south-1")
RmsVpcStack(app, "RmsVpcStack",env=env_ME)

app.synth()
