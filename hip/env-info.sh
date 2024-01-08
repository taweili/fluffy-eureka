echo "OS:" && cat /etc/os-release | grep -E "^(NAME=|VERSION=)";
echo "CPU: " && cat /proc/cpuinfo | grep "model name" | sort --unique;
echo "GPU:" && /opt/rocm/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)";
