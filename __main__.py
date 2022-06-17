import pulumi
import pulumi_aws as aws

GameServersCluster = aws.ecs.Cluster ("GameServer", settings=[aws.ecs.ClusterSettingArgs(
	name="containerInsights", 
	value="enabled")])

Minecraft = aws.ecs.TaskDefinition("MinecraftBedrock", 
	family = "MinecraftBedrock",
	container_definitions=(lambda path: open(path).read())("containers/minecraft-bedrock-server.json"),
	network_mode="awsvpc",
	requires_compatibilities=["FARGATE"],
	cpu="1024",
	memory="2048")





# pulumi.export("output", GameServersCluster)

