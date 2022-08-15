## Ansible concepts

### Control node
* run Ansible commands and playbooks by invoking the ansible or ansible-playbook
* any computer that has a Python installation as a control node

### Managed nodes
* The network devices (and/or servers) you manage with Ansible

### Inventory
* hostfile, specify information like IP address for each managed node.

### Collections
* are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins.

### Modules
* The units of code Ansible executes

### Tasks
* The units of action in Ansible. You can execute a single task once with an ad hoc command.

### Playbooks
* Ordered lists of tasks, saved so you can run those tasks in that order repeatedly
