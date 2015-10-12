import forexconnect
import getpass

username = raw_input("username: ")
password = getpass.getpass("password: ")
connection = raw_input("connection: ")
client = forexconnect.ForexConnectClient(username,
                                         password,
                                         connection)
client.print_accounts()
trades = client.get_trades()
for t in trades:
    print t
client.logout()