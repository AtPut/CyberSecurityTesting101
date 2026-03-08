import argparse
import subprocess
import ipaddress

def ping_device(target):
    command = ['ping','-c','4',target]
    try:
        output = subprocess.check_output(command, shell=False, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(f"Failed to ping {target}\n{e.output.decode()}")
def validate(value):
    try:
        ipaddress.ip_address(value)
    except ValueError:
        raise ValueError("Invalid IP address!")
    return value
def main():
    parser = argparse.ArgumentParser(description="Ping a device. WARNING: This tool is vulnerable to command injection.")
    parser.add_argument("target", type=validate, help="IP address or DNS name of the target device")
    args = parser.parse_args()
    if args.target is not None:
        ping_device(args.target)

if __name__ == "__main__":
    main()
