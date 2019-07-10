import os
import paramiko
import getpass

def console_in():
    #print("Please enter your credentials:")
    #hostname = input("Host IP: ")
    #username = input("User: ")
    password = getpass.getpass(prompt='Password: ', stream=None)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname='69.30.23.70',username='nfarwell',password=password, look_for_keys=False)
    print(client.exec_command('echo hello world'))

def get_creds():
    print("Please enter your credentials:")
    hostname = input("Host IP: ")
    username = input("User: ")
    password = getpass.getpass(prompt='Password: ', stream=None)

console_in()
