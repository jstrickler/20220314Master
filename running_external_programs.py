from subprocess import run, PIPE, CalledProcessError
import shlex

cmd = "netstat -an"
cmd_words = shlex.split(cmd)

print("cmd_words:", cmd_words, '\n')
# run(cmd_words)

process = run(cmd_words, stdout=PIPE, stderr=PIPE)

raw_output = process.stdout

# print(raw_output[:200])

output = raw_output.decode()

print(output[:200])

all_lines = output.splitlines()  # split on '\n'

print(len(all_lines))

all_remote_ips = set()
for line in all_lines:
    if "ESTAB" in line:
        fields = line.split()
        if len(fields) == 6:
            proto, rq, sq, local_addr, remote_addr, status = fields
            bytes = remote_addr.split('.')
            bytes.pop()
            remote_ip = '.'.join(bytes)
            all_remote_ips.add(remote_ip)
print()

print("REMOTE IPs")
for ip in sorted(all_remote_ips):
    print(ip)