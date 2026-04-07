@echo off
schtasks /Create ^
 /TN "\WireGuard\wireguard_on_demand" ^
 /TR "wscript.exe \"C:\Program Files\WireGuard\Data\Configurations\scripts\launch_hidden.vbs\"" ^
 /SC ONEVENT ^
 /EC "Microsoft-Windows-NetworkProfile/Operational" ^
 /MO "*[System[Provider[@Name='Microsoft-Windows-NetworkProfile'] and EventID=10000]]" ^
 /RU "%USERNAME%" ^
 /RL HIGHEST ^
 /F

timeout /t 1 >nul
powershell.exe -ExecutionPolicy RemoteSigned  -File "C:\Program Files\WireGuard\disable_battery_check.ps1"

timeout /t 1 >nul
powershell.exe -ExecutionPolicy RemoteSigned  -File "C:\Program Files\WireGuard\ONLOGON_ADDER.ps1"
