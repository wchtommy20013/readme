js promise 

```
    public async validate() {

        let promises = [];
        for (let inAppId of this.configNames) {
            promises.push(this.service.configExists(inAppId));
        }

        let x = (await Promise.all(Object.values(promises)))

        for (let index in this.configNames) {
            if (x[index] === false) {
                this.warnings.add(`Missing config: ${this.configNames[index]}`);
            }
        }
        return this.warnings;
    }
```
