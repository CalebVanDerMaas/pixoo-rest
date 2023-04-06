#!/bin/bash -xv


now="$(date -v-1d +'%Y-%m-%dT00:00:00-05:00')"
tomorrow="$(date +'%Y-%m-%dT00:00:00-05:00')"

response="$(curl -X POST https://api.notion.com/v1/databases/34f777ba0c9242a6a3f79d6046afc511/query \
    -H "Authorization: Bearer secret_OGWqaD18QVxXogzUF4KollLkNDhv6AgZNqJC8mv1Zbl" \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2021-08-16" \
    --data-raw '{
        "filter": {
            "and": [
                {
                    "property": "Due",
                    "date": {
                        "after": "'"$now"'"
                    }
                },
                {
                    "property": "Due",
                    "date": {
                        "before": "'"$tomorrow"'"
                    }
                }
            ]
        }
    }'
)"

answer=$(python /Users/calebvandermaas/Developer/Pixoo64Dev/pixoo-rest/examples/parser.py "$response"
)

echo $answer


