Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "powershell.exe -ExecutionPolicy Bypass -File ""C:\Program Files\WireGuard\Data\Configurations\scripts\Auto_connect_wg.ps1""", 0, False
