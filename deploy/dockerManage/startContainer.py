#!/usr/bin/env python3
import docker

class Container:
	def __init__(self):
		self.cli = docker.from_env()
	def start(self,service_port , image ,cmd):
		self.container = self.cli.containers.run(image,cmd,detach= True,ports={str(service_port)+'/tcp': service_port})
		print("%s create success!"%(self.container.name))

if __name__ == '__main__':
	print(Container().start(1111,'busybox','tail -f /etc/hosts'))
