# Download and Launch kafka broker server
```
cd VM; 
<Merge files to create a OVA file>
```
### Launch VM
```
<Import OVA file as VM>
```

### Get IP of the server
ARPPing .sh
```
#!/bin/bash

# List network interface names
interface_names=($(ip link show | awk -F: '$0 !~ "lo|vir|docker" {print $2}'))

# Iterate through interface names and ping them
for interface in "${interface_names[@]}"; do
    echo "Pinging $interface..."
    ping -c 4 -I $interface 8.8.8.8  # Change the target IP address if needed
    echo "----------------------------------------"
done
```


```
$ VBoxManage showvminfo bitnami-kafka | grep MAC | awk -F':' '{print $3}'| awk -F',' '{print $1}'|awk '{$1=$1};1'| tr '[:upper:]' '[:lower:]' | sed 's/../&:/g;s/.$//' ### Get mac address of VM
$ 
$ VBoxManage guestproperty enumerate {`VBoxManage list runningvms | awk -F"{" '{print $2}'` | grep IP | awk -F"," '{print $2}' | awk '{print $2}'
```


# OLD (Purge later)
```
sudo docker-compose pull          # Pull dockers
sudo docker-compose build         # Build dockers
sudo docker-compose run consumer  # Run producer
sudo docker-compose run producer  # Run consumer
```
