# Ansible Collection LLM

An Ansible Collection to manage reproducible environments for LLM testing applications

This project is currently in the planning stage.





Prompt construction / testing / storage

`{{ prompt stored in yaml or jinja template }} --> task`

## setup || config

```bash
# clone the repository and set Ansible ENV vars
git clone --recursive https://github.com:b08x/ansibleLLM.git

cd ansibleLLM

export ANSIBLE_HOME=$PWD
export ANSIBLE_CONFIG="$ANSIBLE_HOME/ansible.cfg"

```

## users and privilege escalation

1. create a **user** on the hosts for which are to be managed with Ansible. Add that user to the wheel group (or specify groups depending on your requirements)

  * either set NOPASSWD paramters for specific commands or use NOPASSWD:ALL. alternatively, set `become_ask_pass: True` to prompt for sudo password when tasks require it

2. in the inventory.yml file, set the **ansible_user** as the user created in the previous step. set statically or set an ENV var

```bash
export LLMADMIN=llmadmin
```

```yaml
all:
  vars:
    ansible_user: "{{ lookup('env','LLMADMIN') }}"
```

to run tasks with sudo privilege_escalation, set become at the end of the task:

```yaml
become: True
```

to run tasks as another user:

```yaml
become: True
become_user: "{{ user.name }}"
```


ssh to remote hosts as the user `exampleadmin` then run a task with sudo privilege_escalation:

```yaml
- hosts: servers
  remote_user: exampleadmin

  tasks:
    - name: A task that requires sudo privs
      package:
        name: docker
        state: present
        use: auto
      become: True
```

## playbooks

`base.yml`

Main playbook, includes all other playbooks.

`env.yml`

Configures programming language environments.

  * virtualenv for python
  * rvm for ruby

`user.yml`

Configures users

`audio.yml`

Perform audio analysis

## modules

aur
openai
langchain

## roles



## Data preprocessing / embedding

`data --> pre-processing --> embedding model --> vector database`

* tasks to create vector host and db
* tasks for pre-processing
* tasks to aquire embeddings
* tasks to store embeddings in vector db

### nlp

scripts/
  tokenizer.rb
  etc

injest documents

### prompt

store prompts as yaml files that can be use in various tasks

### database
postgresql + pgvector

### ruby

rails
ruby sintra

### python

streamit

### docker
