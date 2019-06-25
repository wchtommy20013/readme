# NPM

## Basic Commands

```
# Install/Uninstall module (Local, -g for Global [/usr/local/lib/node_modules])
npm install <module_name>
npm install <module_name>:<version_name>
npm uninstall <module_name> 

# List available Global npm modules
npm list -g --depth=0

# Register and Publish to private npm registry
# Remember to set `name` in package.json to be @registry_name/module_name before publishing
npm config set @registry_name:registry "<url_of_private_registry>"
npm publish
```

<hr>

## Private registry setup

1. Verdaccio (Open-Source)
2. MyGet (Paid, Enterprise-level with also Nuget, VSIX, Bower, etc. support)

### Verdaccio
(Recommended installation method: Docker)
```
docker pull verdaccio/verdaccio
docker run -it --rm --name verdaccio -p 4873:4873 verdaccio/verdaccio

# Verdaccio will run on port 4873
```

(Normal way)
```
sudo npm install -g verdaccio
#TODO
```