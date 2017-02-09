# Newspaper API
[Docker Hub](https://hub.docker.com/r/radumihail/newspaper-api/)

Api server that uses the Newspaper Python library to extract data from an article.

Port: 38765


## Running

`docker run -d -p 38765:38765 radumihail/newspaper-api`


## Usage

`localhost`:38765/?url=`https://github.com/codelucas/newspaper`

## Output Example:

```
{
  "authors": [ ],
  "image": "",
  "keywords": [ ],
  "summary": "",
  "text": "",
  "title": ""
} 
```