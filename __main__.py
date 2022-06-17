import pulumi
import pulumi_aws as aws

AZ = "us-east-1a"

ServiceSubnet = aws.ec2.get_subnet(availability_zone=AZ) 

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


MinecraftService = aws.ecs.Service("MinecraftBedrockService",
	cluster = GameServersCluster,
	task_definition = Minecraft,
	desired_count = 1,
	launch_type = "FARGATE",
	network_configuration = aws.ecs.ServiceNetworkConfigurationArgs(
		subnets = [ServiceSubnet.id],
		assign_public_ip = True))


pulumi.export("output", ServiceSubnet)

