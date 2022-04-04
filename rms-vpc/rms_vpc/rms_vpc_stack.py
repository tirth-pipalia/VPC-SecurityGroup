from aws_cdk import (
    aws_ec2 as ec2,
    Stack,
)
from constructs import Construct


class RmsVpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs, tags={
            "cost-center": "8998",
            "department": "Information-technology",
            "workload-name": "rms-webserver-prod"
        })

        vpcINPUT = self.node.try_get_context("vpcINPUT")
        subnetConfigurationINPUT = self.node.try_get_context("subnetConfigurationINPUT")
        vpc = ec2.Vpc(
            self,
            id=vpcINPUT["vpcId"],

            cidr=vpcINPUT["cpcCidr"],
            max_azs=vpcINPUT["vpcMaxAZ"],
            subnet_configuration=[
                ec2.SubnetConfiguration(name="Subnet1Public", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
                ec2.SubnetConfiguration(name="Subnet2Private", cidr_mask=24,
                                        subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            ],
            vpc_name=vpcINPUT["vpcName"]
        )

        securityGroupINPUT = self.node.try_get_context("securityGroupINPUT")
        securityGroup = ec2.SecurityGroup(
            self,
            securityGroupINPUT["securityGroupId"],
            security_group_name=securityGroupINPUT["securityGroupName"],
            vpc=vpc,
        )

        securityGroup.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(securityGroupINPUT["port1"])
        )
        securityGroup.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(securityGroupINPUT["port2"])
        )
        securityGroup.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(securityGroupINPUT["port3"])
        )
