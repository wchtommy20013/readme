```
DATE=$(date +"%Y-%m-%d")
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

touch "${DIR}/${DATE}.bak"
```