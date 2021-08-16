# multi-lang-static-html-generator
multi-lang-static-html-generator

## Architecture
[embed.txt](https://github.com/Junhodo-side/multi-lang-static-html-generator/files/6994350/embed.txt)
### To Do
* support triggered by api(webhook)
* auto push generated file to remote repository


## needs 
* python v3.8.10, recommand pyenv 
* poetry
 
## install 

1. install poetry: `poetry install`
2. set env: `export PYTHONPATH={now your project root}`
3. set google translation json key path: `export GOOGLE_APPLICATION_CREDENTIALS={path of key}`


## usage

#### cli interface
* please execute in `{root of project}/app/interface/cmd`
* language code comply with iso 639-1
```
python generate.py --path {your_path} \
                   --src_lang {your_src_language_code} \
                   --dest_lang {your_dest_language_code}
```
* example command 
```
python generate.py --path ~/test/ko/tmp.html \
                   --src_lang ko \
                   --dest_lang en
```
