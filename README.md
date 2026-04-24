# KeyloggerSim (Educational Only!)

A simple python script that shows how a keylogger works and the danger behind it. 
This keylogger demo has the following purpose:
To demonstrate how keyloggers work to raise security awareness. This script ONLY logs to a local file and prints to the console. It does NOT send data over the network.

Real keyloggers are much more malicious and dangerous because of the following reasons:
- They run silently in the background (no visible window)
- They capture passwords, credit card numbers, private messages
- They exfiltrate data to a remote attacker server
- They persist across reboots via startup registry keys or scheduled tasks
- They can be bundled inside legitimate-looking software (trojan)

If you download the file and run it you can stop it by pressing CTRL+C or ESC.

You need pynput for this script. If you dont already have it install it with:
```
pip install pynput
```
This repository is purely for educational purposes!
