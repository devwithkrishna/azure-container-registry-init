import os
import json
from dotenv import load_dotenv


def replication_config():
	"""
	Load the environment variables
	:return:
	"""
	enable_replication = os.getenv("enable_replication")
	print(f"Enable Replication is {enable_replication}")
	zone_redundancy_for_acr = os.getenv("zone_redundancy_for_acr")
	print(f"Zone Redundancy for ACR is {zone_redundancy_for_acr}")
	location = os.getenv("location")
	print(f"Location is {location}")

	# Check if replication is enabled
	if enable_replication.lower() == "true":
		georeplications = []
		if location == "eastus2":
			georeplications = [
				{"location": "centralus", "zone_redundancy_enabled": zone_redundancy_for_acr},
				{"location": "westeurope", "zone_redundancy_enabled": zone_redundancy_for_acr}
			]
		elif location == "westeurope":
			georeplications = [
				{"location": "northerneurope", "zone_redundancy_enabled": zone_redundancy_for_acr},
				{"location": "eastus2", "zone_redundancy_enabled": zone_redundancy_for_acr}
			]

		config = {"georeplications": georeplications}

		with open("config.json", "w") as file:
			json.dump(config, file, indent=4)

		print(f"Georeplications written to config.json: {georeplications}")
	else:
		print("Replication is not enabled")


def main():
	"""
	Run the code
	:return:
	"""
	load_dotenv()
	replication_config()


if __name__ == "__main__":
	main()