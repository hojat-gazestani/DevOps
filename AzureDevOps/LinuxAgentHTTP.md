sudo add-apt-repository ppa:rael-gc/rvm
sudo apt-get update
sudo apt install libssl1.0-dev
sudo -s
export AZP_AGENT_USE_LEGACY_HTTP=true

sudo ./svc.sh install
sudo ./svc.sh start
sudo ./svc.sh stop

https://azureserver.net/agent/2.210.1/vsts-agent-linux-x64-2.210.1.tar.gz

mkdir myagent && cd myagent
tar zxvf ~/Downloads/vsts-agent-linux-x64-2.210.1.tar.gz
./config.sh
./run.sh

