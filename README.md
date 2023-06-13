# py-sec-vault
Hashicorp Vault implementation in python software


## Pre-requisites
To use this software, you need to have a running instance of Hashicorp Vault.
You can find the installation instructions [here](https://learn.hashicorp.com/vault/getting-started/install).

Alternatively, you can use the docker image provided by Hashicorp [here](https://hub.docker.com/_/vault/).

```bash
docker run --cap-add=IPC_LOCK \
  -e 'VAULT_LOCAL_CONFIG={"storage": {"file": {"path": "/vault/file"}}, "listener": [{"tcp": { "address": "0.0.0.0:8200", "tls_disable": true}}], "default_lease_ttl": "168h", "max_lease_ttl": "720h", "ui": true}' \
  -p 8200:8200 vault server
```

After this command, you can access the vault UI at http://localhost:8200
and follow the instructions to initialize the vault.

## Installation

```bash
pip install py-sec-vault
```

After this you should set environment variables to connect to the vault instance.

```
export VAULT_HOST=http://localhost:8200/
export VAULT_ENABLED=True|False
export VAULT_AUTH_METHOD=approle|token
export VAULT_MOUNT_POINT=<my_engine_name>
export VAULT_ROLE_ID=<my_vault_id>
export VAULT_SECRET_ID=<my_vauld_secret>
export VAULT_PATH=<my_vault_path>
```

## Usage

```python
from vault import from_env_or_vault

from_env_or_vault("DB_PASSWORD", default="admin")
```
