#!/usr/bin/python
#requires paramiko:
#sudo pip install paramiko

import paramiko
import urlparse
import httplib
import os

# To Do:
# 1. test SSH connect to ELF
# 2. test SSH connect to rnzweb-wn-vm-podcast & rnzweb-ak-vm-podcast
# 3. upload audio
# 4. upload metadata
# place file in destination location

class ssh_session(): #object to use for duration of bulletin creation

	def __init__(self,):
		self.dest = ''
		self.port = ''
		self.user = ''
		self.key_file = ''

	def check_elf(self, dest, port, user, key_file, initial_wait=0, interval=0, retries=1):
		self.dest = dest
		self.port = port
		self.user = user
		self.key_file = key_file
		self.string = '/usr/bin/ncat --proxy-type http --proxy 172.17.8.1:3128 {} {}'.format(self.dest, self.port) #don't ask
		ssh = paramiko.SSHClient()
		self.sock=paramiko.ProxyCommand(self.string)
		ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
		print "testing SSH connectivity to {} as user {}".format(self.dest, self.user)
		ssh.connect(self.dest, username=self.user, key_filename=self.key_file, sock=self.sock)
		return True

	def check_podcast(self, dest, port, user, key_file, initial_wait=0, interval=0, retries=1):
		self.dest = dest
		self.port = port
		self.user = user
		self.key_file = key_file
		self.string = '/usr/bin/ncat --proxy-type http --proxy 172.17.8.1:3128 {} {}'.format(self.dest, self.port) #don't ask
		ssh = paramiko.SSHClient()
		self.sock=paramiko.ProxyCommand(self.string)
		ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
		print "testing SSH connectivity to {} as user {}".format(self.dest, self.user)
		ssh.connect(self.dest, username=self.user, key_filename=self.key_file, sock=self.sock)
		return True

if __name__ == '__main__':
  	rnzweb-wn-vm-rnz-app = '10.14.4.51'
  	rnzweb-ak-vm-rnz-app = '10.14.8.51'
  	rnzweb-wn-vm-podcast = '10.14.4.136'
  	rnzweb-ak-vm-podcast = '10.14.8.203'
	radionz-stg-app1 = '150.242.42.149'
	elf_port = 22
	elf_user = 'deploy'
	elf_key_file = '/home/deploy/.ssh/id_rsa.pub'
	podcast_server = '150.242.42.149' #testing for now
	podcast_port = 22
	podcast_user = 'deploy'
	podcast_key_file = '/home/deploy/.ssh/id_rsa.pub'
	test = ssh_session()
	result = test.check_elf(radionz-stg-app1, elf_port, elf_user, key_file)
	if result == True:
		print "ELF success bitches!!!"
	else:
		print "ELF failure bitches!!!"	
	result = test.check_podcast(podcast_server, podcast_port, elf_user, key_file)
	if result == True:
		print "ELF success bitches!!!"
	else:
		print "ELF failure bitches!!!"		