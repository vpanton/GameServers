import pulumi
import pulumi_aws as aws

GameServersCluster = aws.ecs.Cluster ("GameServer", settings=[aws.ecs.ClusterSettingArgs(
	name="containerInsights", 
	value="enabled")])

pulumi.export("output", GameServersCluster)

