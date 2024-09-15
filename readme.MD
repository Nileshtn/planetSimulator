run build.ps1
https://sourceforge.net/projects/vcxsrv/files/vcxsrv/1.20.14.0/vcxsrv-64.1.20.14.0.installer.exe/download install xsvr and start
run $env:DISPLAY = "host.docker.internal:0"
run run.ps1