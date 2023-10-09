## Authors
<details>
    <summary>Agure Lameck</summary>
    <summary>Alex Kinyua</summary>
    <ul>
    <li><a href="https://github.com/Agure-la">Github</a></li>
    <li><a href="mailto:lameckagure@gmail.com">e-mail</a></li>
    <li><a href="https://github.com/Aleki001">Github</a></li>
    <li><a href="mailto:alexkinyua001alx@gmail.com">e-mail</a></li>
    </ul>
</details>

## How to add Author file
`Bash script for generating the list of authors in git repo`

#!/bin/sh

git shortlog -se
| perl -spe 's/^\s+\d+\s+//'
| sed -e '/^CommitSyncScript.*$/d' \
